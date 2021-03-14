function calc() {
    let input1 = document.getElementById("input-1").value;
    let input2 = document.getElementById("input-2").value;
    
    let xhttp = new XMLHttpRequest();
        xhttp.open("POST", "https://praxisprojekt-2021.ew.r.appspot.com/addition", true);
        xhttp.setRequestHeader("Content-Type", "application/json");

        xhttp.onreadystatechange = function() {
    if (this.readyState === XMLHttpRequest.DONE && (this.status === 200 || this.status === 201)) {
        console.log(xhttp.responseText);
        let response = xhttp.responseText;
        // Prozessieren der Response
        let json = JSON.parse(this.responseText);
        let sum = json.sum;
        document.getElementById("output").value = sum;

    }
    let params = `{"number1": "${input-1}", "number2": "${input-2}"}`

    // let params = JSON.stringify(param);
        xhttp.send(params);

    }
}
