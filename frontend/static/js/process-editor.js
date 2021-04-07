//Base url to distinguish between localhost and production environment
const base_url = window.location.origin;
// instantiate object of helper class
const helper = new Helper();

// document.addEventListener("DOMContentLoaded", init(), false);

function init() {

    this.renderWholeProcessScoreCircle(12);
}

function renderWholeProcessScoreCircle(wholeProcessScore) {
    if(wholeProcessScore < 75) {
        document.getElementById("whole-process-score").setAttribute("background-color", "red");
    } else {
        document.getElementById("whole-process-score").setAttribute("background-color", "green");
    }
    document.getElementById("whole-process-score").innerHTML = `${wholeProcessScore}%`;
}