//Base url to distinguish between localhost and production environment
const base_url = window.location.origin;

/**
 * This function initializes the view and distinguishes between create and edit functionality
 */

function init() {
    const url_string = window.location.href;
    const url = new URL(url_string);
    const uid = url.searchParams.get('uid');

    // Check if view has received an uid as URL parameter to check whether to create a new component or edit an existing one
    if (uid && uid.length === 32) {
        // If so, load component data...
        console.log('Editing existing component');

        // Trigger function which gathers component data and processes it
        getComponentData(uid);
    } else {
        // If not, prepare for new component input...
        console.log('Entering new component');
        setSections("default");

        // Set component id to -1
        document.getElementById('component-id').value = -1;
    }
}

/**
 * This function fetches the component data from the backend
 *
 * @param {string} id: The id of the component to get data for
 */

function getComponentData(uid) {
    const post_data = {
        "uid": uid
    }
    post_request('/component/view', JSON.stringify(post_data), processComponentData);
}

/**
 * This function receives the component data and processes it
 *
 * @param {string} json_data: The component data
 */

function processComponentData(json_data) {

    // Check if the request has succeeded
    if (json_data['success']) {
        // Component data has been received

        // Set id and data fields
        document.getElementById('component-id').value = json_data['uid'];
        document.getElementById('component-name').value = json_data['name'];
        document.getElementById('component-description-textarea').value = json_data['description'];

        // Set dropdown and disable it
        document.getElementById('component-category').value = json_data['category'];
        document.getElementById('component-category').setAttribute("disabled", "true");

        // TODO set all metrics

        // Set sections according to the category
        setSections(json_data['category']);
    }
}

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
        "uid": document.getElementById('component-id').value,
        "name": document.getElementById('component-name').value,
        "category": document.getElementById('component-category').value,
        "description": document.getElementById('component-description-textarea').value,
        "metrics": {
            "codelines": 20000,
            "admins": 10,
            "recovery_time": 5,
            // TODO only those metrics that match the component category?
        }
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
                    required_helper_flag = false;
                }
            }
        }
    }

    // If a input have been performend, post changes to backend
    if (required_helper_flag) {
        post_request('/component/create_edit', JSON.stringify(component), saveCallback);
    } else {
        window.alert('Changes could not be saved. Please fill all metrics fields.');
    }
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
