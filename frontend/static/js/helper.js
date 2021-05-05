class Helper {

    /**
     * Shows error message if request was not successful.
     *
     * @param {String} endpoint
     */
    static showError(endpoint) {
        // Saving the data was not successful
        if (endpoint.includes("delete")) {
            window.alert("Object could not be deleted.")
        } else {
            window.alert('Changes could not be saved.');
        }
    }

    /**
     * Shows success message if request was successful.
     *
     * @param {String} endpoint
     */
    static showSuccess(endpoint) {
        if (endpoint !== "/component/view") {
            // Saving the data was successful
            if (endpoint.includes("delete")) {
                // window.alert('Object has been deleted.');
            } else if (endpoint.includes("edit")) {
                // window.alert('Changes were saved.');
            }
        }
    }

    /**
     * This function sends a post request to the backend
     *
     * @param {string} requestType: The type of request which is either GET or POST
     * @param {string} endpoint: The endpoint to be referred to
     * @param {string} endpoint: The request to be either executed synchronously or asynchronously
     * @param {string} post_json: The JSON Object to be passed to the backend
     * @param {function} callbacks: The functions to be executed with the response
     */

    http_request(requestType, endpoint, async, post_json, ...callbacks) {

        const base_url = window.location.origin;
        let xhttp = new XMLHttpRequest();

        if (requestType === "GET") xhttp.open("GET", base_url + endpoint, async);
        if (requestType === "POST") xhttp.open("POST", base_url + endpoint, async);
        xhttp.setRequestHeader("Content-Type", "application/json");

        // Handle response of HTTP-request
        xhttp.onreadystatechange = function () {
            if (this.readyState === XMLHttpRequest.DONE && (this.status >= 200 && this.status < 300 || this.status === 500)) {
                // If status code is 500, an error message should be shown but the callback should be executed anyway.
                let json = JSON.parse(this.responseText);

                if (this.status === 500) {
                    Helper.showError(endpoint);
                } else {
                    if (json['success']) {
                        Helper.showSuccess(endpoint);
                    }
                }
                // Process response
                callbacks.forEach(callback => callback(json));
            } else if (this.readyState === XMLHttpRequest.DONE) {
                Helper.showError(endpoint);
            }
        }

        // Send HTTP-request
        if (requestType === "GET") xhttp.send();
        if (requestType === "POST") xhttp.send(post_json);
    }

    /**
     * Formats date to a DD.MM.YYYY-String to show it in Front-End as German date format.
     * @param {String} date
     * @returns formatted Date
     */
    formatDate(date) {
        const dateOptions = {year: 'numeric', month: '2-digit', day: '2-digit'};
        return new Date(date).toLocaleDateString("DE", dateOptions);
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

    /**
     * Get the color of the process given the calculated score
     *
     * @param {number, null} score
     * @returns {string}
     */

    getCircleColor(score) {
        let color;

        if (score === null) {
            color = "grey";
        } else if (score < 80) {
            color = "red";
        } else if (score < 90) {
            color = "yellow"
        } else if (score <= 100) {
            color = "green"
        } else {
            color = "grey";
        }
        return color;
    }

    /**
     * Render ball for each metric.
     *
     * @param {boolean, null} fulfillment
     * @param {string, boolean} color
     * @returns {string}
     */
    renderSmallCircle(fulfillment, color = false) {
        if (!color) {
            if (fulfillment === true) {
                color = "green";
            } else if (fulfillment === false) {
                color = "red";
            } else {
                color = "grey";
            }
        }

        return `<div class="small-circle" style="background-color: ${color}"></div>`;
    }

    /**
     * This functions toggles the accordion
     *
     * @param {HTMLElement} element: HTML accordion to be either opened oder closed
     */

    toggleSection(element) {
        const metric_child = element.parentElement.children[1];
        const metric_child_icon = element.parentElement.children[0].children[0];
        const isCollapsed = metric_child.getAttribute('data-collapsed') === 'true';
        metric_child.style.display = '';
        if (!(element.getAttribute("disabled") == "true")) {
            if (isCollapsed) {
                this.expandSection(metric_child);
                metric_child_icon.style.setProperty('transform', 'rotateX(180deg)');
                metric_child.setAttribute('data-collapsed', 'false');
            } else {
                this.collapseSection(metric_child);
                metric_child_icon.style.setProperty('transform', 'rotateX(0deg)');
            }
        } else {
            this.collapseSection(metric_child);
        }
    }

    /**
     * This functions collapses the accordion
     *
     * @param {HTMLElement} element: HTML accordion to be collapsed
     */

    collapseSection(element) {
        const sectionHeight = element.scrollHeight;

        const elementTransition = element.style.transition;
        element.style.transition = '';

        requestAnimationFrame(function () {
            element.style.height = sectionHeight + 'px';
            element.style.transition = elementTransition;
            element.style.margin = "0px 0px 0px 0px";
            requestAnimationFrame(function () {
                element.style.height = 0 + 'px';
            });
        });

        element.setAttribute('data-collapsed', 'true');
    }

    /**
     * This functions expands the accordion
     *
     * @param {HTMLElement} element: HTML accordion to be expanded
     */

    expandSection(element) {
        const sectionHeight = element.scrollHeight;
        element.style.height = sectionHeight + 'px';
        element.style.margin = "0px 0px 10px 0px";
        element.setAttribute('data-collapsed', 'false');
    }

    /**
     * This functions hides the loading animation
     */

    hideLoadingScreen() {
        let element = document.getElementById('loader-wrapper');
        element.setAttribute("class", "loader-wrapper-hidden");
    }

    /**
     * This functions shows the loading animation
     */

    showLoadingScreen() {
        let element = document.getElementById('loader-wrapper');
        element.setAttribute("class", "loader-wrapper");
    }

    /**
     * This function checks if the given target average is within the allowed min/max value
     *
     * @param {HTMLElement} element
     */

    targetAvgIsWithinMinMax(element) {
        let min = parseFloat(element.getAttribute("min")); // Getting min value for metric
        let max = parseFloat(element.getAttribute("max")); // Getting max value for metric
        let input = parseFloat(element.value); // Getting entered value for metric
        if (input < min || input > max) {
            return false;
        } else {
            return true;
        }
    }

    raise_alert(type, name_empty = false, text_replaced = false, minmaxlist = '', component_category_missing = false, emptyFieldList = ''){
        let alert_string = 'Changes could not be saved. ';
        if(type=='process'){

            if(name_empty) {
                alert_string += 'Please enter a process name';
            }
            // Prepare alert message strings depending on the error cause
            if (text_replaced) {
                alert_string += '\nNon quantitative metrics have been automatically discarded.\n';
            }
            if (minmaxlist !== "") {
                alert_string += '\nThe following Metrics are not within their min/max values:\n';
                alert_string += minmaxlist + "\n";
            }
            if (component_category_missing) {
                alert_string += 'Please select a metric.';
            }
        }   else if(type=='component'){
                if (component_category_missing) {
                    alert_string += 'Please select a category. \n';
                }
                if(name_empty) {
                    alert_string += 'Please enter a component name. \n';
                }
                if (emptyFieldList !== "") {
                    alert_string += 'Please fill all metrics fields. \n';
                    alert_string += '\nThe following Metrics are empty:\n';
                    alert_string += emptyFieldList + '\n';
                }
                if (text_replaced) {
                    alert_string += '\nNon quantitative metrics have been automatically discarded.\n';
                }
                if (minmaxlist !== "") {
                    alert_string += '\nThe following Metrics are not within their min/max values:\n';
                    alert_string += minmaxlist + "\n";
                }
            }

        this.hideLoadingScreen();
        window.alert(alert_string);

    }
}
