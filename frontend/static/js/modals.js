/**
 * Class that is used inside of dashboard-renderer to get the json objects of processes and components.
 */
class Modals {

    constructor() {
        this.oldprocesses = null;
        this.oldcomponents = null;

        // Get current date to define the outdated threshold
        this.outdatedThreshold = new Date();


        // Set outdated threshold to one months
         this.outdatedThreshold.setMonth(this.outdatedThreshold.getMonth() - 1);
    }

    /**
     * Populate a list of processes that may need to be updated.
     *
     * @param {JSON} json object containing a list of processes
     */
    getProcessDate(json) {
        this.oldprocesses = '';
        Object.keys(json['processes']).forEach(function (key) {
            let process = json['processes'][key];
            let editedDate = new Date(process['last_timestamp']);
            if (editedDate < this.outdatedThreshold) {
                this.oldprocesses += '<a href="process?uid=' + process['uid'] + '">' + process['name'] + '</a><br>';
            }
        }, this);
        this.isFilled();
    }

    /**
     * Populate a list of components that may need to be updated.
     *
     * @param {JSON} json object containing a list of components
     */
    getComponentDate(json) {
        this.oldcomponents = '';
        Object.keys(json['components']).forEach(function (key) {
            let component = json['components'][key];
            let editedDate = new Date(component['last_timestamp']);
            if (editedDate < this.outdatedThreshold) {
                this.oldcomponents += '<a href="component?uid=' + component['uid'] + '">' + component['name'] + '</a><br>';
            }
        }, this);
        this.isFilled();
    }

    /**
     * Checks if the list of components and processes that may need to be updated has been filled.
     */
    isFilled() {
        if (this.oldcomponents !== null && this.oldprocesses !== null
            && (this.oldcomponents !== '' || this.oldprocesses !== '')) {
            this.showModal();
        }
    }

    /**
     * Shows the modal and fills it with the components and processes that may need to be updated.
     */
    showModal() {
        let innerHTML = `The following entries might be outdated:<br><br>`;
        if (this.oldprocesses !== '') innerHTML += this.oldprocesses + `<br>`;
        if (this.oldcomponents !== '') innerHTML += this.oldcomponents + `<br>`;
        innerHTML += `Please check metric inputs for validity and confirm the correct values by re-saving your inputs.`;
        document.getElementById("modal_text").innerHTML = innerHTML;
        modal.style.display = "block";
    }

}

// Create modal 
document.write('<div id=modal_div></div>');
document.getElementById('modal_div').innerHTML = `<div class="center">
<div id="modal" class="modal"><div class="modal-content">
<span class="close">&times;</span>
<p id="modal_text"></p></div></div></div>`;

// Get the modal
let modal = document.getElementById("modal");

// Get the <span> element that closes the modal
let span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
}
