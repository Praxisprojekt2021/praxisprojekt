/**
 * Sends call to backend addition endpoint and shows sum in output-field.
 * 
 * 
 */

function calc() {
    // Get values from Input-Fields
    let input1 = document.getElementById("input-1").value;
    let input2 = document.getElementById("input-2").value;

    // Create new HTTP-Request to addition-endpoint
    let xhttp = new XMLHttpRequest();
    xhttp.open("POST", "https://praxisprojekt-2021.ew.r.appspot.com/addition", true);
    xhttp.setRequestHeader("Content-Type", "application/json");

    // Handle the Response from the HTTP-Request
    xhttp.onreadystatechange = function () {
        if (this.readyState === XMLHttpRequest.DONE && (this.status === 200 || this.status === 201)) {
            let response = xhttp.responseText;
            // Process the Response + Show sum in Output-Feld
            let json = JSON.parse(this.responseText);
            let sum = json.sum;
            document.getElementById("output").value = sum;

        }
    }
    // embed parameters for Request in a JSON-String
    let params = `{"number1": "${input - 1}", "number2": "${input - 2}"}`;

    // send the HTTP-Request
    xhttp.send(params);
}
