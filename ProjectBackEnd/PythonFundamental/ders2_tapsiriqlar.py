# 1.Bir mesajı dəyişəndə saxlayın və sonra mesajı çapa verin
# text = 'bu bir mesajdir))'
# print(text)
# 2.ad və soyad dəyişkənləri yaradın və onlara istədiyiniz kiçik hərflərdən ibarət dəyər verin.
#  Sonra tam_ad adlı dəyərdə ad və soyadın ilk hərflərini böyük şəkildə çapa verərək həmin şəxsə Salam verin.

# Nümunə: Salam, Arif Dadaşov! (Ekrana bu yazı çıxsın)
# ad = 'mehemmed'
# soyad = 'eliyev'
# tam_ad = f'Salam, {ad} {soyad}!'
# print(tam_ad.title())

# 3) sep parametrindən istifadə edərək 4 müxtəlif şəhər adını * işarəsi ilə ayırın
# print('Baki','Masalli','Quba','Salyan',sep='*')

# 4) Macarıstan” sözünü tərsinə çapa verin

# text = 'Macaristan'
# print(text[::-1])

#5) Bir sətir koddan istifadə edərək aşağıdakı yazını göründüyü kimi çapa verin. Languages: Python C JavaScript 
# print('Languages: Python C JavaScript',sep='\n')

#9) word = “istədiyiniz sözü yaza bilərsiz” məsələn word = ‘culture’ “Nineteet Eighty-Four does not present "art-as-culture" but "art-as-function"cüməsini bir dəyişkənə mənimsədin və həmin dəyişkəndə saxlayın və word-ə verdiyiniz sözün bu dəyişkəndə olub-olmamasını yoxlayın. Əgər söz varsa,
#  ekranda belə bir nəticə çıxarın; “Culture” sözü mətndə var. Əgər yoxdursa, “Not found” çapa verin.

# text = """İnsan ömrü boyu orta hesabla 35 ton su içir. Ondan 105 litri, 
# yəni təxminən 420 stəkanı duzlu və təmiz deyil"""
# word = 'su'
# yoxla = word in text
# if yoxla==True:
#     print('su sozu metnde var')
# if yoxla==False:
#     print('tapilmadi')

# 13) String data tipi yaradın və dəyərini 5.567-yə bərabər edin.
#  Sonra bu dəyişkənin dəyərin 10- luqlara qədər yuvarlaqlaşdırın.
# import math
# text ="5.567"
# eded = float(text)
# print(round(eded, 2))

# 15) 1 və 8 arasında random bir ədəd götürsün proqram,
# sonra isə o ədədin kvadrat kökünü tapın (random kitabxansini research edin).
# import random
# import math
# eded = random.randint(1,8)
# print('kvadrat koku: ',math.sqrt(eded))

# 16) 0 və 1 arasında olan təsadüfi bir ədədin 1 və 10 arasında olan təsadüfi bir ədələ hasilini tapın.
#  (random kitabxansini research edin)
# import random
# eded1 = random.random()
# eded2 = random.randint(1,10)
# print(eded1) //ededleri gormek istedim yoxlamaq ucun
# print(eded2)
# print(eded1*eded2)

# 17) x = “5.89” stringinin tam hissəsinin kubunu tapın.
# import math
# x = '5.89'
# y = float(x)
# b = int(y)
# print(math.pow(b, 3))

#18) y = “4.92” stringini integere cast edin.
# import math
# y = '4.92'
# x = float(y)
# z = int(x)
# print(z)