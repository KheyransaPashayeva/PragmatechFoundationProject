#1) Üç müxtəlif a, b, c ədədləri verilmişdir. Onlardan qiymətcə orta olanı tapın.
# n = input('3 muxtelif eded daxil edin:')
# s= n.split()
# i=0
# if i== 0 and s[i]:
#   if s[i+1] < s[i] < s[i+2] or  s[i+1] > s[i] > s[i+2]:
#     print(s[i])
#   if s[i] > s[i+1] and s[i] > s[i+2] and s[i+1] > s[i+2]:
#     print(s[i+1])
#   if s[i] > s[i+1] and s[i] > s[i+2] and s[i+1] < s[i+2]:
#     print(s[i+2])
#   if s[i]< s[i+1] and s[i] < s[i+2] and s[i+1] > s[i+2]:
#     print(s[i+2])
#   elif s[i]< s[i+1] and s[i] < s[i+2] and s[i+1] < s[i+2]:
#    print(s[i+1])
#=========================================================================================================================
#2) Proqramlaşdırma olimpiadasının ikinci turu bitdikdən sonra olimpiada iştirakçıları bu hadisəni qeyd etmək qərarına gəldilər. 
# Bu məqsədlə düzbucaqlı formada bir böyük tort sifarış verildi. Bu zaman iştirakçıların ətrafına toplaşdıqları masa dairəvi idi.
# Təbii ki, onlarda sual yarandı: Düzbucaqlı tort masadan qırağa çıxmamaq şərti ilə masaya yerləşəcəkdirmi?
# Tortun ölçülərini və masanın radiusunu bilərək, bu sualı cavablandırmalısınız. 
# import math
# w = int(input('duzbucaqlinin enin daxil edin: ')) 
# l = int(input('duzbucaqlinin uzunlugun daxil edin: ')) 
# r = int(input('cevrenin radiusunu daxil edin: '))
# d = 2*r
# print(d)
# top = w*w + l*l
# print(top)
# dioqnal = math.sqrt(top)
# print(dioqnal)
# if d > dioqnal:
#   print('yes')
# else:
#   print('no')
# =================================================================================================================================
#3) Heyvanxanada n qəfəs bir sırada düzülmüşdür. Heyvanxanada digər sakinlərlə yanaşı, iki əntər meymun - Slava və Yura da yaşayırdılar.
#  Slava və Yura həmişə yaxşı dost olmuşdular və qonşu qəfəslərdə əyləşirdilər. Lakin indi onlar küsülü idilər və bir-birini görmək istəmirdilər.
# Heyvanlara qulluq edən baxıcı də onları arzularına uyğun olaraq köçürmək istəyirdi, lakin problem yaranmışdı. Slava və Yura çox savadlı 
# meymunlar idilər (onların hər biri cəmi 8 sinif qurtarmışdı!). Onlar bilmək istəyirdilər ki, onların qəfəslərinin qonşu olmaması üçün neçə
#  köçürmə üsulu var və əlbəttə onların xanaları müxtəlif olmalıdır. Belə hesab etmək olar ki, heyvanxananın digər sakinləri hara lazımdırsa
#  köçürülməyə hazırdırlar, yəni bütün n hücrə əlyetərlidir.
# n = int(input('qefes sayini daxil edin: '))
# if 2 < n < 100:
#   m = 2*(n-2) + (n-2)*(n-3)
#   print('Slava və Yuranın qonşu olmaması üçün müxtəlif qəfəslərə köçürülmə üsullarının sayı verilir:',m)
#============================================================================================================================================
#4) m natural ədədi n ədədinin o zaman bərabər böləni adlanır ki, n-nin m-ə bölünməsindən alınan tam və qalıq bərabər
#  olsun. Verilmiş n natural ədədinə görə onun bərabər bölənlərinin sayını tapın.
# eded = int(input('eded daxil edin: '))
# def beraber_bolen(n):
#   i= 1
#   say =0
#   while i < n:
#     print(i)
#     q = n % i
#     t =int(n / i)
#     if q == t:
#       say +=1
#     i+=1
#   print('Sayi:',say)
# beraber_bolen(eded)
# =============================================================================================================
# 5) Verilmiş hesabi ifadədə toplama (+), çıxma (-) və vurma (*) əməllərinin ümumi sayını müəyyənləşdirin.
# Giriş verilənləri
# Yeganə sətirdə mötərizə və boşluq işarəsi olmayan hesabi ifadə verilir. İfadədə simvolların sayı 250-ni aşmır.
# Çıxış verilənləri
# Yeganə ədəd - göstərilən əməllərin sayı.
# ifade = input("ifade daxil edin: ")
# def func(s):
#     say =0
#     for i in range(1,len(s)):
#         if s[i] =='+' or s[i]== '*' or s[i]== '-':
#             say +=1
#     return say
# print(func(ifade))
