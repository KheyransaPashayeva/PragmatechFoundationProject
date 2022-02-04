# qeydiyyatdan kecmek ucun [1] yazin:
# -istifadeci adiniz:
# -istifadeci parolu:
# sisteme daxil olmaq ucun [2] yazin
# ana menyuya qayitmaq ucun [3] yazin
# sistemden cixmaq ucun [4] yazin
# sertler 
# -class ve objectlerden istifade olunaraq yazilmalidir
# -istifadeci daxil oldugu zaman daha onceden qeydiyyatdan kecib kecmediyini yoxlamalisiniz
# -parol daxil etdikden sonra parol sifrelenmis sekilde sisteme dusmelidir.Bunun ucun encript arasdirmasini ede bilersiz
# -ana menuye qayitmaq yuxaridaki menuyunun gorunmesi ,proqramdan cixmaq ise umumi proqramin dayanmasi menasina gelir
def ana_menu():
    return('''Qeydiyyatdan kecmek ucun [1] yazin:\nSisteme daxil olmaq ucun [2] yazin:\n
 Ana menuye qayitmaq ucun [3] yazin:\nSistemden cixmaq ucun [4] yazin:''')
print(ana_menu())
secim = int(input('Seciminizi daxil edin: '))
istifadeciler =[]
class Istifadeci:
    def __init__(self,ad,parol):
        self.ad=ad
        self.parol=parol
        istifadeciler.append(self.ad)   #liste elave etmek ucun
        
    def istifadeci_data_goster(self):
        print(f'{self.ad} siz artiq qeydiyyatdan kecmisiniz')

while True:
    if secim == 1:
        ad=input('-Istifadeci adiniz: ')
        parol=input('-Parolunuz: ')
        istifadeci = Istifadeci(ad, parol)  
        print('ugurla qeydiyyatdan kecdiniz!')
        secim = int(input('Seciminizi daxil edin: '))     
    if secim==2:
        ad=input('-Istifadeci adiniz: ')
        parol=input('-Parolunuz: ')
        istifadeci = Istifadeci(ad,parol)
        if istifadeci.ad in istifadeciler:
           istifadeci.istifadeci_data_goster()
        elif istifadeci not in istifadeciler:
           print('Qeydiyyatdan kecmemisiniz!')
        secim = int(input('Seciminizi daxil edin: '))
    if secim == 3:
        print(ana_menu()) 
        secim = int(input('Seciminizi daxil edin: '))

    if secim ==4:
       break

