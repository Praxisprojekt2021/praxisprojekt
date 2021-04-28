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
            div.innerHTML = '<a href="#" data-wait="Bitte warten..." id="save-button" class="create-button" onclick="createEditComponent()">Speichern</a>';

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
    helper.http_request("POST", '/component/view', true, JSON.stringify(post_data), processComponentData);
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
        component = json_data["component"]

        // Set uid and data fields
        document.getElementById('component-uid').value = component['uid'];
        document.getElementById('component-name').value = component['name'];
        document.getElementById('component-description-textarea').value = component['description'];

        // Set dropdown and disable it
        document.getElementById('component-category').value = component['category'];
        document.getElementById('component-category').setAttribute("disabled", "true");

        // Set all metrics
        let metrics = component['metrics'];
        Object.keys(metrics).forEach(function (key) {
            document.getElementById(key).value = metrics[key];
        });

        // Set sections according to the category
        setSections(component['category']);
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
    let component_name_empty = false; // Helper variable that indicates, whether or not the component name is given

    for (let i = 0; i < metric_elements.length; i++) {
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

    if(document.getElementById('component-name').value === "") component_name_empty = true;

    // Check if all field have been filled
    // Also, when changing between categories, discard inputs made for non-relevant metrics
    const toggles = document.getElementsByClassName('feature-section');
    let minmaxlist = ""; // List for Metrics that are not within min or max
    let emptyFieldList = ""; // List for Metric inputs that are empty
    let component_category_helper_flag = true; // Helper flag for "not selected" category
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
                let inputLabel = metrics_child.getElementsByTagName('label')[i];
                let inputElement = metrics_child.getElementsByTagName('input')[i];
                if (inputElement.value === '') {
                    emptyFieldList += '\n' + feature_child.getElementsByClassName('features-label')[0].innerHTML + ": " + inputLabel.innerHTML;
                    console.log(inputElement);
                    inputElement.style.setProperty("border-color", "red", undefined);
                    continue;
                }

                // Check if enabled fields maintain min/max value
                if (!helper.targetAvgIsWithinMinMax(inputElement)) {
                    minmaxlist += '\n' + feature_child.getElementsByClassName('features-label')[0].innerHTML + ": " + inputLabel.innerHTML;
                    inputElement.style.setProperty("border-color", "red", undefined);
                } else {
                    inputElement.style.removeProperty("border-color");
                }
            }
        }
    }

    if (document.getElementById("component-category").value === "default") {
        component_category_helper_flag = false;
    }

    // If an input has been performed, post changes to backend
    if (emptyFieldList === "" && minmaxlist === "" && component_category_helper_flag && !component_name_empty) {
        helper.showLoadingScreen();
        helper.http_request("POST", '/component/create_edit', true, JSON.stringify(component), saveCallback);
    } else {
        let alert_string = 'Changes could not be saved. ';
        // Prepare alert message strings depending on the error cause
        if (!component_category_helper_flag) {
            alert_string += 'Please select a category. \n';
        }
        if(component_name_empty) {
            alert_string += 'Please enter a component name. \n';
        }
        if (emptyFieldList !== "") {
            alert_string += 'Please fill all metrics fields. \n';
            alert_string += '\nThe following Metrics are empty:\n';
            alert_string += emptyFieldList + '\n';
        }
        if (text_replaced_flag === true) {
            alert_string += '\nNon quantitative metrics have been automatically discarded.\n';
        }
        if (minmaxlist !== "") {
            alert_string += '\nThe following Metrics are not within their min/max values:\n';
            alert_string += minmaxlist + "\n";
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

/**
 * Render metrics section.
 *
 * @param {json} features
 */
createMetricsSection(features) {
    Object.keys(features).forEach(function (key) {
        let feature = features[key];
        let metrics = feature['metrics'];

        let div = document.createElement('div');
        div.id = key;
        div.className = 'feature-section';

        let innerHTML = '';
        innerHTML += '<div data-hover="" data-delay="0" class="accordion-item">';
        innerHTML += '<div class="accordion-toggle" disabled="true" onclick="helper.toggleSection(this)">';
        innerHTML += '<div class="accordion-icon-dropdown-toggle">&#709</div>'
        innerHTML += ('<div class="features-label">' + feature['name'] + '</div>');
        innerHTML += '</div>';
        innerHTML += '<nav class="dropdown-list" data-collapsed="true">';
        innerHTML += '<div class="features-columns">';

        Object.keys(metrics).forEach(function (key) {
            let metric = metrics[key];
            innerHTML += '<div class="metric-entry-element">';
            innerHTML += ('<label for="availability-metric" class="entry-label">' + metric['name'] + '</label>');
            innerHTML += '<input type="text" maxLength="256" data-name="availability-metric-1" id="' + key + '"' +
                ' name="availability-metric" class="metric-input textfield"'
            if (metric['max_value'] === -1) {
                innerHTML += '" min="' + metric['min_value'] + '"'
            } else {
                innerHTML += ' max="' + metric['max_value'] + '" min="' + metric['min_value'] + '"'
            }
            innerHTML += ' >';
            innerHTML += '<img src="images/info.png" loading="lazy" width="35" alt="" title="' +
                metric['description_component'] + '\ni.e. ' + metric['example_component'] + '" class="info-icon">';
            innerHTML += '</div>';
        });

        innerHTML += '</div>';
        innerHTML += '</nav>';
        innerHTML += '</div>';
        div.innerHTML = innerHTML;

        // Append element to document
        document.getElementById('metrics-input').appendChild(div);
    });

    // Live check for correct inputs
    const inputs = document.getElementsByClassName('metric-input textfield');
    console.log(inputs);
    console.log(inputs[0]);
    for (let i = 0; i < inputs.length; i++) {
        inputs[i].addEventListener('blur', (event) => {
            if (!helper.targetAvgIsWithinMinMax(inputs[i]) || inputs[i].value === '') {
                inputs[i].style.setProperty("border-color", "red", undefined);
            } else {
                inputs[i].style.removeProperty("border-color");
            }
        });
    }
}
