var slides = document.querySelectorAll("#slides > img");
var prev = document.getElementById("prev");
var next = document.getElementById("next");

var currents = 0;
showSlides(currents);
prev.onclick = prevSlide;
next.onclick = nextSlide;

function showSlides(n) {
    for (var i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slides[n].style.display = "block";
}
function prevSlide() {
    if (currents > 0) currents -= 1;
    else
      currents = slides.length - 1;
      showSlides(currents);
}
  function nextSlide() {
    if (currents < slides.length - 1) currents += 1;
    else
      currents = 0;
      showSlides(currents);  
}

var current = 0;
showSlide();

function showSlide() {
    var slide = document.querySelectorAll("#slides > img");
    for(let i = 0; i < slide.length; i++) {
        slide[i].style.display = "none";
    }
    current++;
    if(current > slide.length) current = 1;
    slide[current - 1].style.display = "block";
    setTimeout(showSlide, 3000);
}