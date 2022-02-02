from re import I
from countries import olkeler
olke_seher = input("Istediyiniz olke ve ya seher adi daxil edin: ")
def FindCity(cityname):
  # seher adi daxil edildiyi zaman o seherin aid olduğu ölkəni göstərsin
  for cityname in olkeler.values():
    #   print(olkeler.values())
   pass

def FindCountry(countryname):
  # olke adi daxil edildiyi zaman o olkeye aid olan seherlerin adlarini ekranda gostersin
  pass

def CityCountMax():
  # ek cox sehere sahib olan olkeni gostersin
  pass

def CountAllCities():
  # butun seherlerin sayini ekranda gostersin
  seher_sayi = olkeler.values()
  print(len(seher_sayi))
  pass
FindCity(olke_seher)
CountAllCities()