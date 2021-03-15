/**
 * Sends call to backend addition endpoint and shows sum in output-field.
 * 
 * 
 */

function calc(number1, number2) {
    console.log('Hi');
    // Create new HTTP-Request to addition-endpoint
    /*let xhttp = new XMLHttpRequest();
    xhttp.open("POST", "http://0.0.0.0:8080/addition", true);
    xhttp.setRequestHeader("Content-Type", "application/json");

    // Handle the Response from the HTTP-Request
    xhttp.onreadystatechange = function () {
        if (this.readyState === XMLHttpRequest.DONE && (this.status >= 200 && this.status < 300)) {
            // Process the Response + Show sum in Output-Feld
            let json = JSON.parse(this.responseText);
            let sum = json.sum;
            document.getElementById("output").value = sum;

        }
    }
    // embed parameters for Request in a JSON-String
    let params = `{"number1":${number1}, "number2":${number2}}`;

    // send the HTTP-Request
    xhttp.send(params);*/
}
