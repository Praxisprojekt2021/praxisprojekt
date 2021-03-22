/**
 * Sends call to backend addition endpoint and shows sum in output-field.
 *
 * @param {number} number1: first number to be added
 * @param {number} number2: second number to be added
 */

//Base url to distinguish between localhost and production environment
const base_url = window.location.origin;

function calc(number1, number2) {

    // Create new HTTP-Request to addition-endpoint
    let xhttp = new XMLHttpRequest();
    xhttp.open("POST", base_url + "addition", true);
    xhttp.setRequestHeader("Content-Type", "application/json");

    // Handle response of HTTP-request
    xhttp.onreadystatechange = function () {
        if (this.readyState === XMLHttpRequest.DONE && (this.status >= 200 && this.status < 300)) {
            // Process response and show sum in output field
            let json = JSON.parse(this.responseText);
            document.getElementById("output").value = json.sum;
        }
    }

    // Embed parameters for request in JSON object
    let params = `{"number1":${number1}, "number2":${number2}}`;

    // Send HTTP-request
    xhttp.send(params);
}
