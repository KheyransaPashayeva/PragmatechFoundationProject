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
   seherler = olkeler.get(countryname)
   print(f'{countryname} olkesinde olan seher adlari:' ,seherler)
  pass

def CityCountMax():
  # ek cox sehere sahib olan olkeni gostersin
 Olkeler = list(olkeler.keys())
 seherler = list(olkeler.values())
 max_seherili_olke=[]
 max_sayi=0
 for j in range(len(seherler)):
   max_seherili_olke.append(len(seherler[j]))
   max_sayi=max(max_seherili_olke)
   indeks = max_seherili_olke.index(max_sayi)
 print('En cox sehere sahib olan olke:',Olkeler[indeks])
pass

def CountAllCities():
  # butun seherlerin sayini ekranda gostersin
  say=0
  seher_list=list(olkeler.values())
  for i in range(len(olkeler.values())):
    say += len(seher_list[i])
  print('Olkeler siyahisin da olan butun seherlerin sayi: ',say)
  pass
FindCity(olke_seher)
FindCountry(olke_seher)
CityCountMax()
CountAllCities()