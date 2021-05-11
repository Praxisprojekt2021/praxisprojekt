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
        } else if (endpoint.includes("/component/view")) {
            window.alert('Component could not be loaded.');
        } else if (endpoint.includes("/process/view")) {
            window.alert('Process could not be loaded.');
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
     * This functions hides the loading animation
     */
    static hideLoadingScreen() {
        let element = document.getElementById('loader-wrapper');
        element.setAttribute("class", "loader-wrapper-hidden");
    }

    /**
     * This functions shows the loading animation
     */
    static showLoadingScreen() {
        let element = document.getElementById('loader-wrapper');
        element.setAttribute("class", "loader-wrapper");
    }

    /**
     * This function sends a post request to the backend
     *
     * @param {string} requestType: The type of request which is either GET or POST
     * @param {string} endpoint: The endpoint to be referred to
     * @param async
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
     * Adds min max popups and initializes an eventlistener for every input field
     * @param {Array} elementNames
     */
    static checkCorrectInputs(elementNames) {

        // Live check for correct inputs
        elementNames.forEach(element => {
            const inputs = document.getElementsByName(element);
            for (let i = 0; i < inputs.length; i++) {
                Helper.addMinMaxPopup(inputs[i]);
                // Adding event listener for input check
                inputs[i].addEventListener('blur', (event) => {
                    if (!Helper.targetAvgIsWithinMinMax(inputs[i])) {
                        inputs[i].style.setProperty("border-color", "red", undefined);
                    } else {
                        inputs[i].style.removeProperty("border-color");
                    }
                });
            }
        });
    }

    /**
     * Adds a min max popup to the parent HTML element of the given HTML element
     *
     * @param {HTMLElement} element
     */
    static addMinMaxPopup(element) {
        let tooltipData;
        if (element.hasAttribute("min") && element.hasAttribute("max")) {
            tooltipData = "Min: " + element.getAttribute("min") + " Max: " + element.getAttribute("max");
        } else {
            if (element.hasAttribute("min")) tooltipData = "Min: " + element.getAttribute("min");
            if (element.hasAttribute("max")) tooltipData = "Max: " + element.getAttribute("max")
        }
        element.parentElement.classList.add("info-text-popup");
        element.parentElement.setAttribute("tooltip-data", tooltipData);
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
            color = '#d9d9d9'; //grey
        } else if (score < 80) {
            color = '#99201c'; //red
        } else if (score < 90) {
            color = '#fff293'; //yellow
        } else if (score <= 100) {
            color = '#f8ef42'; //green
        } else {
            color = '#d9d9d9'; //grey
        }
        return color;
    }

    /**
     * Get the background of the process given the calculated score
     *
     * @param {number, null} score
     * @returns {string}
     */
    getCircleBackground(score) {
        let background;

        if (score === null) {
            background = 'linear-gradient(315deg, #d9d9d9 0%, #f6f2f2 74%)'; //grey
        } else if (score < 80) {
            background = 'linear-gradient(316deg, #99201c 0%, #f56545 74%)'; //red
        } else if (score < 90) {
            background = 'linear-gradient(315deg, #fff293 0%, #ffe884 74%)'; //yellow
        } else if (score <= 100) {
            background = 'linear-gradient(315deg, #f8ef42 0%, #0fd64f 74%)'; //green
        } else {
            background = 'linear-gradient(315deg, #d9d9d9 0%, #f6f2f2 74%)'; //grey
        }
        return background;
    }

    /**
     * Render ball for each metric.
     *
     * @param {boolean, null} fulfillment
     * @param {string, boolean} color
     * @returns {string}
     */
    renderSmallCircle(fulfillment, color = false) {
        let background;
        if (!color) {
            if (fulfillment === true) {
                color = '#f8ef42'; //green
                background = 'linear-gradient(315deg, #f8ef42 0%, #0fd64f 74%)';
            } else if (fulfillment === false) {
                color = '#99201c'; //red
                background = 'linear-gradient(316deg, #99201c 0%, #f56545 74%)';
            } else {
                color = '#d9d9d9'; //grey
                background = 'linear-gradient(315deg, #d9d9d9 0%, #f6f2f2 74%)';
            }
        }

        return `<div class="small-circle" style="background-color: ` + color + `;background-image: `+ background + `"></div>`;
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
        if (!(element.getAttribute("disabled") === "true")) {
            if (isCollapsed) {
                this.expandSection(metric_child);
                metric_child_icon.style.setProperty('transform', 'rotateX(180deg)');
                metric_child.setAttribute('data-collapsed', 'false');
            } else {
                this.collapseSection(metric_child);
                metric_child_icon.style.setProperty('transform', 'rotateX(0deg)');
            }
        } else {
            if (!isCollapsed) {
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

        requestAnimationFrame(function () {
            element.style.height = sectionHeight + 'vmax';
            element.style.transition = elementTransition;
            element.style.margin = "0vmax 0vmax 0vmax 0vmax";
            requestAnimationFrame(function () {
                element.style.height = 0 + '0vmax';
            });
        });
        if (element.parentElement.parentElement.parentElement.id === "metrics-input-processes") {
            element.children[0].children[0].children[0].childNodes.forEach(element => element.childNodes.forEach(element => {
                if (element.childNodes.length > 0) {
                    if (element.children[0] !== undefined) {
                        element.children[0].setAttribute("disabled", true);
                    }
                }
            }));
        } else {
            element.children[0].childNodes.forEach(element => element.children[1].children[0].removeAttribute("disabled"));
        }
        element.setAttribute('data-collapsed', 'true');
    }

    /**
     * This functions expands the accordion
     *
     * @param {HTMLElement} element: HTML accordion to be expanded
     */
    expandSection(element) {
        const sectionHeight = element.scrollHeight;
        element.style.height = sectionHeight/(window.innerWidth/100) +'vmax';
        element.style.margin = "0vmax 0vmax 0.5210vmax 0vmax";
        element.setAttribute('data-collapsed', 'false');
        if (element.parentElement.parentElement.parentElement.id === "metrics-input-processes") {
            element.children[0].children[0].children[0].childNodes.forEach(element => element.childNodes.forEach(element => {
                if (element.childNodes.length > 0) {
                    if (element.children[0] !== undefined) {
                        element.children[0].removeAttribute("disabled");
                    }
                }
            }));
        } else {
            element.children[0].childNodes.forEach(element => element.children[1].children[0].removeAttribute("disabled"));
        }
    }

    /**
     * This function checks if the given target average is within the allowed min/max value
     *
     * @param {HTMLElement} element
     */
    static targetAvgIsWithinMinMax(element) {
        let min = parseFloat(element.getAttribute("min")); // Getting min value for metric
        let max = parseFloat(element.getAttribute("max")); // Getting max value for metric
        let input = parseFloat(element.value); // Getting entered value for metric
        return !(input < min || input > max);
    }
}
