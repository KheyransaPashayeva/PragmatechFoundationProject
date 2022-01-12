// ilk tapsiriq.ad və soyad tələb edin və bu daxil edilən məlumatlardan
//  istifadə edərək alert() metodu ilə ekrana "Memmed Hesenov sən xoş gəlmisən" formatında yazı çıxarın
// ad=prompt('Ad:')
// soyad=prompt('Soyad:')

// if(ad=='Memmed' && soyad=='Hesenov') {
//     alert("Memmed Hesenov sen  xos gelmisen!")
// } else{
//     alert('Daxil etdiyiniz melumatlar yanlisdir')
// }
// 2. tapsiriq.3+(2-true+false)/3&&true complex ifadəsinin nəticəsi nə olacaq 
//və bunun hansı sıralamalı ilə həllediləcəyi kod yazaraq izah edin


//console.log(2-true) //(2-1=1 ) 1 cavabi aliriq cunki true number deyeri 1 qebul edilir
// console.log(2-true+false) // 1 (2-1+0) cavabi aliriq cunki false number deyeri 0 goturur
// console.log(3+(2-true+false)) // cavab 4 moterize ici 1 almisdiq 3le topladi 4
// console.log(3+(2-true+fale)/3) //1.33333333 4u 3 e bolduk
// console.log(3+(2-true+fale)/3&&) //eror verir number ile ve isaresi ile bir emeliyyat yerine yetire bilmir
//console.log(3+(2-true+false)/3&&true)
//3cu tapsiriq.3=='3'==='3' bu kodun neticesini tapin ve niye bu netice elde edildiyini kod yazaraq izah edin .
// izahlari kodun daxilinde comment olaraq bildirmeyiniz kifayetdir
// console.log(3=='3') //true cunki iki beraber her iki terefi number edir beraberlesdirir
// console.log(3=='3'==='3') // false cunki birinci beraberlikde number tip deyisen oldu === ise her iki terefi hem deyer hem detip olaraq eynilesdiririr buna gore false verdi
// // 4.prompt vasitəsi ilə istifadəçidən username və password tələb olunmalıdır. bu daxil olunan məlumatlara əsasən
// aşağıdakı işlər görülməlidir.
//Əgər username və ya password bos buraxılıbsa ekrana alert vasitəsi ilə 'Deyerler bos ola bilmez' yazısı çıxsın
//Əgər username 'admin' ve password '123456'-dirsa ekrana alert vasitesi ile 'Tebrikler siz sisteme daxil oldugunuz'
//Daxil edilen deyerlerden her hansi biri duz deyilse ona uygun mesaj cixsin. Meselen username duz deyil

// username=prompt('Username:') 
// password=prompt('Password:')


//  if(username !='admin') {
//      alert("Username duz deyil") 
//  }

//   if(password !='123456'){
//      alert("Password duz deyil")
//  }
// if(username=="" && password=="") {
//     alert("Deyerler bos ola bilmez")
// }
//   else if (username=='admin' && password=='123456') {
//     alert('Tebrikler siz sisteme daxil oldunuz')
//  }
//5.while və ya for istifadə edərək aşağıdakı tapşırıqları yazın
//1-1000 arasındakı ədədləri ekrana çap edin
// 1) usul
//   for(let i=2;i<1000;i++){
//     console.log(i)
// }
// 2) usul
// let i=1;
// while (i<1000) {
//     console.log(i)
//     i++;
// }
//1-1000 arasındakı tək ədədləri ekrana çap edin
// 1) usul
//  for(let i=1;i<999;i++){
//     if(i%2==1){
//      console.log(i)
//     }
// }
// 2) usul
//  for(let i=1;i<=500;i++)
//  {     a=2*i-1;
//     console.log(a)
//  }

// 3) usul
// let i=1;
// let a=1;
// while(i<500){
// a=2*i-1;
// i++;
// console.log(a)
// }
//1-1000 3-ə bölünən ədədləri ekrana çap edin
// 1) usul
//  for(let i=1;i<1000;i++){
//     if(i%3==0){
//         console.log(i)
//     }
// }
// 2) usul
//  let i=1;
//  let a=1;
//  while (i<1000) {
//      a=i%3;
//      if (a==0) {
//          console.log(i)
//      }
//        i++; 
//  }
//1-1000 arasındakı ədədlərin cəmini hesablayıb ekrana çap edin
// 1) usul
//  let a=1;
// for(let i=1;i<1000;i++)
// {
//     a=a+i;
// }
// console.log(a)
 
let nums = [23,28,28,24,24,21,33,17,29,25,31,29]
for (let i = 0; i < nums.length; i++) {
    if(nums[i]>25)
    {
        console.log(nums[i])
    }
    
}
