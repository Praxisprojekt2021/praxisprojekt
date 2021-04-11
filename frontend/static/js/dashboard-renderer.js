/*TODO:
*       Call in loadProcesses an Backend-Endpoint senden statt an Mock-Datei --> Abhängigkeit Back-End
*       In add/edit/delete-functions entsprechende URL aufrufen --> Abhängigkeit Tom/Roman
*/

//Base url to distinguish between localhost and production environment
const base_url = window.location.href;

//instantiate object of Helper class
const helper = new Helper();

document.addEventListener("DOMContentLoaded", init(), false);

/**
 * Get component and process Data from Back-End and then populate the tables.
 */
function init() {
    getComponentList();
    getProcessList();
}

/**
 * Get processes data from Back-End and then populate the processes table in FE.
 */
function getProcessList() {
    helper.get_request("/process/overview", refreshProcessTable);
}

/**
 * Get components data from Back-End and then populate the processes table in FE.
 */
function getComponentList() {
    helper.get_request("/component/overview", loadMetricsDefinition);
}

/**
 * Populate Process Table.
 *
 * @param {JSON} json
 */
function refreshProcessTable(json) {
    var table = document.getElementById('processTable');
    json.process.forEach(function (object) {
        var tr = document.createElement('tr');
        tr.innerHTML = '<td>' + object.name + '</td>' +
            '<td>' + object.components_count + '</td>' +
            '<td>' + object.score + '</td>' +
            renderStatusColumn(object.score) +
            '<td>' + helper.formatDate(object.creation_timestamp) + '</td>' +
            '<td>' + helper.formatDate(object.last_timestamp) + '</td>' +
            '<td>' + renderEditProcessButton(object.uid) + '</td>' +
            '<td>' + renderDeleteProcessButton(object.uid) + '</td>';
        table.appendChild(tr);
    });
}

/**
 * Populate Component Table.
 *
 * @param {JSON} json object containing a list of components
 */
function refreshComponentTable(json, metricsDefinition) {
    var table = document.getElementById('componentTable');
    json.components.forEach(function (object) {
        let category = object.category;
        let tr = document.createElement('tr');
        tr.innerHTML = '<td>' + object.name + '</td>' +
            '<td>' + metricsDefinition.categories[category].name + '</td>' +
            '<td>' + helper.formatDate(object.creation_timestamp) + '</td>' +
            '<td>' + helper.formatDate(object.last_timestamp) + '</td>' +
            '<td>' + renderEditComponentButton(object.uid) + '</td>' +
            '<td>' + renderDeleteComponentButton(object.uid) + '</td>';
        table.appendChild(tr);
    });
}

/**
 * Renders HTML-Button to edit a process.
 *
 * @returns {String} Edit-Process-Button HTML-Element
 */
function renderEditProcessButton(uid) {
    return `<div onclick="editProcess('${uid}')"><i id="PenIcon" class="fas fa-pencil-alt"></i></div>`;
}

/**
 * Renders HTML-Button to edit a component.
 *
 * @returns {String} Edit-Component-Button HTML-Element
 */
function renderEditComponentButton(uid) {
    return `<div onclick="editComponent('${uid}')"><i id="PenIcon" class="fas fa-pencil-alt"></i></div>`;
}

/**
 * Renders HTML-Button to delete a process.
 *
 * @returns {String} Delete-Process-Button HTML-Element
 */
function renderDeleteProcessButton(uid) {
    return `<div onclick="deleteProcess('${uid}')"><i id="TrashIcon" class="fas fa-trash-alt"></i></div>`;
}

/**
 * Renders HTML-Button to delete a component.
 *
 * @returns {String} Delete-Component-Button HTML-Element
 */
function renderDeleteComponentButton(uid) {
    return `<div onclick="deleteComponent('${uid}')"><i id="TrashIcon" class="fas fa-trash-alt"></i></div>`;
}

/**
 * Routes to the URL where user can add a new process
 */
function addProcess() {
    // open edit process URL without param
    window.location.replace(base_url + "process");
}

/**
 * Routes to the URL where user can add a new process.
 */
function addComponent() {
    // open edit component URL without param
    window.location.replace(base_url + "component");

}

/**
 * Routes to the URL where the user can edit the process with the given uid.
 *
 * @param {String} uid
 */
function editProcess(uid) {
    // open edit process URL with param uid
    window.location.replace(base_url + "process?uid=" + uid);
}

/**
 * Routes to the URL where the user can edit the component with the given uid.
 *
 * @param {String} uid
 */
function editComponent(uid) {
    // open edit component URL with param uid
    window.location.replace(base_url + "component?uid=" + uid);
}

/**
 * Routes to the URL where the user can delete the process with the given uid.
 *
 * @param {String} uid
 */
function deleteProcess(uid) {
    // call delete-process endpoint
    let params = JSON.stringify({uid: uid});
    helper.post_request("/process/delete", params, deleteCallback);
}

/**
 * Delete Component with given Id.
 *
 * @param {String} uid
 */
function deleteComponent(uid) {
    let params = JSON.stringify({uid: uid});
    helper.post_request("/component/delete", params, deleteCallback);
}


/**
 * Renders column to show status as red or green.
 *
 * @param {number} wholeProcessScore
 * @returns {String} green or red td-cell (depending on viv-value)
 */
function renderStatusColumn(wholeProcessScore) {
    // if score > 90, status is green, elseif score > 80, status is yellow, else status is red;
    // TODO: adapt to requirements (when it should be red or green)
    let color;

    if(wholeProcessScore < 80) {
        color = "RedCircle";
    } else if (wholeProcessScore < 90) {
        color = "YellowCircle"
    } else {
        color = "GreenCircle";
    }

    return '<td><i id="' + color + '" class="fas fa-circle"></i></td>';
}

/**
 * Load Metrics Definition data from json file.
 *
 * TODO: Could not be realized be helper.get_request because callback function needs to be called with two params. To be checked later if needed.
 * @param componentData
 */
function loadMetricsDefinition(componentData) {
    const base_url = window.location.origin;
    let xhttp = new XMLHttpRequest();
    xhttp.open("GET", base_url + "/content/mapping_metrics_definition.json", true);
    xhttp.setRequestHeader("Content-Type", "application/json");

    // Handle response of HTTP-request
    xhttp.onreadystatechange = function () {
        if (this.readyState === XMLHttpRequest.DONE && (this.status >= 200 && this.status < 300)) {
            // Process response and show sum in output field
            let metricsDefinition = JSON.parse(this.responseText);
            refreshComponentTable(componentData, metricsDefinition);
        }
    }
    xhttp.send();
}

/**
 * Shows success/error message and reloads dashboard.
 */
function deleteCallback() {
// Check if component has been deleted successfully
    if (response['success']) {
        // Component has been deleted successfully
        window.alert('Object has been deleted.');
        window.location.reload();
    } else {
        // Component has not been deleted successfully
        window.alert('Object could not be deleted.');
    }
}