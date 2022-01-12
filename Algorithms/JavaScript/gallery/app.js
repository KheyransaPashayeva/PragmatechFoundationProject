let b=0

function changeImage(a) { 
    b =a.querySelector('img').getAttribute("src");
    document.querySelector('.big-image img').setAttribute('src', b )
} 