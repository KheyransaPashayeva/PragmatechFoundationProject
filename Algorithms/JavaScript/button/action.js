 let a=document.getElementsByTagName('li').length;
 //button1
 function backgroundchange(){
 document.querySelector('body').setAttribute('style','background-color: rgb(10, 167, 159);')
 }
  //button2
 function h1colorchange() {
    document.querySelector('h1').setAttribute('style','color: blue;')
 }
 //button3
 function textcolorchange() {
    document.querySelector('p').setAttribute('style','color: yellow;')
    document.querySelector('ul').setAttribute('style','color: yellow;')
}
//button4
function herfsayi(){
    let textp = document.querySelector('p').innerText;
    let textul = document.querySelector('ul').innerText;
    let text = textp + textul;
    let herfsayi=0;
  for(let Soz of text.split(" ")){
     herfsayi+=Soz.length;
  }

  document.querySelector(".card div").innerHTML =`Netice: herf sayi: ${herfsayi}`;

}
//button5
function wordnumber(){
    let textp = document.querySelector('p').innerText;
     let textul = document.querySelector('ul').innerText;
     let text = textp + textul;
    let word=text.split(" ").length;

document.querySelector(".card div").innerHTML =`Netice: Soz sayi ${word}`;
}
 //button6
 function wordsearch(){
     let textp = document.querySelector('p').innerText;
     let textul = document.querySelector('ul').innerText;
     let text = textp + textul;
    
     
     let str=text.indexOf('Proqramçi') ;
     
         if(str == -1){
            document.querySelector(".card div").innerHTML =`Netice: proqramçi sozu yoxdur`; 
         }
         else  document.querySelector(".card div").innerHTML =`Netice: proqramçi sozu var`;
     
 }
//button7
function imgproperty() {
    document.querySelector('img').setAttribute('style','border: 8px solid lightblue;')
}
//button8
  function imgchange(){ 
document.querySelector('img').setAttribute('src','image/2.jpg')
}
//button9

    function saitsamitsayi(){
    let textp = document.querySelector('p').innerText;
    let textul = document.querySelector('ul').innerText;
    let text = textp + textul;
    let saitler = ['a','e','i','o','ö','ə','ü','u']
    let saitsayi=0;
    let samitsayi=0;
    for (let herf of text){
        for(let sait of saitler){
            if(herf == sait){
                saitsayi++
            }
            else {
                 samitsayi++} 
        } 
    }
    document.querySelector(".card div").innerHTML =`Netice: Sait sayi: ${saitsayi}  Samit sayi: ${samitsayi}`;
}


//button10
function tekcutrengle() {
    for(let i = 0; i < a; i++){
    if(i % 2 == 0 ){
        document.getElementsByTagName('li')[i].style.color = 'red' ;
    }
    
    else {
        document.getElementsByTagName('li')[i].style.color = 'blue' ;
    }
    }
}
//button11
let firsttext;
let lasttext;
function firstlasttextchange(){
    for (let i = 0; i < a; i++){
       if(i == 0){
        firsttext = document.getElementsByTagName('li')[i].innerText;
       }  
        else   if (i == a-1) {
       lasttext = document.getElementsByTagName('li')[i].innerText;
       document.getElementsByTagName('li')[i].innerHTML = firsttext;
    }
     }
     document.getElementsByTagName('li')[0].innerHTML = lasttext;
    }
     
    
    //button12

function herfdeyis(){
cardP.innerText.replaceAll('e','ə')
CardUl.innerText.replaceAll('e','ə')
}
   
    




    



