var slideIndex = 1;
showSlides(slideIndex);

/**
 * Iterates the slide number using showSlides
 *
 *@param {number} slideindex number of the current slide after iteration
 *
 * **/
function plusSlides(n) {
    showSlides(slideIndex += n);
}
/**
 * States the current slide number using showSlides
 *
 *@param {number} slideindex number of the current slide
 *
 * **/

function currentSlide(n) {
    showSlides(slideIndex = n);
}
/**
 *Displays the current slides and Dots for orientation
 *
 *@param {number} i used for incrementation
 *@param {number} n received from the above functions to get the current slide
 *@param {array} slides individual slides/images and texts
 *@param {array} dots dots used for orientation
 *
 * **/
function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    var dots = document.getElementsByClassName("dot");
    if (n > slides.length) {slideIndex = 1}
    if (n < 1) {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex-1].style.display = "block";
    dots[slideIndex-1].className += " active";
}
