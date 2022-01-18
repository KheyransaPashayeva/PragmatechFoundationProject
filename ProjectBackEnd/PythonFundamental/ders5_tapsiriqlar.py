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
#6) Write a function called returnDay. This function takes in one parameter ( a number from 1-7) and returns
#  the day of the week ( 1 is Sunday, 2 is Monday etc.). If the number is less than 1 or greater than 7,
#  the function should return None.
# typeday = int(input('eded daxil edin: '))
# day = ['Monday','Tuesday ','Wednesday ','Thursday  ','Friday  ','Saturday ','Sunday']
# my_list =[1,2,3,4,5,6,7]
# def returnDay():
#     for _ in my_list:
#         if typeday >=1 and typeday <=7:
#             day_index =my_list.index(typeday)
#             for j in range(len(day)):
#              if typeday in my_list:
#               return f'{typeday}-ci gun {day[day_index]}-dir'
#     return 'Daxil etdiyiniz eded 1den kicik 7den boyuk olmamalidir'
# print(returnDay())          
# ============================================================================================================
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
# ====================================================================================================================
# 8)dict={"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}
#  Verilen dictionary-e esasen asgidaki suallari cavablandirmaq ucun ekrana sualin cavabiniz yazdirin. 
# Bunun ucun userden input alin. Eger user “born”, “when” sozlerini daxil etse program texmin etsin ki user 
# ne sorushmaq isteyir. Meselen born ve when sozleri varsa cumlede user cox guman ki “When was Plato born?” 
# sualina cavab axtarir. Proqram o sozleri gorub sorushsun ki, “Maybe did you mean “When was Plato born?” “.
#  Bu suali sorushduqda yes ve no secimleri verin. Eger yes yazsa dictionarydeki datadan istifade ederek
#  Platonun doguldugu ili usere gosterin.Meselen country daxil etse proqram texmin etsin ki user platonun 
# doguldugu yeri axtarir ve siz de ele proqram yazin ki ona uygun cavab qaytarin. 
# Eger mentiqsiz soz daxil edilse not found verin ekrana.
# dict={"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}
# word = input('writing thing:')
# def sual_cavab(x):
#     for i in x:
#         if word =='born' or word =='when':
#             print('Maybe did you mean “When was Plato born?')
#             yes_no =input('answer:')
#             if yes_no =='yes':
#              answer= dict.get('born')
#              return answer
#             else:
#              break
#         if word == 'country' or word == 'where':
#               print('Maybe did you mean “Where was Plato born?')
#               yes_no =input('answer:')
#               if yes_no =='yes':
#                    answer= dict.get('country')
#                    return answer
#               else:
#                   break
#         if word == 'name' or word == 'who':
#               print('Maybe did you mean “What is his name?')
#               yes_no =input('answer:')
#               if yes_no =='yes':
#                    answer= dict.get('name')
#                    return answer
#               else:
#                   break
#         if word == 'teacher' or word == 'subject':
#               print('Maybe did you mean "Which is subject teacher?"')
#               yes_no =input('answer:')
#               if yes_no =='yes':
#                    answer= dict.get('teacher')
#                    return answer
#               else:
#                   break
#         if word == 'student':
#               print('Maybe did you mean "Who is student?"')
#               yes_no =input('answer:')
#               if yes_no =='yes':
#                    answer= dict.get('teacher')
#                    return answer
#               else:
#                   break  
#     if word not in dict:
#          return 'Not found'
# print(sual_cavab(dict))             
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
#     for _ in numbers:
#         if numbers[0] == numbers[-1]:
#            return True
#     return False
# print(is_first_last_true(numbers))
#11) Funksiya yazin parameter olaraq list,ve dict qebul etsin. Funksiya yoxlamalidi listin icindeki 
# reqemler dictioneryde yoxdusa onlari silmelidi ve sonda listi return etmelidi.
#  (mes : [27,22,34,44],{"tural": 27,"soltan": 22} funksiyaya gonderirsen o sene [27,22] qaytarir.
# my_parametr =[[27,8,22,34,11,44],{"tural":27,"soltan":22,"melik":31,"eli":11}]
# def kesisme(x):
#     my_list =[]
#     for i in x[0]:
#       for j in x[1].values():
#         if i == j: 
#           my_list.append(j)
#     print(my_list)
# kesisme(my_parametr)           