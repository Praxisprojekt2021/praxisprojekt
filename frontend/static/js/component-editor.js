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
    if (uid) {
        // If so, load component data...
        Helper.showLoadingScreen();

        // Trigger function which gathers component data and processes it
        getComponent(uid);
    } else {
        // If not, prepare for new component input...
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
            getButtonType().then(button => {
                const features = data['features'];
                let buttonType = button;
                createMetricsSection(features);
                let div = document.createElement('div');
                div.className = 'control-area';
                div.innerHTML = `<button id="save-button" class="button" onclick="createEditComponent()" type="button">` + buttonType + `</button>`;

                // Append element to document
                document.getElementById('metrics-input').appendChild(div);
            });
            return features;
        });
}

/**
 * Get text for button types.
 */
function getButtonType() {
    // Read JSON file
    return fetch(base_url + '/content/en.json')
        .then(response => response.json())
        .then(data => {
            return data['en']['translation']['saveButton'];
        });
}

/**
 * Load features from file to provide component specific metrics information
 *
 * @param {string} category: The component category of the section
 */
function getMetricsInfo(category) {
    // Read JSON file
    let return_variable;
    helper.http_request("GET", "/content/mapping_metrics_definition.json", false, "", function (data) {
        return_variable = data['categories'][category]['sections'];
    });
    return return_variable
}

/**
 * This function fetches the component data from the backend
 *
 * @param {string} uid: The uid of the component to get data for
 */
function getComponent(uid) {
    const post_data = {"uid": uid};
    helper.http_request("POST", '/component/view', true, JSON.stringify(post_data), processComponentData);
}

/**
 * This function receives the component data and processes it
 *
 * @param {string} json_data: The component data
 */
function processComponentData(json_data) {

    // Check if the request has succeeded
    let component;
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
        //window.alert('Component could not be loaded');
        // Error will be shown in showError
        window.location.href = '/';
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
                    feature_child.setAttribute("onclick", "helper.toggleSection(this)");
                } else {
                    helper.collapseSection(metrics_child);
                    feature_child.setAttribute("disabled", "true");
                    feature_child.removeAttribute("onclick");
                    metrics_child.style.display = 'none';
                }
                metrics_child.children[0].childNodes.forEach(element => element.children[1].children[0].setAttribute("disabled", true));
            });
        });
    Helper.hideLoadingScreen();
}


/**
 * This function saves the data entered to the database by transmitting the data to the backend
 */
function createEditComponent() {

    let metric_elements = document.getElementsByClassName('metric-input');
    let metrics = {};
    let metrics_info;
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

    // Get information which categories apply for this metric
    metrics_info = getMetricsInfo(component['category']);

    if (document.getElementById('component-name').value === "") component_name_empty = true;

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

        if (metrics_info[toggles[i].id] === "false") {
            // Discard data from disabled metrics inputs
            for (let i = 0; i < metrics_child_input_fields.length; i++) {
                metrics_child.getElementsByTagName('input')[i].value = '';
                let current_metric_name = metrics_child.getElementsByTagName('input')[i].id;
                if (current_metric_name in component['metrics']) {
                    delete component['metrics'][current_metric_name];

                    // Easter Egg - please leave as is.
                    window.alert('You tried to sneak around, didn\'t you? Of course, we deleted your input for ' + current_metric_name);
                }
            }
        } else {
            // Check if enabled fields have been filled - all fields are required
            for (let i = 0; i < metrics_child_input_fields.length; i++) {
                let inputLabel = metrics_child.getElementsByTagName('label')[i];
                let inputElement = metrics_child.getElementsByTagName('input')[i];
                if (inputElement.value === '') {
                    emptyFieldList += '\n' + feature_child.getElementsByClassName('features-label')[0].innerHTML + ": " + inputLabel.innerHTML;
                    inputElement.style.setProperty("border-color", "red", undefined);
                    continue;
                }

                // Check if enabled fields maintain min/max value
                if (!Helper.targetAvgIsWithinMinMax(inputElement)) {
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
        Helper.showLoadingScreen();
        helper.http_request("POST", '/component/create_edit', true, JSON.stringify(component), saveCallback);
    } else {
        Helper.raise_alert('component', component_name_empty, text_replaced_flag, minmaxlist, !component_category_helper_flag, emptyFieldList);
    }
}

/**
 * This function gets called if saving was successful and reloads the page.
 *
 * @param response
 */
function saveCallback(response) {
    Helper.hideLoadingScreen();
    // Component has been created/edited successfully
    window.location.replace(base_url);
}

function createMetricsSection(features) {
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
            let binary = metric['binary'];
            innerHTML += '<div class="metric-entry-element">';
            innerHTML += ('<label for="metric-input" class="entry-label">' + metric['name'] + '</label>');
            if (!binary) {
                innerHTML += '<div><input disabled="true" type="text" maxLength="256" id="' + key + '"' +
                    ' name="metric-input" class="metric-input textfield"';
                if (metric['max_value'] === -1) {
                    innerHTML += ' min="' + metric['min_value'] + '"';
                } else {
                    innerHTML += ' max="' + metric['max_value'] + '" min="' + metric['min_value'] + '"';
                }
                innerHTML += ' ></div>';
            } else {
                innerHTML += '<div><select id="' + key + '" class="metric-input category-dropdown">' +
                    '<option value="0">No</option><option value="1">Yes</option></select></div>';
            }
            innerHTML += '<div class="icon-popup-fix info-text-popup" tooltip-data="' +
                metric['description_component'] + '\ni.e. ' + metric['example_component'] + '">' +
                '<img src="images/info.png" loading="lazy" width="35" alt="" class="info-icon"></div>';
            innerHTML += '</div>';
        });

        innerHTML += '</div>';
        innerHTML += '</nav>';
        innerHTML += '</div>';
        div.innerHTML = innerHTML;

        // Append element to document
        document.getElementById('metrics-input').appendChild(div);
    });
    let elementNames = ['metric-input'];
    Helper.checkCorrectInputs(elementNames);
}
