class Helper {

    /**
     * This function sends a post request to the backend
     *
     * @param {string} endpoint: The endpoint to be referred to
     * @param {string} data_json: The JSON Object to be passed to the backend
     * @param {function} callback: The function to be executed with the response
     */

    post_request(endpoint, data_json, callback) {

        const base_url = window.location.origin;
        let xhttp = new XMLHttpRequest();
        xhttp.open("POST", base_url + endpoint, true);
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
                callback(json);
            } else if (this.readyState === XMLHttpRequest.DONE) {
                Helper.showError(endpoint);
            }
        }
        // Send HTTP-request
        xhttp.send(data_json);
    }

    /**
     * This function sends a post request to the backend
     *
     * @param {string} endpoint: The endpoint to be referred to
     * @param {function} callback: The function to be executed with the response
     */

    get_request(endpoint, callback) {
        const base_url = window.location.origin;
        let xhttp = new XMLHttpRequest();
        xhttp.open("GET", base_url + endpoint, true);
        xhttp.setRequestHeader("Content-Type", "application/json");

        // Handle response of HTTP-request
        xhttp.onreadystatechange = function () {
            if (this.readyState === XMLHttpRequest.DONE && (this.status >= 200 && this.status < 300 || this.status === 500)) {
                // Process response and show sum in output field
                let json = JSON.parse(this.responseText);

                if (this.status === 500) {
                    Helper.showError(endpoint);
                } else {
                    if (json['success']) {
                        Helper.showSuccess(endpoint);
                    }
                }

                callback(json);
            } else if (this.readyState === XMLHttpRequest.DONE) {
                Helper.showError(endpoint);
            }
        }
        xhttp.send();
   
    }

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
            innerHTML += '<div class="accordion-icon"></div>';
            innerHTML += ('<div class="features-label">' + feature['name'] + '</div>');
            innerHTML += '</div>';
            innerHTML += '<nav class="dropdown-list" style="height: 0px;" data-collapsed="true">';
            innerHTML += '<div class="features-columns">';

            Object.keys(metrics).forEach(function (key) {
                let metric = metrics[key];
                innerHTML += '<div class="metric-entry-element">';
                innerHTML += ('<label for="availability-metric" class="entry-label">' + metric['name'] + '</label>');
                innerHTML += '<input type="text" maxLength="256" data-name="availability-metric-1" id="' + key + '"' +
                    ' name="availability-metric" class="metric-input textfield">';
                innerHTML += `<img src="images/info.png" loading="lazy" width="35" alt="" class="info-icon">`;
                innerHTML += '</div>';
            });

            innerHTML += '</div>';
            innerHTML += '</nav>';
            innerHTML += '</div>';
            div.innerHTML = innerHTML;

            // Append element to document
            document.getElementById('metrics-input').appendChild(div);
        });
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
        } else if(score < 80) {
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
            if(fulfillment === true) {
                color = "green";
            } else if(fulfillment === false) {
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
        const isCollapsed = metric_child.getAttribute('data-collapsed') === 'true';
        metric_child.style.display = '';
        if(!(element.getAttribute("disabled") === "true")) {
            if(isCollapsed) {
                this.expandSection(metric_child);
                metric_child.setAttribute('data-collapsed', 'false');
            } else {
                this.collapseSection(metric_child);
            }
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

        requestAnimationFrame(function() {
            element.style.height = sectionHeight + 'px';
            element.style.transition = elementTransition;
            element.style.margin = "0px 0px 0px 0px";
            requestAnimationFrame(function() {
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
        element.setAttribute("class","loader-wrapper-hidden");
    }

    /**
     * This functions shows the loading animation
     */

    showLoadingScreen() {
        let element = document.getElementById('loader-wrapper');
        element.setAttribute("class","loader-wrapper");
    }
}