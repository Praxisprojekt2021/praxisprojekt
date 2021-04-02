/*TODO:
*       Call in loadProcesses an Backend-Endpoint senden statt an Mock-Datei --> Abhängigkeit Back-End
*       In add/edit/delete-functions entsprechende URL aufrufen --> Abhängigkeit Tom/Roman
*/

//Base url to distinguish between localhost and production environment
const base_url = window.location.href;
const dateOptions = { year: 'numeric', month: '2-digit', day: '2-digit' };

document.addEventListener("DOMContentLoaded", loadData(), false);

/**
 * Get component and process Data from Back-End and then populate the tables.
 */
function loadData() {
    loadComponents();
    loadProcesses();
}

/**
 * Get processes data from Back-End and then populate the processes table in FE.
 */
function loadProcesses() {
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
function loadComponents() {
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
            '<td>' + formatDate(object.created) + '</td>' +
            '<td>' + formatDate(object.edited) + '</td>' +
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
            '<td>' + formatDate(object.creation_timestamp) + '</td>' +
            '<td>' + formatDate(object.last_timestamp) + '</td>' +
            '<td>' + renderEditComponentButton(object.uid) + '</td>' +
            '<td>' + renderDeleteComponentButton(object.uid) + '</td>';
        table.appendChild(tr);
    });
}

/**
 * Renders HTML-Button to add a process.
 * @returns Add-Process-Button HTML-Element
 */
function renderAddProcessButton() {
    return `<div onclick="addProcess()">+</div>`;
}

/**
 * Renders HTML-Button to add a component.
 * @returns Add-Component-Button HTML-Element
 */
function renderAddComponentButton() {
    return `<div onclick="addComponent()">+</div>`;
}

/**
 * Renders HTML-Button to edit a process.
 * @returns Edit-Process-Button HTML-Element
 */
function renderEditProcessButton(uid) {
    return `<div onclick="editProcess('${uid}')"><img name="PenIcon" src="/images/penIcon.png" alt="pencil"></div>`;
}

/**
 * Renders HTML-Button to edit a component.
 * @returns Edit-Component-Button HTML-Element
 */
function renderEditComponentButton(uid) {
    return `<div onclick="editComponent('${uid}')"><img name="PenIcon"  src="/images/penIcon.png" alt="pencil"></div>`;
}

/**
 * Renders HTML-Button to delete a process.
 * @returns Delete-Process-Button HTML-Element
 */
function renderDeleteProcessButton(uid) {
    return `<div onclick="deleteProcess('${uid}')"><i name="TrashIcon" class="fas fa-trash-alt"></i></div>`;
}

/**
 * Renders HTML-Button to delete a component.
 * @returns Delete-Component-Button HTML-Element
 */
function renderDeleteComponentButton(uid) {
    return `<div onclick="deleteComponent('${uid}')"><i name="TrashIcon" class="fas fa-trash-alt"></i></div>`;
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
 * @param {String} uid
 */
function editProcess(uid) {
    // ... open edit process URL with param uid
}

/**
 * Routes to the URL where the user can edit the component with the given uid.
 * @param {String} uid
 */
function editComponent(uid) {
    // open edit component URL with param uid
    window.location.replace(base_url + "component?uid=" + uid);
}

/**
 * Routes to the URL where the user can delete the process with the given uid.
 * @param {String} uid
 */
function deleteProcess(uid) {
    // call delete-process endpoint
}

/**
 * Routes to the URL where the user can delete the component with the given uid.
 * @param {String} uid
 */
function deleteComponent(uid) {
    // Create new HTTP-Request to component-delete-endpoint
    let xhttp = new XMLHttpRequest();
    xhttp.open("POST", base_url + "component/delete", true);
    xhttp.setRequestHeader("Content-Type", "application/json");

    // Handle response of HTTP-request
    xhttp.onreadystatechange = function () {
        if (this.readyState === XMLHttpRequest.DONE && (this.status >= 200 && this.status < 300)) {
            // Process response and show data in tables
            location.reload();
        }
    }
    // add component uid as parameter
    let params = JSON.stringify({uid: uid});

    // Send HTTP-request
    xhttp.send(params);
}

/**
 * Formats date to a DD.MM.YYYY-String to show it in Front-End as German date format.
 * @param {String} date
 * @returns formatted Date
 */
function formatDate(date) {
    return new Date(date).toLocaleDateString("DE", dateOptions);
}

/**
 * Renders column to show status as red or green.
 * @param {String} viv_value 
 * @returns green or red td-cell (depending on viv-value)
 */
function renderStatusColumn(viv_value) {
    // if viv_value > 4, status is green, else status is red;
    // TODO: adapt to requirements (when it should be red or green)
    return viv_value > 4 ? '<td>🟢</td>' : '<td>🔴</td>';
}
