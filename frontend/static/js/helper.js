
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
     * This function sends a post request to the backend
     *
     * @param {string} endpoint: The endpoint to be referred to
     * @param {string} data_json: The JSON Object to be passed to the backend
     * @param {function} callback: The function to be executed with the response
     */

    get_request(endpoint, data_json, callback) {
        const base_url = window.location.origin;
        let xhttp = new XMLHttpRequest();
        xhttp.open("GET", base_url + endpoint, true);
        xhttp.setRequestHeader("Content-Type", "application/json");

        // Handle response of HTTP-request
        xhttp.onreadystatechange = function () {
            if (this.readyState === XMLHttpRequest.DONE && (this.status >= 200 && this.status < 300)) {
                // Process response and show sum in output field
                let json = JSON.parse(this.responseText);
                callback(json);
            }
        }

        if(data_json!=="") {
            // Send HTTP-request
            xhttp.send(data_json);
        } else {
            xhttp.send();
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
            innerHTML += '<div data-hover="" data-delay="0" class="accordion-item w-dropdown">';
            innerHTML += '<div class="accordion-toggle w-dropdown-toggle" onclick="toggleSection(this)">';
            innerHTML += '<div class="accordion-icon w-icon-dropdown-toggle"></div>';
            innerHTML += ('<div class="features-label">' + feature['name'] + '</div>');
            innerHTML += '</div>';
            innerHTML += '<nav class="dropdown-list w-dropdown-list">';
            innerHTML += '<div class="features-columns w-row">';

            Object.keys(metrics).forEach(function (key) {
                let metric = metrics[key];
                innerHTML += '<div class="metric-entry-element w-clearfix">';
                innerHTML += ('<label for="availability-metric-7" class="entry-label">' + metric['name'] + '</label>');
                innerHTML += '<input type="text" maxLength="256" data-name="availability-metric-1" id="' + key + '"' +
                    ' name="availability-metric-1" class="metric-input textfield w-input">';
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
}