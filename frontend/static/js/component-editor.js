// Base url to distinguish between localhost and production environment
const base_url = window.location.origin;
// instantiate object of helper class
const helper = new Helper();

/**
 * This function initializes the view and distinguishes between create and edit functionality
 */

function init() {
    const url_string = window.location.href;
    const url = new URL(url_string);
    const uid = url.searchParams.get('uid');

    getCategoryDropdown();
    getFeatures();

    // Check if view has received an uid as URL parameter to check whether to create a new component or edit an existing one
    if (uid && uid.length === 32) {
        // If so, load component data...
        helper.showLoadingScreen();
        console.log('Editing existing component');

        // Trigger function which gathers component data and processes it
        getComponent(uid);
    } else {
        // If not, prepare for new component input...
        console.log('Entering new component');
        setSections("default");
        // Enable component-category which is disabled by default
        document.getElementById('component-category').removeAttribute("disabled");
        // Set component uid to -1
        document.getElementById('component-uid').value = -1;
    }
}

/**
 *  Load Categories from file to get options for category dropdown.
 */

function getCategoryDropdown() {
    // Read JSON file
    fetch(base_url + '/content/mapping_metrics_definition.json')
        .then(response => response.json())
        .then(data => {
            let innerHTML = '';
            const categories = data['categories'];

            Object.keys(categories).forEach(function (key) {
                if (key !== 'default') {
                    innerHTML += '<option value="' + key + '">' + categories[key]['name'] + '</option>';
                }
            });

            // Append element to document
            document.getElementById('component-category').innerHTML += innerHTML;
        });
}

/**
 * Load Features from file to create metrics section.
 */

function getFeatures() {
    // Read JSON file
    fetch(base_url + '/content/mapping_metrics_definition.json')
        .then(response => response.json())
        .then(data => {
            const features = data['features'];

            helper.createMetricsSection(features);
            let div = document.createElement('div');
            div.className = 'control-area';
            div.innerHTML = '<a href="#" data-wait="Bitte warten..." id="save-button" class="create-button" onclick="createEditComponent(); helper.showLoadingScreen()">Speichern</a>';

            // Append element to document
            document.getElementById('metrics-input').appendChild(div);
        });
}

/**
 * This function fetches the component data from the backend
 *
 * @param {string} uid: The uid of the component to get data for
 */

function getComponent(uid) {
    const post_data = {
        "uid": uid
    }
    helper.post_request('/component/view', JSON.stringify(post_data), processComponentData);
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

        // Set uid and data fields
        document.getElementById('component-uid').value = json_data['uid'];
        document.getElementById('component-name').value = json_data['name'];
        document.getElementById('component-description-textarea').value = json_data['description'];

        // Set dropdown
        document.getElementById('component-category').value = json_data['category'];

        // Set all metrics
        let metrics = json_data['metrics'];
        Object.keys(metrics).forEach(function (key) {
            document.getElementById(key).value = metrics[key];
        });

        // Set sections according to the category
        setSections(json_data['category']);
    } else {
        // Request was not successful
        window.alert('Component could not be loaded');
    }
}

/**
 * This function enables and disables the component metrics for user input
 *
 * @param {string} selected_category: The component category selected in the dropdown
 */

function setSections(selected_category) {

    // Read JSON file
    fetch(base_url + '/content/mapping_metrics_definition.json')
        .then(response => response.json())
        .then(data => {
            const category = data['categories'][selected_category]['sections'];
            Object.keys(category).forEach(function (key) {
                const feature_child = document.getElementById(key).children[0].children[0];
                const metrics_child = document.getElementById(key).children[0].children[1];
                if (category[key] === 'true') {
                    feature_child.removeAttribute("disabled");
                } else {
                    feature_child.setAttribute("disabled", "true");
                    metrics_child.style.display = 'none';
                }
            });
        });
    helper.hideLoadingScreen();
}


/**
 * This function saves the data entered to the database by transmitting the data to the backend
 */

function createEditComponent() {

    let metric_elements = document.getElementsByClassName('metric-input');
    let metrics = {};
    let text_replaced_flag = false; // Helper variable that indicates, whether or not a non quantitative metric input has been found and discarded

    for (let i = 0; i < metric_elements.length; i++) {
        // TODO also check if values are within min and max values
        // Replace non quantitative metric inputs with an emtpy string to have them discarded
        if (metric_elements[i].value !== '' && isNaN(metric_elements[i].value)) {
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
    // Check if name field is filled
    if (document.getElementById('component-name').value == "") required_helper_flag = false;
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

        if (document.getElementById("component-category").value === "default") {
            required_helper_flag = false;
        }
    }

    // If a input have been performend, post changes to backend
    if (required_helper_flag) {
        helper.post_request('/component/create_edit', JSON.stringify(component), saveCallback);
    } else {
        let alert_string = 'Changes could not be saved. Please fill all metrics or name fields.';
        if (text_replaced_flag === true) {
            alert_string += '\nNon quantitative metrics have been automatically discarded.';
        }
        helper.hideLoadingScreen();
        window.alert(alert_string);
    }
}

/**
 * This function gets called if saving was successful and reloads the page.
 *
 */

function saveCallback(response) {
    helper.hideLoadingScreen();
    // Component has been created/edited successfully
    window.location.replace(base_url);
}
