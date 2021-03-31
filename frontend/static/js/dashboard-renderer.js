/*TODO:
*       Call in loadProcesses an Backend-Endpoint senden statt an Mock-Datei --> Abhängigkeit Back-End
*       In add/edit/delete-functions entsprechende URL aufrufen --> Abhängigkeit Tom/Roman
*/

//Base url to distinguish between localhost and production environment
const base_url = window.location.href;

//instantiate object of Helper class
const helper = new Helper();

document.addEventListener("DOMContentLoaded", loadData(), false);

/**
 * Get component and process Data from Back-End and then populate the tables.
 */
function loadData() {
    getComponentList();
    getProcessList();
}

/**
 * Get processes data from Back-End and then populate the processes table in FE.
 */
function getProcessList() {
    // Create new HTTP-Request to processes-endpoint
    let xhttp = new XMLHttpRequest();
    xhttp.open("GET", base_url + "content/mock-data.json", true);
    xhttp.setRequestHeader("Content-Type", "application/json");

    // Handle response of HTTP-request
    xhttp.onreadystatechange = function () {
        if (this.readyState === XMLHttpRequest.DONE && (this.status >= 200 && this.status < 300)) {
            // Process response and show data in tables
            let json = JSON.parse(this.responseText);
            refreshProcessTable(json);
        }
    }
    // Send HTTP-request
    xhttp.send();
}

/**
 * Get components data from Back-End and then populate the processes table in FE.
 */
function getComponentList() {
    // Create new HTTP-Request to components-endpoint
    let xhttp = new XMLHttpRequest();
    xhttp.open("GET", base_url + "component/overview", true);
    xhttp.setRequestHeader("Content-Type", "application/json");

    // Handle response of HTTP-request
    xhttp.onreadystatechange = function () {
        if (this.readyState === XMLHttpRequest.DONE && (this.status >= 200 && this.status < 300)) {
            // Process response and show data in tables
            let json = JSON.parse(this.responseText);
            refreshComponentTable(json);
        }
    }
    // Send HTTP-request
    xhttp.send();
}

/**
 * Populate Process Table.
 * 
 * @param {JSON} json 
 */
function refreshProcessTable(json) {
    var table = document.getElementById('processTable');
    json.processes.forEach(function (object) {
        var tr = document.createElement('tr');
        tr.innerHTML = '<td>' + object.process + '</td>' +
            '<td>' + object.components + '</td>' +
            '<td>' + object.viv_value + '</td>' +
            renderStatusColumn(object.viv_value) +
            '<td>' + helper.formatDate(object.created) + '</td>' +
            '<td>' + helper.formatDate(object.edited) + '</td>' +
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
function refreshComponentTable(json) {
    var table = document.getElementById('componentTable');
    json.components.forEach(function (object) {
        let tr = document.createElement('tr');
        tr.innerHTML = '<td>' + object.name + '</td>' +
            '<td>' + object.category + '</td>' +    // TODO: erst mappen mit tatsächlicher Kategorie
            '<td></td>' +
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
    return `<div onclick="editProcess('${uid}')">🖊️</div>`;
}

/**
 * Renders HTML-Button to edit a component.
 * 
 * @returns {String} Edit-Component-Button HTML-Element
 */
function renderEditComponentButton(uid) {
    return `<div onclick="editComponent('${uid}')">🖊️</div>`;
}

/**
 * Renders HTML-Button to delete a process.
 * 
 * @returns {String} Delete-Process-Button HTML-Element
 */
function renderDeleteProcessButton(uid) {
    return `<div onclick="deleteProcess('${uid}')">🗑️</div>`;
}

/**
 * Renders HTML-Button to delete a component.
 * 
 * @returns {String} Delete-Component-Button HTML-Element
 */
function renderDeleteComponentButton(uid) {
    return `<div onclick="deleteComponent('${uid}')">🗑️</div>`;
}

/**
 * Routes to the URL where user can add a new process.
 */
function addProcess() {
    // ... open edit process URL without param
    window.location.replace(base_url + "/process");
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
    // ... open edit process URL with param uid
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
}

/**
 * Delete Component with given Id.
 * 
 * @param {String} uid
 */
function deleteComponent(uid) {
    let params = JSON.stringify({uid: uid});
    helper.post_request("component/delete", params, deleteCallback());
}


/**
 * Renders column to show status as red or green.
 * 
 * @param {String} viv_value 
 * @returns {String} green or red td-cell (depending on viv-value)
 */
function renderStatusColumn(viv_value) {
    // if viv_value > 4, status is green, else status is red;
    // TODO: adapt to requirements (when it should be red or green)
    return viv_value > 4 ? '<td>🟢</td>' : '<td>🔴</td>';
}

/**
 * Shows success/error message and reloads dashboard.
 */
function deleteCallback() {
// Check if component has been created/edited successfully
if (response['success']) {
    // Component has been created/edited successfully
    window.alert('Object has been deleted.');
    window.location.reload();
} else {
    // Component has not been created/edited successfully
    window.alert('Object could not be deleted.');
}
}