let person = {
    ad: 'Kamil',
    soyad: 'Hemidov',
    yas: "25",
    vezife: "Seo",
} ;
let str='jnsdisabgcvauhk cbcawsjhcvbiqSNBSY';
let arr=[];
function checkType(a) {
if (typeof a == 'number') { //argument ədəddirsə neçə rəqəmli ədəd olduğunu return etsin
    console.log('ededdir')
    return String(a).length  
} // argument stringdirsə o stringin daxilindəki hərflərdən istifadə edərək
// təsadufi 5 söz istehsal edib 
    //, istehsal edilən sözləri array olaraq return etsin
else if (typeof a == 'string') {
    function makeid(length) {
        let result           = '';
        let charactersLength = a.length;
        for ( let i = 0; i < length; i++ ) {
          result += a.charAt(Math.floor(Math.random() * charactersLength));
        
       return result;
        }
     console.log(makeid());

        
}
    for(let i=0; i< a.length; i++){
        return result;
        arr.push(result)
    }
    console.log('metndir')
}else if (typeof a == 'object') {//argument obyektdirsə onun daxilində necə propertisinin olduğunu return etsin
    console.log('obyektdir')
    let prop = Object.keys(a);
    let say = Object.keys(a).length;
    console.log("propertinin sayi:" , say)
    console.log('Propertiler' , prop)
}
}
checkType(str)