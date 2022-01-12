// let pos = 0;
// let sliderWidth = 1800;
// let sliderHeight = 450;
// let slideCount = 3;

// let slides = document.querySelector('.slides');
// let slider = document.querySelector('.slider');
 let allSlides = document.querySelectorAll('.mySlides'); // .slide classina aid olan butun elementleri sec
let slideIndex = 1;
showSlides(slideIndex);
let n=5;
// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}


function showSlides(n) {
    let dots = document.getElementsByClassName("dot");
for(let i=0; i <= allSlides.length; i++ ){
  if(i > allSlides.length){
      dots[i].style.display = "none"
  }
  else dots.innerHTML += `<span class ="dot" onclick="currentSlide(i)"></span>`
}
 let i;
let slides = document.getElementsByClassName("mySlides");
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