from re import I
from countries import olkeler
olke_seher = input("Istediyiniz olke ve ya seher adi daxil edin: ")
def FindCity(cityname):
  # seher adi daxil edildiyi zaman o seherin aid olduğu ölkəni göstərsin
  Olkeler = list(olkeler.keys())
  seherler = list(olkeler.values())
  for i in range(len(Olkeler)):
    for j in range(len(seherler)):
      if cityname in seherler[j] and i==j:
       print(f'{cityname} seherinin aid oldugu olke:' ,Olkeler[i])
  pass

def FindCountry(countryname):
  # olke adi daxil edildiyi zaman o olkeye aid olan seherlerin adlarini ekranda gostersin
  if countryname in olkeler.keys():
   seherler = olkeler.get(countryname) #daxil edilen olkenin valuerin secdim
   print(f'{countryname} olkesinde olan seher adlari:' ,seherler)
  pass

def CityCountMax():
  # ek cox sehere sahib olan olkeni gostersin
 Olkeler = list(olkeler.keys())
 seherler = list(olkeler.values())
 seherlerin_sayi=[]
 max_seher=0
 for j in range(len(seherler)):
   seherlerin_sayi.append(len(seherler[j])) #ilk once her olkenin seher saylarini bir liste elave etdim
   max_seher=max(seherlerin_sayi)   #en boyuk ededi tapdim
   indeks = seherlerin_sayi.index(max_seher) # en boyuk ededin durdugu indeksi tapdim
 print('En cox sehere sahib olan olke:',Olkeler[indeks])  # hemin indeksli olkeler listindeki olkeni capa verdim
pass

def CountAllCities():
  # butun seherlerin sayini ekranda gostersin
  say=0
  seher_list=list(olkeler.values())
  for i in range(len(olkeler.values())):
    say += len(seher_list[i])       # her defe say uzerine seherlerin sayini geldim
  print('Olkeler siyahisin da olan butun seherlerin sayi: ',say)
  pass
FindCity(olke_seher)
FindCountry(olke_seher)
CityCountMax()
CountAllCities()
