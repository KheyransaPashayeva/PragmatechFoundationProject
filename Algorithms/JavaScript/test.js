
// function maasHesabla(maas,vergi){
//     let result=maas-vergi;
//     return result
// }
// console.log(maasHesabla(860,129))

// function mesajVar(istifadeciAdi,mesaj){
//     if(mesaj==undefined){
//         console.log(`Salam hormetli ${istifadeciAdi},size gelen mesaj yoxdur.`)
//     }else{
//     console.log(`Salam hormetli ${istifadeciAdi}, size gelen mesaj var.Mesajin metni: ${mesaj}`)
//     }
// }
// mesajVar('Xeyransa')
// a=undefined;
// if(a){
//     console.log("a is true");
//     a+=20;
// }else{
//     console.log("a is false");
// }
// console.log(a)
// a='ju';
// if(!a){
//     console.log("a is true");
//     a+=20;
// }else{
//     console.log("a is false");
// }
// console.log(a)

// function getBiggestNumber(a,b){
//     // verilən iki ədəddən böyük olanını istehsal etsin
//     if (a>b){
//         console.log(a)
//     }else{
//         console.log(b)
//     }
// }
// getBiggestNumber(2,12)

// function printNumbersFrom1To100(){
//     let a=0;
//     // 1-100 arası ədədləri ekrana çap edin
//   while(a<100){
//     a+=1;
//     console.log(a)
//   }
    
// }
// printNumbersFrom1To100()

// let numbers=[2,4,6,8,9,2]
// let string=['ad','salam','test']
// let mix=[1,'isim','say',3,7]
// console.log(numbers.concat(string,mix))

// let text = "ABCDEFG"
// let myArr = Array.from(text);
// console.log(myArr)


// let fruits = ["Banana", "Orange", "Lemon", "Apple", "Mango"];
// let citrus = fruits.slice(1, 3);
// console.log(citrus)

// let resepts=[
//     {
//         mealName:'Dolma',
//         incridents:['et','duyu','sogan','edviyyat','goyerti']
//     },
//     {
//         mealName:'Qovurma',
//         incridents:['et','kartof','sogan','edviyyat','tomat','biber','pamidor']
//     }
// ]
// console.table(resepts)

// console.table(resepts[1].mealName)

customers=[
    {
        name:"John",
        age:30,
        city:"New York"
    },
    {
        name:"Albert",
        age:40,
        city:"Los Angeles"
    },
    {
        name:"Mary",
        age:50,
        city:"Miami"
    },
    {
        name:"Anna",
        age:30,
        city:"Washington"
    }
];
// let customersName=[];
// function showCustomersName(){
//     for(let i=0; i< customers.length; i++){
//         customersName.push(customers[i].name);
        
//     }
//     return customersName
// }
// console.log(showCustomersName())
// let customersAgeSum=0;
// function showCustomersAgeSum(){
//     for(let i=0; i< customers.length; i++){
//         customersAgeSum+=customers[i].age; 
//     }
//     return customersAgeSum
// }
// console.log(showCustomersAgeSum())

//A herfi ilə başlayan customer-lərin yaşlarını və şəhərlərini ekrana çap edin

// function showCustomersAgeAndCity(){
//     for(let i=0; i< customers.length; i++){
//         if(customers[i].name[0]=='A'){
//             console.log(customers[i].age,customers[i].city)
//         } 

//     } 
// }
// showCustomersAgeAndCity()

//Elə funksiya yazın ki o funksiyaya name,age,city parametrləri daxil edildiyi zaman 
//yeni customer yaradaraq customers siyahısına əlavə etsin.
// function addNewItemCustomer(name,age, city) {
//     customers.push(
//         {
//             name:name,
//             age:age,
//             city:city
//         })

//   }
// addNewItemCustomer('Xeyrnsa','26','Baki')
// console.table(customers)

class cvResume{
    constructor(_fullname,_birthdate,_address,_email,_phone,_education,_experience,_skills,_certificate,_language,_hobby){
        this.fullname=_fullname;
        this.birthdate=_birthdate;
        this.address=_address;
        this.email=_email;
        this.phone=_phone;
        this.education=_education;
        this.experience=_experience; 
        this.skills=_skills;
        this.certificate=_certificate;
        this.language=_language;
        this.hobby=_hobby;

    }

    getName(){
        return this.fullname;
    }
}

let newCv= new cvResume('Xeyransa Pasayeva','16.12.1996','Baki,Buzuovna qes.','xeyransa.pashayeva@gmail.com','055-722-85-15',
'BDU komp elmleri,Pragmatech','1-3 years uni','c++,html,css,python','','Azeri,Turk,English,Russian','read book,gym')
console.log(newCv)