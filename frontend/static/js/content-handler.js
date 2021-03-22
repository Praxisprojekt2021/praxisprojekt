//Base url to distinguish between localhost and production environment
const base_url = window.location.origin;

/**
 * This function initializes the view and distinguishes between create and edit functionality
 */

function init() {
    const url_string = window.location.href;
    const url = new URL(url_string);
    const id = url.searchParams.get('id');

    // Check if view has received an id as URL parameter to check whether to create a new component or edit an existing one
    if (Number.isInteger(parseInt(id)) && parseInt(id) > 0) {
        // If so, load component data...
        console.log('Editing existing component');
        const component_data = getComponentData(parseInt(id));

        // TODO set data fields -> extra function
        // TODO ^^^set hidden id from parameter

        // Set Dropdown and disable it
        // TODO set Dropdown according to the actual category
        document.getElementById('component-category').setAttribute("disabled", "true");

        // TODO set Sections according to the category
    } else {
        // If not, prepare for new component input...
        console.log('Entering new component');
        setSections("default");
        // TODO set hidden id -1
    }
}

/**
 * This function fetches the component data from the backend
 *
 * @param {number} id: The id of the component to get data for
 */

function getComponentData(id) {
    const post_data = {
        "id": id
    }
    post_request('component/view', post_data, print_log);
}

function print_log() {console.log('print_log');}

/**
 * This function sends a post request to the backend
 *
 * @param {string} endpoint: The endpoint to be referred to
 * @param {string} data_json: The JSON Object to be passed to the backend
 * @param {function} callback: The function to be executed with the response
 */

function post_request(endpoint, data_json, callback) {
    const base_url = window.location.origin;
    let xhttp = new XMLHttpRequest();
    xhttp.open("POST", base_url + endpoint, true);
    xhttp.setRequestHeader("Content-Type", "application/json");

    // Handle response of HTTP-request
    xhttp.onreadystatechange = function () {
        if (this.readyState === XMLHttpRequest.DONE && (this.status >= 200 && this.status < 300)) {
            // Process response and show sum in output field
            let json = JSON.parse(this.responseText);
            callback(json);
        }
    }

    // Send HTTP-request
    xhttp.send(data_json);
}

/**
 * This function enables and disables the component metrics for user input
 *
 * @param {string} selected_category: The component category selected in the dropdown
 */

function setSections(selected_category) {

    // Read JSON file
    fetch(base_url + '/content/component-sections.json')
        .then(response => response.json())
        .then(data => {
            const category = data[selected_category];
            Object.keys(category).forEach(function (key) {
                const feature_child = document.getElementById(key).children[0].children[0];
                const metrics_child = document.getElementById(key).children[0].children[1];
                if (category[key] === 'true') {
                    feature_child.style.color = 'inherit';
                    feature_child.removeAttribute("disabled");
                } else {
                    feature_child.style.color = '#999999';
                    feature_child.setAttribute("disabled", "true");
                    metrics_child.style.display = 'none';
                }
            });
        });
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

function saveComponent() {
    const component = {
        "id": 1,
        "name": "SQL Datenbank",
        "category": "Datenbank",
        "description": "Datenbank zu xy mit ...",
        "creation_timestamp": "20200219...",
        "last_timestamp": "20200219...",
        "metrics": {
            "codelines": 20000,
            "admins": 10,
            "recovery_time": 5,
            // TODO only those metrics that match the component category?
        }
    }
    // TODO implement required handler
    // TODO create AJAX post request to backend

}
