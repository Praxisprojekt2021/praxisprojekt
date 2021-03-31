
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
     * Formats date to a DD.MM.YYYY-String to show it in Front-End as German date format.
     * @param {String} date
     * @returns formatted Date
     */
    formatDate(date) {
        const dateOptions = {year: 'numeric', month: '2-digit', day: '2-digit'};
        return new Date(date).toLocaleDateString("DE", dateOptions);
    }
}