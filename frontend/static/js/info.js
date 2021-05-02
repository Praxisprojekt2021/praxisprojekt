let slideIndex = 1;
showSlides(slideIndex);

/**
 * Iterates the slide number using showSlides
 *
 * @param n
 * **/
function plusSlides(n) {
    showSlides(slideIndex += n);
}

/**
 * States the current slide number using showSlides
 *
 * @param n
 * **/

function currentSlide(n) {
    showSlides(slideIndex = n);
}

/**
 *Displays the current slides and Dots for orientation
 *
 *@param {number} n received from the above functions to get the current slide
 * **/
function showSlides(n) {
    let i;
    const slides = document.getElementsByClassName("mySlides");
    const dots = document.getElementsByClassName("dot");
    if (n > slides.length) {
        slideIndex = 1
    }
    if (n < 1) {
        slideIndex = slides.length
    }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active";
}
