//Base url to distinguish between localhost and production environment
const base_url = window.location.origin;
// instantiate object of helper class
const helper = new Helper();
let uid = null;

function init() {
    const url_string = window.location.href;
    const url = new URL(url_string);

    getFeatures().then(data => {
        getProcess(data);
    });
    // getProcess(features);


    // TODO: change param to process score of the process
    this.renderWholeProcessScoreCircle(12);
}

function renderWholeProcessScoreCircle(wholeProcessScore) {
    if(wholeProcessScore < 75) {
        document.getElementById("whole-process-score").setAttribute("background-color", "red");
    } else {
        document.getElementById("whole-process-score").setAttribute("background-color", "green");
    }
    document.getElementById("whole-process-score").innerHTML = `${wholeProcessScore}%`;
}

/**
 * TODO comment here
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
 * This function fetches the process data from the backend
 *
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


    let metric_elements = document.getElementsByClassName('metric-input');
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
            metrics[metric_elements[i].id] = metric_elements[i].value;
        }
    }

    const component = {
        "uid": document.getElementById('component-uid').value,
        "name": document.getElementById('component-name').value,
        "category": document.getElementById('component-category').value,
        "description": document.getElementById('component-description-textarea').value,
        "metrics": metrics
    }

    // Check if all field have been filled
    // Also, when changing between categories, discard inputs made for non-relevant metrics
    let required_helper_flag = true; // Helper variable which gets set to false, if any required field is not filled
    const toggles = document.getElementsByClassName('feature-section');
    for (let i = 0; i < toggles.length; i++) {
        const feature_child = toggles[i].children[0].children[0];
        const metrics_child = toggles[i].children[0].children[1];
        const metrics_child_input_fields = metrics_child.getElementsByTagName('input');

        // Check if metric is mandatory or even not allowed
        if (feature_child.getAttribute("disabled") === "true") {
            // Discard data from disabled metrics inputs
            for (let i = 0; i < metrics_child_input_fields.length; i++) {
                metrics_child.getElementsByTagName('input')[i].value = '';
            }
        } else {
            // Check if enabled fields have been filled - all fields are required
            for (let i = 0; i < metrics_child_input_fields.length; i++) {
                if (metrics_child.getElementsByTagName('input')[i].value === '') {
                    console.log(metrics_child.getElementsByTagName('input')[i].id);
                    required_helper_flag = false;
                }
            }
        }
        if(document.getElementById("component-category").value == "default") {
            required_helper_flag = false;
        }
    }

    // If a input has been performend, post changes to backend
    if (required_helper_flag) {
        helper.post_request('/component/create_edit', JSON.stringify(component), saveCallback);
    } else {
        let alert_string = 'Changes could not be saved. Please fill all metrics fields.';
        if (text_replaced_flag === true) {
            alert_string += '\nNon quantitative metrics have been automatically discarded.';
        }
        window.alert(alert_string);
    }
}

/**
 * Render metrics section.
 *
 * @param {json} features
 */
function createMetricsSection(features, processData) {
    // Check if the request has succeeded
    if (processData['success']) {
        // Component data has been received

        // Set uid and data fields
        document.getElementById('process-name-textarea').value = processData['process']['name'];
        document.getElementById('process-beschreibung-textarea').value = processData['process']['description'];
    }

        let i=0;
    Object.keys(features).forEach(function (key) {
        i++;
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
        // TODO: Tabellenheader erzeugen
        innerHTML += `
        <label>Feature ${i}: ${feature['name']}</label>
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
                <th name="ampel"></th>
                <th name="info">Info</th>
            </tr>`;
        Object.keys(metrics).forEach(function (key) {
            let metric = metrics[key];
            console.log(processData);
            console.log(key)
            //TODO: if wieder entfernen, ist nur weil es nicht überall die id gibt momentan!
            if(processData['actual_target_metrics'][key]) {
                let metricId = metric;
                console.log("test")




                // TODO: hier Tabelle erzeugen
                innerHTML += `
            <tr>
                <td id="${metric['name']}">${metric['name']}</td>
                <td>${processData['actual_target_metrics'][key]['actual']['average']}</td>
                <td>${processData['actual_target_metrics'][key]['actual']['standard_deviation']}</td>
                <td>${processData['actual_target_metrics'][key]['actual']['standard_deviation']}</td>
                <td>${processData['actual_target_metrics'][key]['actual']['total']}</td>
                <td>${processData['actual_target_metrics'][key]['actual']['min']}</td>
                <td>${processData['actual_target_metrics'][key]['actual']['max']}</td>
                <td><img src="images/info.png" loading="lazy" width="35" alt="" class="info-icon"></td>
            </tr>`
            }
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