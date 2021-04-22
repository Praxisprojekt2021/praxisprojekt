var slideIndex = 1;
showSlides(slideIndex);

// Next/previous functionality
function plusSlides(n) {
    showSlides(slideIndex += n);
}

// Thumbnail image functionality
function currentSlide(n) {
    showSlides(slideIndex = n);
}
/**
 * i        - used for increments
 * slides   - individual slides/images and texts
 * dots     - dots used for orientation
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