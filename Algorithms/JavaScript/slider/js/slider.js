let pos = 0;
let sliderWidth = 1200;
let sliderHeight = 300;
 let slideCount = 3;

let slides = document.querySelector('.slides');
let slider = document.querySelector('.slider');
let allSlides = document.querySelectorAll('.slide'); // .slide classina aid olan butun elementleri sec
// set slider width and height

slider.style.width = `${sliderWidth}px`;
slider.style.height = `${sliderHeight}px`;

// butun slide elementlerinin genisliyini javascript vasitesi ile teyin edirem
for (let slide of allSlides) {
    slide.style.width = `${sliderWidth/slideCount}px`
}

// slides divinin genisliyi dinamik olaraq teyin edirem

slides.style.width = `${sliderWidth/slideCount*allSlides.length}px`

// slider dots

let dots = document.querySelector('.slider-dots');

for (let i = 0; i < allSlides.length; i++) {
    dots.innerHTML += `<div class="dot" onclick="slideSelectedItem(${i})"></div>`

}


function left() {
    if (pos >= 0) {
        pos = 0
    } else {
        pos += sliderWidth / slideCount;
        slides.style.left = `${pos}px`;
    }
    

}

function right() {
    let dtindex = 0;
    let dt = document.querySelector('.dot');
    if (pos <= -((sliderWidth / slideCount) * (allSlides.length - slideCount))) {
        pos = -((sliderWidth / slideCount) * (allSlides.length - slideCount))
    } else {
        pos -= sliderWidth / slideCount;
        slides.style.left = `${pos}px`;
    }
    
  if(dtindex <= allSlides.length){
     dt.style.background = '#717171';
     dtindex ++;
}
}

function slideSelectedItem(i) {
    slides.style.left = `${-i*sliderWidth / slideCount}px`
}
