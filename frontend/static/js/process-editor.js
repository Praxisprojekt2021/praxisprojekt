// Base url to distinguish between localhost and production environment
const base_url = window.location.origin;
// Instantiate object of helper class
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

    Helper.showLoadingScreen();

    getFeatures().then(data => {
        // If page is reloaded (after saving) processes are updated else => page is loaded from databased and entries are prepared
        getTableHeaderInfo().then(tableHeaderInfo => {
                if (!json_process) {
                    getProcess(data, tableHeaderInfo);

                } else {
                    fillDataFields(data, json_process, tableHeaderInfo);
                    loadComponentNames(json_process);
                }
            }
        );
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

            document.getElementById('buttons').innerHTML = '';
            let div = document.createElement('div');
            div.className = 'control-area';

            let buttonType;
            if (typeof uid !== undefined && uid !== "" && uid != null) {
                buttonType = "Save";
            } else {
                buttonType = "Create";
            }
            div.innerHTML = `<button id="save-button" class="create-button" onclick="createEditProcess()" type="button"> ` + buttonType + ` </button>`

            // Append element to document
            document.getElementById('buttons').appendChild(div);
            return features;
        });
}

/**
 * Get list of process features.
 */
async function getTableHeaderInfo() {
    // Read JSON file
    return await fetch(base_url + '/content/table_header_info.json')
        .then(response => response.json())
        .then(data => {
            let tableHeaderInfo = data['headerInfo'];
            return tableHeaderInfo;
        });
}


/**
 * Fetches process data from BE.
 * @param features
 * @param tableHeaderInfo
 */

function getProcess(features, tableHeaderInfo) {
    const url_string = window.location.href;
    const url = new URL(url_string);
    let uid = url.searchParams.get('uid');

    // Check if view has received an uid as URL parameter to check whether to create a new process or edit an existing one
    if (uid) {
        // If so, load process data...
        console.log('Editing existing process');

        // Trigger function which gathers process data and processes it
        const post_data = `{
            "uid": "` + uid + `"
        }`;

        helper.http_request("POST", "/process/view", true, post_data, function (processData) {
            fillDataFields(features, processData, tableHeaderInfo);
            loadComponentNames(processData);
        });

    } else {
        // If not, prepare for new process input...
        let processData = {};
        createMetricsSection(features, processData, tableHeaderInfo);
        console.log('Entering new process');
    }
}

/**
 * This function fills the process data in all fields
 *
 * @param {json} features
 * @param {json} processData
 * @param {json} tableHeaderInfo
 */
function fillDataFields(features, processData, tableHeaderInfo) {

    if (processData['success']) {
        // fill description column
        fillDescriptionColumn(processData);
        // create metric/feature toggle area
        createMetricsSection(features, processData, tableHeaderInfo);
        //
    } else {
        // Component has not been created/edited successfully
        //window.alert('Process could not be loaded.');
        // Error will be shown in showError
        window.location.href = '/';
    }
}

/**
 * This function fills the description fields
 *
 * @param {json} processData
 */

function fillDescriptionColumn(processData) {

    renderWholeProcessScoreCircle(processData['score']);

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
 * @param {json} tableHeaderInfo
 */
function createMetricsSection(features, processData, tableHeaderInfo) {
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
        innerHTML += '<div class="accordion-icon-dropdown-toggle">&#709</div>';
        innerHTML += '<div class="features-label">' + feature_header + '</div>';
        innerHTML += helper.renderSmallCircle(feature_fulfillment);
        innerHTML += '</div>';
        innerHTML += '<nav class="dropdown-list" data-collapsed="true">';
        innerHTML += '<div class="features-columns">';

        // Table Headers
        innerHTML += `
        <table class="responsive-table" id="process-feature-table">
            <tr class="table-header">
                <th class="col-1" ></th>
                <th class="col-2 info-text-popup" tooltip-data="` + tableHeaderInfo['average']['helper'] + `">
                ` + tableHeaderInfo['average']['name'] + `
                </th>
                <th class="col-3 info-text-popup" tooltip-data="` + tableHeaderInfo['standard-deviation']['helper'] + `">
                ` + tableHeaderInfo['standard-deviation']['name'] + `
                </th>
                <th class="col-4 info-text-popup" tooltip-data="` + tableHeaderInfo['sum']['helper'] + `">
                ` + tableHeaderInfo['sum']['name'] + `
                </th>
                <th class="col-5 info-text-popup" tooltip-data="` + tableHeaderInfo['min']['helper'] + `">
                ` + tableHeaderInfo['min']['name'] + `
                </th>
                <th class="col-6 info-text-popup" tooltip-data="` + tableHeaderInfo['max']['helper'] + `">
                ` + tableHeaderInfo['max']['name'] + `
                </th>
                <th class="col-7 info-text-popup" tooltip-data="` + tableHeaderInfo['target-min']['helper'] + `">
                ` + tableHeaderInfo['target-min']['name'] + `
                </th>
                <th class="col-8 info-text-popup" tooltip-data="` + tableHeaderInfo['target-max']['helper'] + `">
                ` + tableHeaderInfo['target-max']['name'] + `
                </th>
                <th class="col-9 info-text-popup" tooltip-data="` + tableHeaderInfo['target-avg']['helper'] + `">
                ` + tableHeaderInfo['target-avg']['name'] + `
                </th>
                <th class="col-10 info-text-popup" tooltip-data="` + tableHeaderInfo['target-sum']['helper'] + `">
                ` + tableHeaderInfo['target-sum']['name'] + `
                </th>
                <th class="col-11">` + tableHeaderInfo['check']['name'] + `</th>
                <th class="col-12">` + tableHeaderInfo['info']['name'] + `</th>
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

    checkCorrectInputs();
    Helper.hideLoadingScreen();
}

function checkCorrectInputs() {

    // Live check for correct inputs
    let names = ['target-average', 'target-minimum', 'target-maximum'];
    names.forEach(element => {
        const inputs = document.getElementsByName(element);
        for (let i = 0; i < inputs.length; i++) {
            // Adding popup for target avg, min, and max input -> with min max values if they exist
            helper.addMinMaxPopup(inputs[i]);
            // Adding event listener for input check
            inputs[i].addEventListener('blur', (event) => {
                if (!helper.targetAvgIsWithinMinMax(inputs[i])) {
                    inputs[i].style.setProperty("border-color", "red", undefined);
                } else {
                    inputs[i].style.removeProperty("border-color");
                }
            });
        }
    });
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

    let binary = metricData['binary'];
    // default table row, when no metric data is provided
    let innerHTML_actual = `
                    <tr>
                        <td class="col-1" id="` + metricData['name'] + `">` + metricData['name'] + `</td>
                        <td class="col-2" ></td>
                        <td class="col-3" ></td>
                        <td class="col-4" ></td>
                        <td class="col-5" ></td>
                        <td class="col-6" ></td>`;

    let innerHTML_target = [];
        innerHTML_target['min'] =
            `<td class="col-7" ><input type="text" name="target-minimum" id="` + slug + `"`; // Rest of the string is added below
        innerHTML_target['max'] =
            `<td class="col-8" ><input type="text" name="target-maximum" id="` + slug + `"`; // Rest of the string is added below
        innerHTML_target['average'] = `
             <td class="col-9" ><input type="text" name="target-average" id="` + slug + `"`; // Rest of the string is added below
    let innerHTML_total = `
                        <td class="col-10" ></td>`;
    let innerHTML_fulfillment = `
                        <td class="col-11" ></td>
                        <td class="col-12" ><div tooltip-data="` + metricData['description_process'] + `\ni.e. ` + metricData['example_process'] + `"
                         class="info-text-popup"><img class="info-icon" src="images/info.png" loading="lazy" width="35"
                         ></div></td>
                    </tr>`;

    if (uid != null && uid !== -1 && (slug in processData['actual_target_metrics'])) {

        let actual_target_metrics = processData['actual_target_metrics'][slug];

        if ('count_component' in actual_target_metrics) {
            count_component = actual_target_metrics['count_component'];
        }

        // check if actual values are provided
        if ('actual' in actual_target_metrics) {
            innerHTML_actual = getMetricRowActual(actual_target_metrics, metricData);
        }

        // check if target values are provided
            if ('target' in actual_target_metrics) {
                innerHTML_target = getMetricRowTarget(innerHTML_target, actual_target_metrics, slug, binary);

                innerHTML_total = getMetricRowTotal(actual_target_metrics, binary);
            }


        // check if a fulfillment and consequentially a target sum is provided (if fulfillment was calculated, a target sum was also able to be calculated)
        if ('fulfillment' in processData['actual_target_metrics'][slug]) {
            metric_fulfillment = processData['actual_target_metrics'][slug]['fulfillment'];
            innerHTML_fulfillment = `
                        <td class="col-11" >` + helper.renderSmallCircle(metric_fulfillment) + ` </td>
                        <td class="col-12" ><div tooltip-data="` + metricData['description_process'] + `\ni.e. ` + metricData['example_process'] + `"
                         class="info-text-popup"><img class="info-icon" src="images/info.png" loading="lazy" width="35"
                         ></div></td>
                    </tr>`;
        }
    }

    Object.keys(innerHTML_target).forEach(function (key) {
        innerHTML_target[key] = addMinMaxToInputFields(innerHTML_target[key], metricData);
    });

    let innerHTML_metric_row = innerHTML_actual + innerHTML_target['min'] + innerHTML_target['max'] + innerHTML_target['average'] + innerHTML_total + innerHTML_fulfillment;

    return [metric_fulfillment, count_component, innerHTML_metric_row];
}


function getMetricRowActual(actual_target_metrics, metricData) {
    let binary = metricData['binary'];

    let actualAverage;
    let actualStandardDev;
    let actualTotal;
    let actualMin;
    let actualMax;

    if (!binary) {
        actualAverage = Math.round(actual_target_metrics['actual']['average'] * 100 + Number.EPSILON) / 100;
        actualStandardDev = Math.round(actual_target_metrics['actual']['standard_deviation'] * 100 + Number.EPSILON) / 100;
        actualTotal = Math.round(actual_target_metrics['actual']['total'] * 100 + Number.EPSILON) / 100;
        actualMin = Math.round(actual_target_metrics['actual']['min'] * 100 + Number.EPSILON) / 100;
        actualMax = Math.round(actual_target_metrics['actual']['max'] * 100 + Number.EPSILON) / 100;
    } else {
        actualAverage = Math.round(actual_target_metrics['actual']['average'] * 100 + Number.EPSILON) + "%";
        actualStandardDev = Math.round(actual_target_metrics['actual']['standard_deviation'] * 100 + Number.EPSILON) + "%";
        actualTotal = "-";
        actualMin = "-";
        actualMax = "-";
    }
    return `
                <tr>
                    <td class="col-1"  id="` + metricData['name'] + `">` + metricData['name'] + ` </td>
                    <td class="col-2" >` + actualAverage + `</td>
                    <td class="col-3" >` + actualStandardDev + `</td>
                    <td class="col-4" >` + actualTotal + `</td>
                    <td class="col-5" >` + actualMin + `</td>
                    <td class="col-6" >` + actualMax + `</td>`;
    }

function getMetricRowTarget(innerHTML_target, actual_target_metrics, slug, binary) {

    let targetValues = {};

    Object.keys(innerHTML_target).forEach(function (key) {
        if (actual_target_metrics['target'][key] !== null) {
            targetValues[key] = Math.round(actual_target_metrics['target'][key] * 100 + Number.EPSILON) / 100;
        } else {
            targetValues[key] = '';
        }
    });

    // replace null with empty strings, so that "null" is not entered in the table
    if (!binary) {
    innerHTML_target['min'] = `
                        <td class="col-7" ><input type="text" name="target-minimum" id = "` + slug + `" value="` + targetValues['min'] + `"`;
    innerHTML_target['max'] = `
                        <td class="col-8" ><input type="text" name="target-maximum" id = "` + slug + `" value="` + targetValues['max'] + `"`;
    innerHTML_target['average'] = `
                        <td class="col-9" ><input type="text" name="target-average" + id = "` + slug + `" value="` + targetValues['average'] * 100 + `"`;
    } else {
        innerHTML_target['min'] = `
                        <td class="col-7" ><input type="text" name="target-minimum" id = "` + slug + `" disabled`;
        innerHTML_target['max'] = `
                        <td class="col-8" ><input type="text" name="target-maximum" id = "` + slug + `" disabled`;
        innerHTML_target['average'] = `
                        <td class="col-9" ><input type="text" name="target-average" binary="true" + id = "` + slug + `" value="` + targetValues['average'] * 100 + `"`;
    }
    return innerHTML_target;
}

function getMetricRowTotal(actual_target_metrics, binary) {

    let targetTotalValue = "";
    if (!binary) {
        if ('total' in actual_target_metrics['target']) {
            targetTotalValue = Math.round(actual_target_metrics['target']['total'] * 100 + Number.EPSILON) / 100;
        }
    } else {
        targetTotalValue = "-";
    }

    return `<td class="col-10" >` + targetTotalValue + `</td>`;
}


function addMinMaxToInputFields(innerHTML_target, metricData) {
    let binary = metricData['binary'];
    // Rest of the innerHTML_target string
    if (!binary) {
        if (metricData['min_value'] >= 0) innerHTML_target += ' min="' + metricData['min_value'] + '"';
        if (metricData['max_value'] >= 0) innerHTML_target += ' max="' + metricData['max_value'] + '"';
    } else {
        innerHTML_target += ' min="' + 0 + '%"';
        innerHTML_target += ' max="' + 100 + '%"';
    }
    innerHTML_target += `></td>`;

    return innerHTML_target;

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

    if (!isNaN(wholeProcessScore)) {
        document.getElementById("whole-process-score").style.setProperty("background-color", color);
        document.getElementById("whole-process-score").style.setProperty("display", "flex");
        document.getElementById("whole-process-score").innerHTML = wholeProcessScore + `%`;
    } else {
        document.getElementById("whole-process-score").style.setProperty("display", "none");
    }
}


/**
 * This function saves the data entered to the database by transmitting the data to the backend
 */

function createEditProcess() {
    Helper.showLoadingScreen();
    let metric_elements = {};
    metric_elements['average'] = document.getElementsByName('target-average');
    metric_elements['min'] = document.getElementsByName('target-minimum');
    metric_elements['max'] = document.getElementsByName('target-maximum');

    let metrics = {};

    let text_replaced_flag = false; // Helper variable that indicates, whether or not a non quantitative metric input has been found and discarded
    let minmaxlist = ""; // List for Metrics that are not within min or max
    let process_name_empty = false; // Helper variable that indicates, whether or not the process name is given
    for (let i = 0; i < metric_elements['average'].length; i++) {

        // Process quantitative metrics to push them into the JSON Object to be passed to the backend
        let id = metric_elements['average'][i].id;

        metrics[id] = {
            "average": null,
            "min": null,
            "max": null
        };

        // Replace non quantitative metric inputs with an emtpy string to have them discarded
        Object.keys(metric_elements).forEach(function (key) {
            if (metric_elements[key][i].value !== '' && isNaN(metric_elements[key][i].value)) {
                metric_elements[key][i].value = '';
                text_replaced_flag = true;
            }

            if (metric_elements[key][i].value !== '') {
                if (key === "average" && metric_elements['average'][i].hasAttribute("binary")) {
                        metrics[id][key] = parseFloat(metric_elements[key][i].value) / 100;
                } else {
                    metrics[id][key] = parseFloat(metric_elements[key][i].value);
                }
                if (!helper.targetAvgIsWithinMinMax(metric_elements[key][i])) {
                    minmaxlist += '\n' + metric_elements[key][i].parentElement.parentElement.children[0].id; //TODO: Add metric name to the list of wrong target avg values (von Roman?)
                    metric_elements[key][i].style.setProperty("border-color", "red", undefined); //TODO: noch nötig oder nicht durch EventListener schon abgedeckt? (von Jasmin)
                } else {
                    metric_elements[key][i].style.removeProperty("border-color"); //TODO: noch nötig oder nicht durch EventListener schon abgedeckt? (von Jasmin)
                }
            }

        });
    }

    // delete metric from json if no target metric (min, max, average) is entered
    for (const key in metrics) {
        if (metrics[key]["min"] == null && metrics[key]["max"] == null && metrics[key]["average"] == null) {
            delete metrics[key];
        }
    }

    if (typeof uid === undefined || uid === "" || uid == null) {
        uid = -1;
    }
    // Prepare json string
    const process = `{
        "process": {
            "uid": "` + uid + `",
            "name": "` + document.getElementById('process-name-textarea').value + ` ",
            "responsible_person": "` + document.getElementById('process-responsible-person-textarea').value + `",
            "description": "` + document.getElementById('process-beschreibung-textarea').value + ` "
        },
            "target_metrics": ` + JSON.stringify(metrics) + ` 
        }`;

    if (document.getElementById('process-name-textarea').value === "") process_name_empty = true;

    // If a input has been performed, post changes to backend
    if (minmaxlist === "" && !process_name_empty && !text_replaced_flag) {
        saveProcess(process);
    } else {
        let alert_string = 'Changes could not be saved. ';
        if (process_name_empty) {
            alert_string += 'Please enter a process name';
        }
        // Prepare alert message strings depending on the error cause
        if (text_replaced_flag === true) {
            alert_string += '\nNon quantitative metrics have been automatically discarded.\n';
        }
        if (minmaxlist !== "") {
            alert_string += '\nThe following Metrics are not within their min/max values:\n';
            alert_string += minmaxlist + "\n";
        }
        Helper.hideLoadingScreen();
        window.alert(alert_string);
    }
}


/**
 * Saves data.
 * @param data
 */
function saveProcess(data) {
    helper.http_request("POST", "/process/create_edit", true, data, saveCallback);
}


/**
 * This function loads component names from json file
 *
 * @param processData
 */
function loadComponentNames(processData) {
    helper.http_request("GET", "/content/mapping_metrics_definition.json", true, "", function (metricsDefinition) {
        createComponentTable(processData, metricsDefinition);
        visualizeProcess(processData, metricsDefinition);
        helper.http_request("GET", "/component/overview", true, "", fillComponentDropdown);
    });
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

    // Table header
    let header = document.createElement('tr');
    header.className = "table-header";
    header.innerHTML = `
        <th class="col-1" name="Position"> Position</th>
        <th class="col-2" name="Component">Component</th>
        <th class="col-3" name="Category">Category</th>
        <th class="col-4"></th>
        <th class="col-5"></th>
        <th class="col-6"></th>
        <th class="col-7"></th>
        <th class="col-8"></th>
    `;
    document.getElementById('ComponentOverviewTable').appendChild(header);

    // Setting elements/components
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

        // Filling values
        component.innerHTML = `
            <td class="col-1" ></td>
            <td class="col-2" >` + componentData['name'] + `</td>
            <td class="col-3" >` + metricsDefinition['categories'][componentData['category']]['name'] + ` </td>
            <td class="col-4" ></td>
            <td class="col-5" ></td>
            <td class="col-6" ></td>
            <td class="col-7" ></td>
            <td class="col-8" ><i id="TrashIcon" class="fas fa-trash-alt" onclick="deleteComponent(this.parentElement.parentElement.id);"></i></td>
        `;

        // Sorting the components according to their weights
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
    Helper.showLoadingScreen();
    let componentUID = document.getElementById('addposition').value;
    if (componentUID.length === 32) {
        let weight = document.getElementById('ComponentOverviewTable').lastChild.id;
        // If there is no components in the table, the new component receives the weight = 1
        if (weight === '') {
            weight = 1;
        } else { // Else it receives the weight of the last component in the table + 1
            weight = parseFloat(weight) + 1;
        }

        let data = {
            "process_uid": uid,
            "component_uid": componentUID,
            "weight": weight
        };

        helper.http_request("POST", "/process/edit/createstep", true, JSON.stringify(data), init);
    } else {
        Helper.hideLoadingScreen();
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

    helper.http_request("POST", "/process/edit/editstep", true, JSON.stringify(data), init);
}

/**
 * This function deletes the selected component from the process
 *
 * @param {string} weight: The weight if the component to be deleted
 */
function deleteComponent(weight) {
    Helper.showLoadingScreen();
    let data = {
        "uid": uid,
        "weight": parseFloat(weight)
    }
    helper.http_request("POST", "/process/edit/deletestep", true, JSON.stringify(data), init);
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
    insertAfter(ev.target, element); // Component is inserted after the above component where the drop takes place

    let previousID;
    try {
        previousID = parseFloat(element.previousSibling.id); // Trying to get the weight of the previous element
        if (isNaN(previousID)) {                             // If there is no previous weight then default weight = own weight
            previousID = parseFloat(element.id);             // Which should be 1 by default as there are no weights in the table
        }
    } catch (e) {
        previousID = parseFloat(element.id);
    }
    let nextID;
    try {
        nextID = parseFloat(element.nextSibling.id); // Trying to get the ID of the below component where the drop takes place
    } catch (e) {
        nextID = parseFloat(element.previousSibling.id) + 1; // If there is no next component the next weight is the weight of the previous component + 1
    }
    let newWeight = parseFloat(previousID + (nextID - previousID) / 2);
    element.id = newWeight;

    Helper.showLoadingScreen();
    editComponent(oldWeight, newWeight); // Updating component table
}

/**
 * This function inserts an element after another specified one
 *
 * @param {HTMLElement} referenceNode: The element that the other element should be inserted after
 * @param {HTMLElement} newNode: The element to be inserted
 */
function insertAfter(referenceNode, newNode) {
    referenceNode.style.setProperty("border", "inherit", undefined);
    referenceNode.parentNode.insertBefore(newNode, referenceNode.nextSibling);
}

/**
 * This function handles the styles when an element gets dragged over another specified one
 *
 * @param {event} ev: The event associated with dragging and dropping elements
 */
function enter(ev) {
    ev.target.style.setProperty("border-bottom", "4px solid black", undefined);
}

/**
 * This function handles the styles when an element gets dragged over another specified one and then exits the scope
 *
 * @param {event} ev: The event associated with dragging and dropping elements
 */
function exit(ev) {
    ev.target.style.setProperty("border", "inherit", undefined);
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


    // Begin at index 1 because 0 contains table headers
    for (let i = 0; i < components.length; i++) {
        let currentComponent = components[i];
        let componentName = currentComponent['name'];
        let componentCategory = metricsDefinition['categories'][currentComponent['category']]['name'];

        rectangle = renderRectangle(componentName, componentCategory);

        innerHTML += `<div class="visualize">` + rectangle + `</div>`;
        if (i < components.length - 1) {
            innerHTML += `<div class="visualize" >` + arrowRight + `</div>`;
        }
    }

    div.innerHTML = innerHTML;

    document.getElementById('modelling-process').innerHTML = ""; // Reset div
    document.getElementById('modelling-process').appendChild(div); // Populate div

    horizontalScroll();

    //Setting row positions
    let componentRows = document.getElementById("ComponentOverviewTable").getElementsByTagName("tr");

    for (let i = 1; i < componentRows.length; i++) {
        let currentComponent = componentRows[i];
        let tds = currentComponent.getElementsByTagName("td");
        tds[0].innerHTML = i;
    }
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
            <div class="componentname">` + componentName + `</div>
            <div class="componentcategory">` + componentCategory + `</div>
        </div>`;
}

/**
 * Makes the components visualization box from visualizeProcess() horizontally scrollable with the mouse-wheel
 */
function horizontalScroll() {
    document.getElementById("visualizeprocess").addEventListener('wheel', function (e) {
        if (e.type !== 'wheel') {
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
    Helper.hideLoadingScreen();
    if (uid.length === 32) {
        init(response);
    } else {
        location.replace(location.href + '?uid=' + response['process']['uid']);
    }
}
