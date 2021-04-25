//Base url to distinguish between localhost and production environment
const base_url = window.location.origin;
// instantiate object of helper class
const helper = new Helper();

const url_string = window.location.href;
const url = new URL(url_string);
let uid = url.searchParams.get('uid');

/**
 * Initialize View.
 *
 * @param {json, boolean} json_process
 */
function init(json_process = false) {

    helper.showLoadingScreen();

    getFeatures().then(data => {
        if (!json_process) {
            getProcess(data);
        } else {
            fillDataFields(data, json_process);
            loadComponentNames(json_process);
        }
    });

}

/**
 * Get list of features.
 */
async function getFeatures() {
    // Read JSON file
    return await fetch(base_url + '/content/mapping_metrics_definition.json')
        .then(response => response.json())
        .then(data => {
            let features = data['features'];

            //TODO: auskommentieren

            // createMetricsSection(features);

            document.getElementById('buttons').innerHTML = '';
            let div = document.createElement('div');
            div.className = 'control-area';

            let buttonType;
            if (typeof uid !== undefined && uid !== "" && uid != null) {
                buttonType = "Save";
            } else {
                buttonType = "Create";
            }
            div.innerHTML = `<button id="save-button" class="create-button" onclick="createEditProcess(); helper.showLoadingScreen()" type="button">${buttonType}</button>`

            // Append element to document
            document.getElementById('buttons').appendChild(div);
            return features;
        });
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

        // TODO: auslagern in helper js

        // Handle response of HTTP-request
        xhttp.onreadystatechange = function () {
            if (this.readyState === XMLHttpRequest.DONE && (this.status >= 200 && this.status < 300)) {
                // Process response and show sum in output field
                let processData = JSON.parse(this.responseText);
                fillDataFields(features, processData);
                loadComponentNames(processData);
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
 * This function fills the process data in all fields
 *
 * @param {json} features
 * @param {json} processData
 */
function fillDataFields(features, processData) {

    if (processData['success']) {
        // fill description column
        fillDescriptionColumn(processData);
        // create metric/feature toggle area
        createMetricsSection(features, processData);
        //
    } else {
        // Component has not been created/edited successfully
        window.alert('Process could not be loaded.');
    }
}

/**
 * This function fills the description fields
 *
 * @param {json} processData
 */

function fillDescriptionColumn(processData) {

    this.renderWholeProcessScoreCircle(processData['score']);

    // Set uid and data fields
    document.getElementById('process-name-textarea').value = processData['process']['name'];
    document.getElementById('process-responsible-person-textarea').value = processData['process']['responsible_person'];
    document.getElementById('process-beschreibung-textarea').value = processData['process']['description'];
}

/**
 * Render metrics section.
 *
 * @param {json} features
 * @param {json} processData
 */
function createMetricsSection(features, processData) {
    document.getElementById('metrics-input-processes').innerHTML = '';
    let featureCount = 0;
    Object.keys(features).forEach(function (key) {
        featureCount++;
        let feature = features[key];
        let metrics = feature['metrics'];

        let div = document.createElement('div');
        div.id = key;
        div.className = 'feature-section';


        // get all metric rows and the contained data
        let metric_fulfillment_list = [];
        let innerHTML_metric_block = '';
        let feature_component_count = 0;
        let feature_fulfillment;

        Object.keys(metrics).forEach(function (key) {
            let metric = metrics[key];
            let [metric_fulfillment, component_count, innerHTML_metric_row] = fillMetricRows(metric, key, processData);

            // append metric row to a metric row block for the feature
            innerHTML_metric_block += innerHTML_metric_row;

            // create a list of all metric fulfillments
            if (metric_fulfillment != null) {
                metric_fulfillment_list.push(metric_fulfillment);
            }

            // set component_count ( should be equal over all metrics contained in a feature)
            feature_component_count = component_count;
        });

        // calculate the feature fulfillment -> if one metric_fulfillment is false, the feature_fulfillment is also false
        if (metric_fulfillment_list.length === 0) {
            feature_fulfillment = null;
        } else {
            feature_fulfillment = !metric_fulfillment_list.includes(false);
        }

        let feature_header = "Feature " + featureCount + ": " + feature['name'] + " (Components: " + feature_component_count + ")";

        let innerHTML = '';
        innerHTML += '<div data-hover="" data-delay="0" class="accordion-item">';
        innerHTML += '<div class="accordion-toggle" onclick="helper.toggleSection(this)">';
        innerHTML += '<div class="accordion-icon"></div>';
        innerHTML += '<div class="features-label">' + feature_header + '</div>';
        innerHTML += helper.renderSmallCircle(feature_fulfillment);
        innerHTML += '</div>';
        innerHTML += '<nav class="dropdown-list">';
        innerHTML += '<div class="features-columns">';

        // Table Headers
        innerHTML += `
        <table id="process-feature-table">
            <tr>
                <th name="metric">Metric</th>
                <th name="average">
                    Average
                    <img src="images/info.png" loading="lazy" width="35" 
                        title="The average value for the respective metrics across all components in the process." 
                        class="info-icon-header">
                </th>
                <th name="standard-deviation">
                    Std. Dev.
                    <img src="images/info.png" loading="lazy" width="35" 
                        title="The standard deviation for each metric across all components in the process." 
                        class="info-icon-header">
                </th>
                <th name="sum">
                    Sum 
                    <img src="images/info.png" loading="lazy" width="35" 
                        title="The sum for each respective metric across all components in the process." 
                        class="info-icon-header">
                </th>
                <th name="min">
                    Min
                    <img src="images/info.png" loading="lazy" width="35" 
                        title="The minimum value specifies the smallest value for each respective metric across all components in the process."
                        class="info-icon-header">
                </th>
                <th name="max">
                    Max
                    <img src="images/info.png" loading="lazy" width="35" 
                        title="The maximum value indicates the largest value for each respective metric across all components of the process."
                        class="info-icon-header">
                </th>
                <th name="target-avg">
                    Target Average
                    <img src="images/info.png" loading="lazy" width="35" 
                        title="The average, user-entered, Target-value for each metric across all components in the process."
                        class="info-icon-header">
                </th>
                <th name="target-min">
                    Target Min
                    <img src="images/info.png" loading="lazy" width="35" 
                        title="The average, user-entered, Target-value for each metric across all components in the process."
                        class="info-icon-header">
                </th>
                <th name="target-max">
                    Target Max
                    <img src="images/info.png" loading="lazy" width="35" 
                        title="The average, user-entered, Target-value for each metric across all components in the process."
                        class="info-icon-header">
                </th>
                <th name="target-sum">
                    Target Sum
                    <img src="images/info.png" loading="lazy" width="35" 
                        title="The target sum for each metric across all components in the process."
                        class="info-icon-header">
                </th>
                <th name="ampel">Check</th>
                <th name="info">Info</th>
            </tr>`;

        innerHTML += innerHTML_metric_block;

        innerHTML += `</table>`;
        innerHTML += '</div>';
        innerHTML += '</nav>';
        innerHTML += '</div>';
        div.innerHTML = innerHTML;

        // Append element to document
        document.getElementById('metrics-input-processes').appendChild(div);
    });
    helper.hideLoadingScreen();
}

/**
 * Create a metric row for the table.
 *
 * @param {json} metricData
 * @param {string} slug
 * @param {json} processData
 */
function fillMetricRows(metricData, slug, processData) {

    // default value, because null has no influence on feature_fulfillment if metric_fulfillment is not given
    let metric_fulfillment = null;
    let count_component = 0;

    // default table row, when no metric data is provided
    let innerHTML_actual = `
                    <tr>
                        <td id="` + metricData['name'] + `">` + metricData['name'] + `</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>`;
    let innerHTML_target = `

                        <td><input name="target-average" id="${slug}" value=""></td>
                        <td><input name="target-minimum" id="${slug}" value=""></td>
                        <td><input name="target-maximum" id="${slug}" value=""></td>`;

    let innerHTML_fulfillment = `
                        <td></td>
                        <td></td>
                        <td><img src="images/info.png" loading="lazy" width="35"
                        title="` + metricData['description_process'] + `\ni.e. ` + metricData['example_process'] + `"
                        alt="" class="info-icon"></td>
                    </tr>`;

    if (uid != null && uid !== -1 && (slug in processData['actual_target_metrics'])) {

        if ('count_component' in processData['actual_target_metrics'][slug]) {
            count_component = processData['actual_target_metrics'][slug]['count_component'];
        }

        // check if actual values are provided
        if ('actual' in processData['actual_target_metrics'][slug]) {
            innerHTML_actual = `
                    <tr>
                        <td id="${metricData['name']}">${metricData['name']}</td>
                        <td>${processData['actual_target_metrics'][slug]['actual']['average']}</td>
                        <td>${processData['actual_target_metrics'][slug]['actual']['standard_deviation']}</td>
                        <td>${processData['actual_target_metrics'][slug]['actual']['total']}</td>
                        <td>${processData['actual_target_metrics'][slug]['actual']['min']}</td>
                        <td>${processData['actual_target_metrics'][slug]['actual']['max']}</td>`;
        }

        // check if target values are provided
        if ('target' in processData['actual_target_metrics'][slug]) {

            // replace null with empty strings, so that "null" is not entered in the table
            if (processData['actual_target_metrics'][slug]['target']['average'] == null) {
                processData['actual_target_metrics'][slug]['target']['average'] = '';
            }
            if (processData['actual_target_metrics'][slug]['target']['min'] == null) {
                processData['actual_target_metrics'][slug]['target']['min'] = '';
            }
            if (processData['actual_target_metrics'][slug]['target']['max'] == null) {
                processData['actual_target_metrics'][slug]['target']['max'] = '';
            }

            innerHTML_target = `
                        <td><input name="target-average" id="${slug}" value="${processData['actual_target_metrics'][slug]['target']['average']}"></td>
                        <td><input name="target-minimum" id="${slug}" value="${processData['actual_target_metrics'][slug]['target']['min']}"></td>
                        <td><input name="target-maximum" id="${slug}" value="${processData['actual_target_metrics'][slug]['target']['max']}"></td>`

        }

        // check if a fulfillment and consequentially a target sum is provided (if fulfillment was calculated, a target sum was also able to be calculated)
        if ('fulfillment' in processData['actual_target_metrics'][slug]) {
            metric_fulfillment = processData['actual_target_metrics'][slug]['fulfillment'];
            innerHTML_fulfillment = `
                        <td>${processData['actual_target_metrics'][slug]['target']['total']}</td>
                        <td>${helper.renderSmallCircle(metric_fulfillment)}</td>
                        <td><img src="images/info.png" loading="lazy" width="35" alt="heyy"
                         title="` + metricData['description_process'] + `\ni.e. ` + metricData['example_process'] + `"
                         class="info-icon"></td>
                    </tr>`;
        }
    }

    let innerHTML_metric_row = innerHTML_actual + innerHTML_target + innerHTML_fulfillment;

    return [metric_fulfillment, count_component, innerHTML_metric_row];
}


/**
 * Render process ball for whole process.
 *
 * @param wholeProcessScore
 */
function renderWholeProcessScoreCircle(wholeProcessScore) {
    let color;
    wholeProcessScore = parseInt(wholeProcessScore);

    color = helper.getCircleColor(wholeProcessScore);

    document.getElementById("whole-process-score").setAttribute("style", `background-color:  ${color}`);
    document.getElementById("whole-process-score").innerHTML = `${wholeProcessScore}%`;
}


/**
 * This function saves the data entered to the database by transmitting the data to the backend
 */

function createEditProcess() {

    let metric_elements_average = document.getElementsByName('target-average');
    let metric_elements_min = document.getElementsByName('target-minimum');
    let metric_elements_max = document.getElementsByName('target-maximum');

    let metrics = {};

    let text_replaced_flag = false; // Helper variable that indicates, whether or not a non quantitative metric input has been found and discarded
    for (let i = 0; i < metric_elements_average.length; i++) {

        // Replace non quantitative metric inputs with an emtpy string to have them discarded
        if (metric_elements_average[i].value !== '' && !parseFloat(metric_elements_average[i].value)) {
            metric_elements_average[i].value = '';
            text_replaced_flag = true;
        }
        if (metric_elements_min[i].value !== '' && !parseFloat(metric_elements_min[i].value)) {
            metric_elements_min[i].value = '';
            text_replaced_flag = true;
        }
        if (metric_elements_max[i].value !== '' && !parseFloat(metric_elements_max[i].value)) {
            metric_elements_max[i].value = '';
            text_replaced_flag = true;
        }

        // Process quantitative metrics to push them into the JSON Object to be passed to the backend
        let id = metric_elements_average[i].id;

        metrics[id] = {
            "average": null,
            "min": null,
            "max": null
        };

        if (metric_elements_average[i].value !== '') {
            metrics[id]["average"] = parseInt(metric_elements_average[i].value);
        }
        if (metric_elements_min[i].value !== '') {
            metrics[id]["min"] = parseInt(metric_elements_min[i].value);
        }
        if (metric_elements_max[i].value !== '') {
            metrics[id]["max"] = parseInt(metric_elements_max[i].value);
        }
    }

    // delete metric from json if no target metric (min, max, average) is entered
    for (var key in metrics) {
        if (metrics[key]["min"] == null && metrics[key]["max"] == null && metrics[key]["average"] == null) {
            delete metrics[key];
        }
    }

    if (typeof uid === undefined || uid === "" || uid == null) {
        uid = -1;
    }

    const process = `{
        "process": {
            "uid": "${uid}",
            "name": "${document.getElementById('process-name-textarea').value}",
            "responsible_person": "${document.getElementById('process-responsible-person-textarea').value}",
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
 * This function loads component names from json file
 *
 * TODO use modular helper functionality instead
 * @param processData
 */
function loadComponentNames(processData) {
    const base_url = window.location.origin;
    let xhttp = new XMLHttpRequest();
    xhttp.open("GET", base_url + "/content/mapping_metrics_definition.json", true);
    xhttp.setRequestHeader("Content-Type", "application/json");

    // Handle response of HTTP-request
    xhttp.onreadystatechange = function () {
        if (this.readyState === XMLHttpRequest.DONE && (this.status >= 200 && this.status < 300)) {
            // Process response and show sum in output field
            let metricsDefinition = JSON.parse(this.responseText);
            createComponentTable(processData, metricsDefinition);
            visualizeProcess(processData, metricsDefinition);
            helper.get_request("/component/overview", fillComponentDropdown);
        }
    }
    xhttp.send();
}

/**
 * This function renders the component drag and drop table
 *
 * @param {json} processData: JSON Object containing the process data loaded
 * @param {json} metricsDefinition: JSON Object containing the metrics definitions and component categories
 */
function createComponentTable(processData, metricsDefinition) {
    const components = processData['process']['components'];
    document.getElementById('ComponentOverviewTable').innerHTML = '';

    let header = document.createElement('tr');
    header.innerHTML = `
        <th name="Position"> Position</th>
        <th name="Component">Component</th>
        <th name="Category">Category</th>
        <th></th>
        <th></th>
        <th></th>
        <th></th>
        <th><i id="TrashIcon" class="fas fa-trash-alt"></i></th>
    `;
    document.getElementById('ComponentOverviewTable').appendChild(header);

    Object.keys(components).forEach(function (key) {
        const componentData = components[key];

        let component = document.createElement('tr');
        component.id = componentData['weight'];
        component.draggable = true;
        component.setAttribute('ondragstart', 'drag(event)');
        component.setAttribute('ondrop', 'drop(event)');
        component.setAttribute('ondragover', 'allowDrop(event)');
        component.setAttribute('ondragenter', 'enter(event)');
        component.setAttribute('ondragleave', 'exit(event)');

        component.innerHTML = `
            <td>${componentData['weight']}</td>
            <td>${componentData['name']}</td>
            <td>${metricsDefinition['categories'][componentData['category']]['name']}</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td><i id="TrashIcon" class="fas fa-trash-alt" onclick="deleteComponent(this.parentElement.parentElement.id); helper.showLoadingScreen()"></i></td>
        `;

        const componentTable = document.getElementById('ComponentOverviewTable');
        for (let i = componentTable.childElementCount - 1; i >= 0; i--) {
            const previousComponent = componentTable.children[i];
            if (i === 0) {
                insertAfter(previousComponent, component);
            } else if (componentData['weight'] > previousComponent.id) {
                insertAfter(previousComponent, component);
                break;
            }
        }
    });
}

/**
 * This function fills the component dropdown to enable the functionality of adding components to a process
 *
 * @param {json} componentData: A list of all components available through user input
 * */
function fillComponentDropdown(componentData) {
    let components = componentData['components'];
    document.getElementById('addposition').innerHTML = '';
    let defaultOption = document.createElement('option');
    defaultOption.value = 'default';
    defaultOption.innerHTML = 'Select';
    document.getElementById('addposition').appendChild(defaultOption);

    Object.keys(components).forEach(function (key) {
        let option = document.createElement('option');
        option.value = components[key]['uid'];
        option.innerHTML = components[key]['name'];
        document.getElementById('addposition').appendChild(option);
    });
}

/**
 * This function adds the selected component to the process
 */
function addComponent() {
    let componentUID = document.getElementById('addposition').value;
    if (componentUID.length === 32) {
        let weight = document.getElementById('ComponentOverviewTable').lastChild.id;
        if (weight === '') {
            weight = 1;
        } else {
            weight = parseFloat(weight) + 1;
        }

        let data = {
            "process_uid": uid,
            "component_uid": componentUID,
            "weight": weight
        };

        helper.post_request("/process/edit/createstep", JSON.stringify(data), init);
    } else {
        helper.hideLoadingScreen();
        // Please select a component from the dropdown.
        // TODO: Fill with something?
    }
}

/**
 * This function saves the component after weights have changed
 *
 * @param {float} oldWeight: The old weight of the component selected
 * @param {float} newWeight: The new weight of the component selected
 */
function editComponent(oldWeight, newWeight) {
    let data = {
        "uid": uid,
        "old_weight": oldWeight,
        "new_weight": newWeight
    };

    helper.post_request("/process/edit/editstep", JSON.stringify(data), init);
}

/**
 * This function deletes the selected component from the process
 *
 * @param {string} weight: The weight if the component to be deleted
 */
function deleteComponent(weight) {
    let data = {
        "uid": uid,
        "weight": parseFloat(weight)
    }

    helper.post_request("/process/edit/deletestep", JSON.stringify(data), init);
}

/**
 * This function allows for an element to have another element dropped upon
 *
 * @param {event} ev: The event associated with dragging and dropping elements
 */
function allowDrop(ev) {
    ev.preventDefault();
}

/**
 * This function handles the data to be transferred when an element gets dragged
 *
 * @param {event} ev: The event associated with dragging and dropping elements
 */
function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

/**
 * This function handles the data transfer when an element gets dropped
 *
 * @param {event} ev: The event associated with dragging and dropping elements
 */
function drop(ev) {
    ev.preventDefault();
    let data = ev.dataTransfer.getData("text");
    let element = document.getElementById(data);
    let oldWeight = parseFloat(element.id);
    insertAfter(ev.target.parentElement, element);

    let previousID;
    try {
        previousID = parseFloat(element.previousSibling.id);
        if (isNaN(previousID)) {
            previousID = parseFloat(element.id);
        }
    } catch (e) {
        previousID = parseFloat(element.id);
    }
    let nextID;
    try {
        nextID = parseFloat(element.nextSibling.id);
    } catch (e) {
        nextID = parseFloat(element.previousSibling.id) + 1;
    }
    let newWeight = parseFloat(previousID + (nextID - previousID) / 2);
    element.id = newWeight;
    element.children[0].innerHTML = newWeight;

    helper.showLoadingScreen();
    editComponent(oldWeight, newWeight);
}

/**
 * This function inserts an element after another specified one
 *
 * @param {HTMLElement} referenceNode: The element that the other element should be inserted after
 * @param {HTMLElement} newNode: The element to be inserted
 */
function insertAfter(referenceNode, newNode) {
    referenceNode.style.border = "inherit";
    referenceNode.parentNode.insertBefore(newNode, referenceNode.nextSibling);
}

/**
 * This function handles the styles when an element gets dragged over another specified one
 *
 * @param {event} ev: The event associated with dragging and dropping elements
 */
function enter(ev) {
    ev.target.parentElement.style.borderBottom = "15px solid black";
}

/**
 * This function handles the styles when an element gets dragged over another specified one and then exits the scope
 *
 * @param {event} ev: The event associated with dragging and dropping elements
 */
function exit(ev) {
    ev.target.parentElement.style.border = "inherit";
}

/**
 * This function visualizes the components of a process in a box above the components table
 *
 * @param {json} processData
 * @param {json} metricsDefinition
 * */
function visualizeProcess(processData, metricsDefinition) {
    let div = document.createElement("div");
    div.className = "modelling-processes";
    div.id = "visualizeprocess";
    let rectangle = "";
    let arrowRight = `<div class="arrow">&#8594;</div>`;
    let innerHTML = "";
    let components = processData['process']['components'];
    components.sort((a, b) => (a.weight > b.weight) ? 1 : ((b.weight > a.weight) ? -1 : 0));


    // begin at index 1 because 0 contains table headers
    for (let i = 0; i < components.length; i++) {
        let currentComponent = components[i];

        let componentName = currentComponent['name'];
        let componentCategory = metricsDefinition['categories'][currentComponent['category']]['name'];

        rectangle = renderRectangle(componentName, componentCategory);

        innerHTML += `<div class="visualize">${rectangle}</div>`;
        if (i < components.length - 1) {
            innerHTML += `<div class="visualize" >${arrowRight}</div>`;
        }

    }


    div.innerHTML = innerHTML;

    document.getElementById('modelling-process').innerHTML = ""; // reset div
    document.getElementById('modelling-process').appendChild(div); // populate div

    horizontalScroll();
}

/**
 * Returns rectangle HTML-Element to visualize one component in the process visualization.
 *
 * @param componentName
 * @param componentCategory
 * @returns {string} rectangle Element
 */
function renderRectangle(componentName, componentCategory) {
    return `
        <div class="square-border">
            <div class="componentname">${componentName}</div>
            <div class="componentcategory">${componentCategory}</div>
        </div>`;
}


/**
 * Makes the components visualization box from visualizeProcess() horizontally scrollable with the mouse-wheel
 */
function horizontalScroll() {
    document.getElementById("visualizeprocess").addEventListener('wheel', function (e) {
        if (e.type != 'wheel') {
            return;
        }
        let delta = ((e.deltaY || -e.wheelDelta || e.detail) >> 10) || 1;
        delta = delta * (-50);

        document.getElementById("visualizeprocess").scrollLeft -= delta;

        e.preventDefault();
    });
}

/**
 * This function gets called if saving was successful and reloads the page.
 *
 * @param {JSON} response
 */

function saveCallback(response) {
    // Process has been created/edited successfully
    helper.hideLoadingScreen();
    if (uid.length === 32) {
        init(response);
    } else {
        location.replace(location.href + '?uid=' + response['process']['uid']);
    }
}
