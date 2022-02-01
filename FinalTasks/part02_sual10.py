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
 print('Qeydiyyatdan kecmek ucun [1] yazin:\nSisteme daxil olmaq ucun [2] yazin:\nAna menuye qayitmaq ucun [3] yazin:\nSistemden cixmaq ucun [4] yazin:')
ana_menu()
secim = int(input('Seciminizi daxil edin: '))
my_list =[]
def yoxla(a):
    if a ==1:
        ad=input('-Istifadeci adiniz: ')
        soyad=input('-Parolunuz: ')
        my_list.append(ad,soyad)
    if a==2:
        ...
    if a == 3:
        return ana_menu()