let slideIndex = 1;
showSlide(slideIndex);

function openLightbox() {
  document.getElementById('test').style.display = 'block';
  // document.querySelector('.modal').style.display = 'block';
  document.getElementById('test').style.opacity = '1';
  document.getElementById('test').style.zIndex = '12';
  document.body.style.overflow = 'hidden'
}

function closeLightbox() {
  document.getElementById('test').style.display = 'none';
  document.body.style.overflow = 'scroll'
}

function changeSlide(n) {
	showSlide(slideIndex += n);
}

function toSlide(n) {
	showSlide(slideIndex = n);
}

function showSlide(n) {

  let slides = document.querySelectorAll('.slide');
  let modalPreviews = document.getElementsByClassName('modal-preview');

  if (n > slides.length) {
    slideIndex = 1;	
  }
  
  if (n < 1) {
  	slideIndex = slides.length;
  }

  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (let i = 0; i < modalPreviews.length; i++) {
    modalPreviews[i].className = modalPreviews[i].className.replace(' active', '');
  }
  
    slides[slideIndex -1].style.display ='block';
    console.log( slides[slideIndex -1])
    modalPreviews[slideIndex - 1].className += ' active';
}