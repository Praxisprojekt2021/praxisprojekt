//Base url to distinguish between localhost and production environment
const base_url = window.location.origin;
// instantiate object of helper class
const helper = new Helper();

const url_string = window.location.href;
const url = new URL(url_string);
let uid = url.searchParams.get('uid');

/**
 * Initialize View.
 */
function init() {

    getFeatures().then(data => {
        getProcess(data);
    });
    // getProcess(features);

}

/**
 * Render process ball for whole process.
 * @param wholeProcessScore
 */
function renderWholeProcessScoreCircle(wholeProcessScore) {
    let color;
    wholeProcessScore = parseInt(wholeProcessScore);

    if(wholeProcessScore < 80) {
        color = "red";
    } else if (wholeProcessScore < 90) {
        color = "yellow"
    } else {
        color = "green";
    }
    document.getElementById("whole-process-score").setAttribute("style", `background-color:  ${color}`);
    document.getElementById("whole-process-score").innerHTML = `${wholeProcessScore}%`;
}

/**
 * Render ball for each metric.
 *
 * @param fulfillment
 * @returns {string}
 */
function renderCircle(fulfillment) {
    let color;
    if(fulfillment) {
        color = "green";
    } else {
        color = "red";
    }

    return `<div class="small-circle" style="background-color: ${color}"></div>`;
}

/**
* Get list of features.
 */
async function getFeatures() {
    // Read JSON file
    let features = await fetch(base_url + '/content/mapping_metrics_definition.json')
        .then(response => response.json())
        .then(data => {
            let features = data['features'];

            //TODO: auskommentieren

            // createMetricsSection(features);
            let div = document.createElement('div');
            div.className = 'control-area';

            let buttonType;
            if (typeof uid !== undefined && uid !="" && uid != null) {
                buttonType = "Save";
            } else {
                buttonType = "Create";
            }
            div.innerHTML = `<button id="save-button" class="create-button" onclick="createEditProcess()" type="button">${buttonType}</button>`//'<button="#" data-wait="Bitte warten..." id="save-button" class="create-button w-button" onclick="saveComponent()">Speichern</a>';

            // Append element to document
            document.getElementById('buttons').appendChild(div);
            return features;
        });
    return features;
}

/**
 * Fetches process data from BE.
 * @param features
 */

function getProcess(features) {
    const url_string = window.location.href;
    const url = new URL(url_string);
    let uid = url.searchParams.get('uid');

    // Check if view has received an uid as URL parameter to check whether to create a new component or edit an existing one
    if (uid && uid.length === 32) {
        // If so, load component data...
        console.log('Editing existing process');

        // Trigger function which gathers process data and processes it
        const post_data = `{
        "uid": "${uid}"
    }`
        const base_url = window.location.origin;
        let xhttp = new XMLHttpRequest();
        xhttp.open("POST", base_url + "/process/view", true);
        xhttp.setRequestHeader("Content-Type", "application/json");

        // Handle response of HTTP-request
        xhttp.onreadystatechange = function () {
            if (this.readyState === XMLHttpRequest.DONE && (this.status >= 200 && this.status < 300)) {
                // Process response and show sum in output field
                let processData = JSON.parse(this.responseText);
                createMetricsSection(features, processData);
            }
        }
        xhttp.send(post_data);
    } else {
        // If not, prepare for new component input...
        let processData = {};
        createMetricsSection(features, processData);
        console.log('Entering new process');
    }

}

/**
 * This functions toggles the accordion
 *
 * @param {HTMLElement} element: HTML accordion to be either opened oder closed
 */

function toggleSection(element) {
    const metric_child = element.parentElement.children[1];
    if (metric_child.style.display === "block" || element.getAttribute("disabled") === "true") {
        metric_child.style.display = "none";
    } else {
        metric_child.style.display = "block";
        metric_child.style.position = "static";
    }
}

/**
 * This function saves the data entered to the database by transmitting the data to the backend
 */

function createEditProcess() {

    document.getElementById('save-button').setAttribute("disabled","disabled");
    document.getElementById('save-button').style.backgroundColor='grey';


    let metric_elements = document.getElementsByName('target-average');
    let metrics = {};
    let text_replaced_flag = false; // Helper variable that indicates, whether or not a non quantitative metric input has been found and discarded
    for (let i = 0; i < metric_elements.length; i++) {
        // TODO also check if values are within min and max values
        // Replace non quantitative metric inputs with an emtpy string to have them discarded
        if (metric_elements[i].value !== '' && !parseFloat(metric_elements[i].value)) {
            metric_elements[i].value = '';
            text_replaced_flag = true;
        }
        // Process quantitative metrics to push them into the JSON Object to be passed to the backend
        if (metric_elements[i].value !== '') {
            metrics[metric_elements[i].id] = parseInt(metric_elements[i].value);
        }
    }
    if (typeof uid == undefined || uid == "" || uid == null) {
        uid = -1;
    }
        const process = `{
        "process": {
            "uid": "${uid}",  
            "name": "${document.getElementById('process-name-textarea').value}",
            "description": "${document.getElementById('process-beschreibung-textarea').value}"
    },
        "target_metrics": ${JSON.stringify(metrics)}
}`;

    // Check if all field have been filled
    // Also, when changing between categories, discard inputs made for non-relevant metrics
    let required_helper_flag = true; // Helper variable which gets set to false, if any required field is not filled
    const toggles = document.getElementsByName("target-average");
    console.log(toggles);
    for (let i = 0; i < toggles.length; i++) {
        console.log(toggles[i].value);
        const input = toggles[i].value;

        // Check if enabled fields have been filled - all fields are required
                if (toggles[i].value === '') {
                    console.log(toggles[i].id);
                    required_helper_flag = false;
                }
            }

    // If a input has been performed, post changes to backend
    if (required_helper_flag) {
        console.log(process);
        saveProcess(process);
    } else {
        let alert_string = 'Changes could not be saved. Please fill all metrics fields.';
        if (text_replaced_flag === true) {
            alert_string += '\nNon quantitative metrics have been automatically discarded.';
        }
        window.alert(alert_string);
    }
}

/**
 * Saves data.
 * @param data
 */
function saveProcess(data) {
    helper.post_request("/process/create_edit", data, saveCallback);
}


/**
 * Render metrics section.
 *
 * @param {json} features
 * @param {json} processData
 */
function createMetricsSection(features, processData) {
    // Check if the request has succeeded
    if (processData['success']) {
        // Component data has been received

        this.renderWholeProcessScoreCircle(processData['score']);

        // Set uid and data fields
        document.getElementById('process-name-textarea').value = processData['process']['name'];
        document.getElementById('process-beschreibung-textarea').value = processData['process']['description'];
    }

        let featureCount=0;
    Object.keys(features).forEach(function (key) {
        featureCount++;
        let feature = features[key];
        let metrics = feature['metrics'];

        let div = document.createElement('div');
        div.id = key;
        div.className = 'feature-section';

        let innerHTML = '';
        innerHTML += '<div data-hover="" data-delay="0" class="accordion-item">';
        innerHTML += '<div class="accordion-toggle" onclick="toggleSection(this)">';
        innerHTML += '<div class="accordion-icon"></div>';
        innerHTML += ('<div class="features-label">' + feature['name'] + '</div>');
        innerHTML += '</div>';
        innerHTML += '<nav class="dropdown-list">';
        innerHTML += '<div class="features-columns">';

        // Table Headers
        innerHTML += `
        <label>Feature ${featureCount}: ${feature['name']}</label>
        <table id="process-feature-table">
            <tr>
                <th name="metric">Metric</th>
                <th name="average">Average</th>
                <th name="standard-deviation">Std. Dev.</th>
                <th name="sum">Sum</th>
                <th name="min">Min</th>
                <th name="max">Max</th>
                <th name="target-avg">Target Average</th>
                <th name="target-sum">Target Sum</th>
                <th name="ampel">Check</th>
                <th name="info">Info</th>
            </tr>`;
        Object.keys(metrics).forEach(function (key) {
            let metric = metrics[key];

            // default table row, when no metric data is provided
            let innerHTML_actual = `
                    <tr>
                        <td id="${metric['name']}">${metric['name']}</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>`;
            let innerHTML_target = `
                        <td><input name="target-average" id="${key}" value=""></td>`;
            let innerHTML_fulfillment = `
                        <td></td>
                        <td></td>
                        <td><img src="images/info.png" loading="lazy" width="35" alt="" class="info-icon"></td>
                    </tr>`;

            if(uid != null && uid != -1 && processData['actual_target_metrics'][key]) {

                // check if actual values are provided
                if(processData['actual_target_metrics'][key]['actual']) {
                    innerHTML_actual = `
                    <tr>
                        <td id="${metric['name']}">${metric['name']}</td>
                        <td>${processData['actual_target_metrics'][key]['actual']['average']}</td>
                        <td>${processData['actual_target_metrics'][key]['actual']['standard_deviation']}</td>
                        <td>${processData['actual_target_metrics'][key]['actual']['total']}</td>
                        <td>${processData['actual_target_metrics'][key]['actual']['min']}</td>
                        <td>${processData['actual_target_metrics'][key]['actual']['max']}</td>`;
                }

                // check if a target value is provided
                if(processData['actual_target_metrics'][key]['target']) {
                    innerHTML_target =`
                        <td><input name="target-average" id="${key}" value="${processData['actual_target_metrics'][key]['target']['average']}"></td>`
                }

                // check if a fulfillment and consequentially a target sum is provided (if fulfillment was calculated, a target sum was also able to be calculated)
                if(processData['actual_target_metrics'][key]['fulfillemt']) {
                    innerHTML_fulfillment = `
                        <td>${processData['actual_target_metrics'][key]['target']['total']}</td>
                        <td>${renderCircle(processData['actual_target_metrics'][key]['fulfillment'])}</td>
                        <td><img src="images/info.png" loading="lazy" width="35" alt="" class="info-icon"></td>
                    </tr>`;
                }
            }

            innerHTML += innerHTML_actual + innerHTML_target + innerHTML_fulfillment;

        });

    innerHTML += `</table>`;
    innerHTML += '</div>';
        innerHTML += '</nav>';
        innerHTML += '</div>';
        div.innerHTML = innerHTML;

        // Append element to document
        document.getElementById('metrics-input-processes').appendChild(div);
    });
}

/**
 * This function checks for success in communication
 *
 * @param {string} response: JSON Object response, whether the changes have been saved successfully
 */

function saveCallback(response) {
    // Check if component has been created/edited successfully
    if (response['success']) {
        // Component has been created/edited successfully
        window.alert('Changes were saved.');
        window.location = base_url;
    } else {
        // Component has not been created/edited successfully
        window.alert('Changes could not be saved.');
    }
}