// Base url to distinguish between localhost and production environment
const base_url = window.location.href;

// Instantiate object of Helper class
const helper = new Helper();

// Instantiate object of Modals class
const modals = new Modals();

/**
 * Get component and process Data from Back-End and then populate the tables.
 */
function init() {
    Helper.showLoadingScreen();
    getComponentList();
    getProcessList();
}

/**
 * Get processes data from Back-End and then populate the processes table in FE.
 */
function getProcessList() {
    helper.http_request("GET", "/process/overview", false, "", refreshProcessTable);
}

/**
 * Get components data from Back-End and then populate the processes table in FE.
 */
function getComponentList() {
    helper.http_request("GET", "/component/overview", true, "", loadMetricsDefinition);
}

/**
 * Populate Process Table.
 *
 * @param {JSON} json
 */
function refreshProcessTable(json) {
    const table = document.getElementById('processTable');
    json.processes.forEach(function (object) {
        const tr = document.createElement('tr');
        tr.innerHTML = '<td class="col-1">' + object.name + '</td>' +
            '<td class="col-2">' + object.components_count + '</td>' +
            '<td class="col-3">' + object.score + '</td>' +
            renderStatusColumn(object.score) +
            '<td class="col-5">' + helper.formatDate(object.creation_timestamp) + '</td>' +
            '<td class="col-6">' + helper.formatDate(object.last_timestamp) + '</td>' +
            '<td class="col-7">' + renderEditProcessButton(object.uid) + '</td>' +
            '<td class="col-8">' + renderDeleteProcessButton(object.uid) + '</td>';
        table.appendChild(tr);
    });
    Helper.hideLoadingScreen();
    modals.getProcessDate(json);
}

/**
 * Populate Component Table.
 *
 * @param {JSON} json object containing a list of components
 * @param metricsDefinition
 */
function refreshComponentTable(json, metricsDefinition) {
    let table = document.getElementById('componentTable');
    json.components.forEach(function (object) {
        let category = object.category;
        let tr = document.createElement('tr');
        tr.innerHTML = '<td class="col-1">' + object.name + '</td>' +
            '<td class="col-2">' + metricsDefinition.categories[category].name + '</td>' +
            '<td class="col-3">' + helper.formatDate(object.creation_timestamp) + '</td>' +
            '<td class="col-4">' + helper.formatDate(object.last_timestamp) + '</td>' +
            '<td class="col-5">' + renderEditComponentButton(object.uid) + '</td>' +
            '<td class="col-6">' + renderDeleteComponentButton(object.uid) + '</td>';
        table.appendChild(tr);
    });
    modals.getComponentDate(json);
}

/**
 * Renders HTML-Button to edit a process.
 *
 * @returns {String} Edit-Process-Button HTML-Element
 */
function renderEditProcessButton(uid) {
    return `<a href="process?uid=` + uid + `"><i id="PenIcon" class="fas fa-pencil-alt"></i></a>`;
}

/**
 * Renders HTML-Button to edit a component.
 *
 * @returns {String} Edit-Component-Button HTML-Element
 */
function renderEditComponentButton(uid) {
    return `<a href="component?uid=` + uid + `"><i id="PenIcon" class="fas fa-pencil-alt"></i></a>`;
}

/**
 * Renders HTML-Button to delete a process.
 *
 * @returns {String} Delete-Process-Button HTML-Element
 */
function renderDeleteProcessButton(uid) {
    return `<div onclick="deleteProcess('` + uid + `')"><i id="TrashIcon" class="fas fa-trash-alt"></i></div>`;
}

/**
 * Renders HTML-Button to delete a component.
 *
 * @returns {String} Delete-Component-Button HTML-Element
 */
function renderDeleteComponentButton(uid) {
    return `<div onclick="deleteComponent('` + uid + `')"><i id="TrashIcon" class="fas fa-trash-alt"></i></div>`;
}

/**
 * Routes to the URL where the user can delete the process with the given uid.
 *
 * @param {String} uid
 */
function deleteProcess(uid) {
    // call delete-process endpoint
    let params = JSON.stringify({uid: uid});
    helper.http_request("POST", "/process/delete", true, params, deleteCallback);
}

/**
 * Delete Component with given Id.
 *
 * @param {String} uid
 */
function deleteComponent(uid) {
    let params = JSON.stringify({uid: uid});
    helper.http_request("POST", "/component/delete", true, params, deleteCallback);
}


/**
 * Renders column to show status as red or green.
 *
 * @param {number} wholeProcessScore
 * @returns {String} green or red td-cell (depending on viv-value)
 */
function renderStatusColumn(wholeProcessScore) {
    // If score > 90, status is green, elseif score > 80, status is yellow, else status is red;
    let color = helper.getCircleColor(wholeProcessScore);
    return '<td class="col-4">' + helper.renderSmallCircle(null, color) + '</td>';
}

/**
 * Load Metrics Definition data from json file.
 *
 * @param componentData
 */
function loadMetricsDefinition(componentData) {
    helper.http_request("GET", "/content/mapping_metrics_definition.json", true, "", function (response_json) {
        refreshComponentTable(componentData, response_json);
    });
}

/**
 * Reloads page if deletion was successful.
 */
function deleteCallback(response) {
    window.location.reload();
}
