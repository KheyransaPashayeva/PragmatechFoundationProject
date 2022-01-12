let second = document.querySelector('.second');
let minute = document.querySelector('.minute');
let hour = document.querySelector('.hour');
let deg = 6;
setInterval(() => {
    let now = new Date();
   let hh = now.getHours();
   let mm = now.getMinutes();
   let ss = now.getSeconds();
   let hrotation = 30*hh + mm/2;
   let mrotation = 6*mm;
   let srotation = 6*ss;

   hour.style.transform = `rotateZ(${hrotation}deg)`;
   minute.style.transform = `rotateZ(${mrotation}deg)`;
   second.style.transform = `rotateZ(${srotation}deg)`;
},1000);


setInterval(function() {
    let now = new Date()
    document.querySelector('p').innerHTML = now.getTime()
}, 1)

//doguldugum gunden indiye kimi kecen zaman
setInterval( function(){
const myd = new Date(1997,2,9,19,5);
let time = myd.getTime();
let now = new Date();
let fulltime = now.getTime();
let mydate = fulltime - time;

document.getElementById("lasttime").innerHTML = mydate;
},1)



const myd = new Date(1997,2,9,19,5,0,0);
let old = myd.getFullYear();
let time = myd.getTime();
let now = new Date();
let fulltime = now.getTime();
let nowyear = now.getFullYear();
let years = nowyear - old;
let month = myd.getMonth() + (12 * years);
let days = myd.getDay() + (years *365);
let hours = myd.getHours() + (days * 24);
let minutes = myd.getMinutes() + (hours * 60);
let seconds = myd.getSeconds() + (minutes * 60);
let salise = fulltime - time ;
document.getElementById("time").innerHTML = `Il: ${years}il ,Ay: ${month}ay,
                                             Gun: ${days}gun ,Saat: ${hours}saat ,Deqiqe: ${minutes}deqiqe,
                                              Saniye: ${seconds}saniye, Salise: ${salise}salise`;
