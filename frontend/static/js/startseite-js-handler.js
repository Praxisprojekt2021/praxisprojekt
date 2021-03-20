/*TODO:
*       th/td-tags: style einbinden
*       renderAdd/Edit/Delete: Icons einfügen
*       Call an Backend-Endpoint senden statt an Mock-Datei
*       Datumswerte formatieren mit momentjs
*
*/

/**
 * Sends call to backend addition endpoint and shows sum in output-field.
 *
 */

//Base url to distinguish between localhost and production environment
const url = window.location.href;

document.addEventListener( "DOMContentLoaded", loadData(), false ); 

function loadData () {

    // Create new HTTP-Request to addition-endpoint
    let xhttp = new XMLHttpRequest();
    xhttp.open("GET", url + "content/mock-data.json", true);
    xhttp.setRequestHeader("Content-Type", "application/json");

    // Handle response of HTTP-request
    xhttp.onreadystatechange = function () {
        if (this.readyState === XMLHttpRequest.DONE && (this.status >= 200 && this.status < 300)) {
            // Process response and show sum in output field
            let json = JSON.parse(this.responseText);
            refreshComponentTable(json);
            refreshProcessTable(json);
    }
    }
    // Send HTTP-request
    xhttp.send();
}

function refreshComponentTable(json) {
    var table = document.getElementById('KomponentenTable');
            json.components.forEach(function(object) {
                var tr = document.createElement('tr');
                tr.innerHTML = '<td>' + object.name + '</td>' +
                '<td>' + object.category + '</td>' +
                '<td></td>' +
                '<td>' + object.creation_timestamp + '</td>' +
                '<td>' + object.last_timestamp + '</td>' +
                '<td>' + renderEditComponentButton(object.id) + '</td>' +
                '<td>' + renderDeleteComponentButton(object.id) + '</td>';
                table.appendChild(tr);
            });
            tr = document.createElement('tr');
            tr.innerHTML = '<td>' + renderAddComponentButton() + '</td>';
            table.appendChild(tr);
}

function refreshProcessTable(json) {
    var table = document.getElementById('ProzesseTable');
            json.processes.forEach(function(object) {
                var tr = document.createElement('tr');
                tr.innerHTML = '<td>' + object.process + '</td>' +
                '<td>' + object.components + '</td>' +
                '<td></td>' + 
                '<td>' + object.viv_value + '</td>' +
                '<td>' + object.created + '</td>' +
                '<td>' + object.edited + '</td>' +
                '<td>' + renderEditProcessButton(object.id) + '</td>' + 
                '<td>' + renderDeleteProcessButton(object.id) + '</td>';
                table.appendChild(tr);
            });
            tr = document.createElement('tr');
            tr.innerHTML = '<td>' + renderAddComponentButton() + '</td>';
            table.appendChild(tr);
}

function renderAddProcessButton() {
    return `<div onclick="addProcess()">+</div>`;
}

function renderAddComponentButton() {
    return `<div onclick="addComponent()">+</div>`;
}

function renderEditProcessButton(id) {
    return `<div onclick="editProcess(${id})">Edit</div>`;
}

function renderEditComponentButton(id) {
    return `<div onclick="editComponent(${id})">Edit</div>`;
}

function renderDeleteProcessButton(id) {
    return `<div onclick="deleteProcess(${id})">Delete</div>`;
}

function renderDeleteComponentButton(id) {
    return `<div onclick="deleteComponent(${id})">Delete</div>`;
}

function addProcess() {
    // ... open edit process URL without param
}

function addComponent() {
    // ... open edit component URL without param
}

function editProcess(id) {
    // ... open edit process URL with param id
}

function editComponent(id) {
    // ... open edit component URL with param id
}

function deleteProcess(id) {
    // ...
}

function deleteComponent(id) {
    // ...
}

