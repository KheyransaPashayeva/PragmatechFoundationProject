#1) Write a Python program to select the odd items of a list.
# my_list = [1,2,4,5,6,3,7,9,8]
# def tek_eded(x):
#  for i in x:
#     if i % 2 != 0:
#        print(i)
# tek_eded(my_list)
# ======================================================================
#2) Write a Python function to sum all the numbers in a list.
# my_list = [1,4,6,8,12,45,67,78]
# sample_list =[8, 2, 3, 0, 7]
# def cem(x):
#  cem = 0
#  for i in x:
#     cem += i
#  return(cem)
# print(cem(my_list))
# print(cem(sample_list)) //3) Sample List : (8, 2, 3, 0, 7) Expected Output : 20
# ===============================================================================
# 4) Write a Python function to multiply all the numbers in a list.
# my_list =[8, 2, 3, 4, 7]
# sample_list = [8, 2, 3, -1, 7]
# def multiply(x):
#  vur = 1
#  for i in x:
#     vur *= i
#  return(vur)
# print(multiply(my_list))
# print(multiply(sample_list)) // 5) Sample List : (8, 2, 3, -1, 7) Expected Output : -336
# ===========================================================================================================
#7) 'admin' adı da daxil olmaqla beş və ya daha çox istifadəçi adının siyahısını tərtib edin.
#  Təsəvvür edin ki, hər bir istifadəçi vebsayta daxil olduqdan sonra ona salam yazacaq kod yazırsınız.
#  Siyahıda dövr edin və hər bir istifadəçi üçün salamı çap edin: • İstifadəçi adı 'admin'dirsə, 
# salam admin kimi xüsusi salamı çap edin, status hesabatını görmək istərdinizmi? 
# • Əks halda, Salam Eric kimi ümumi salamı çap edin, yenidən daxil olduğunuz üçün təşəkkür edirik. 
# username = ['nermin','ali','murad','admin','lale','seyid']
# def salamla(x):
#  for i in x:
#      if i != 'admin':
#          print(f'Hello, {i} ,thank you for logging in again') 
#      else:
#         print(' Hello admin, would you like to see a status report?') 
# salamla(username)
# ===========================================================================================================
#9) len() funksiyasini ozunuz yazmaga calishin.
# my_list = [6,9,0,7,3,11,23,6,43,67]
# def listin_uzunluq(my_list):
#   for i in my_list:
#    say = my_list.index(i) +1
#   return say
# print(listin_uzunluq(my_list))
# ==============================================================================================================
#10) funksiya yazin ededlerden ibaret list qebul etsin ve eger listin birinci ve sonuncu elementleri beraberdise
#  return True qaytarsin. Mes: [1,2,3,1] bu halda True qaytaracag
# eded = input('Ededleri dagil edin: ')
# numbers = eded.split()
# def is_first_last_true(numbers):
#     for i in numbers:
#         if numbers[0] == numbers[-1]:
#            return True
#     return False
# print(is_first_last_true(numbers))
