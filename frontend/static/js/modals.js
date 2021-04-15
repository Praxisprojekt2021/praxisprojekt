class Modals {

    constructor() {
        this.oldprocesses = null;
        this.oldcomponents = null;
        
        // get current date
        this.threemonth = new Date()
        this.threemonth.setMonth(threemonth.getMonth()-3);

       
    }

    getProcessDate(json) {
        this.oldprocesses = "";
        json.process.forEach(function (object) {
            var editdate = new Date(object.last_timestamp)
            if(editdate<this.threemonth){
                this.oldprocesses += object.name +"\n"    
            }
        });
    }
    
    getComponentDate(json) {
        this.oldcomponents = "";
        json.components.forEach(function (object) {
            var editdate = new Date(object.last_timestamp)
            if(editdate<this.threemonth){
                this.oldcomponents += object.name +"\n"    
            } 
        });
    }

    isFilled() {
        if (this.oldcomponents !== null && this.oldprocesses !== null) showModal();
    }

    showModal() {
        // Modal dynamisch erstellen
        let innerHTML = `The following entries might be outdated:<br>`;
        if  (this.oldprocesses != "") innerHTML += this.oldprocesses + `<br>`;
        if  (this.oldcomponents != "") innerHTML += this.oldcomponents + `<br>`;
        innerHTML += `Please check metric inputs for validity and confirm the correct values by re-saving your inputs.`;

        document.getElementById("modal_text").innerHTML = innerHTML;
        modal.style.display = "block";
    }

}

document.write('<div id=modaldiv></div>');
document.getElementById('modaldiv').innerHTML =  `<div class="center">
<button id="modalbtn" class="button" data-i18n="remindertest"></button>
<div id="modal" class="modal"><div class="modal-content">
<span class="close">&times;</span>
<p id="modal_text"></p></div></div></div>`;

// Get the modal
var modal = document.getElementById("modal");

// Get the button that opens the modal
var modalbtn = document.getElementById("modalbtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// Open modal every 2 hours
setInterval(function(){
    modal.style.display = "block";},7200000);

// When the user clicks on the test button, open the modal
modalbtn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}