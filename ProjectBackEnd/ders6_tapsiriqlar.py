#1) Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both. If the salary is missing in the function
#  call then assign default value 9000 to salary
# expected result: showEmployee("Ben", 12000) showEmployee("Jessa") Name: Ben salary: 12000 Name: Jessa salary: 9000
# def show_employee(*x):
#     for i in x:
#         name = i
#         break
#     for j in x:
#        salary = j
#     if len(x) > 1:
#         return(f'Name: {name} salary: {salary}')
#     else:
#         salary = 9000
#         return(f'Name: {name} salary: {salary}')
# print(show_employee('Jessa') )   
# ===================================================================================================================
# 2)'test' adinda function yaradin, funksiyaya parametrleri key value shekline gonderin istenilen sayda, 
# funksiya gonderilen ededlerden cut olanlarin sayini tapsin expected result: test(a=4, b=1, c=2) result=2
# def test(**x):
#     say =0
#     for i in x.values():
#         if i%2==0:
#           say +=1
#     return f'result = {say}'
# print(test(x=4,b=5,e=9,d=2,o=8))
# =============================================================================================================
# 3) math.ceil funksiyasini ozunuz yazin
# def math_ceil(*x):
#     for i in x:
#        if i*10 % 10 > 5:
#            tam = int(i)+1
#            print(tam)
#        else:
#             tam = int(i)
#             print(tam)
# math_ceil(2.3,4.7,6.4,4.1)
# ==============================================================================================================
# 4) stringlerin index metodunu ozunuz yazin
# def my_string(*s):
#     for i in s:
#         my_index = len(i)
#         print(my_index)
# my_string('salam','hello' ,'wolrd', 'welcome')
# ==============================================================================================================
#5) Natural ədədin onluq yazılışında rəqəmləri eyni olan və bu ədədin onluq yazılışının mərkəzinə nəzərən simmetrik
#yerləşən cütlüklərin sayını həmin ədədin simmetriya dərəcəsi adlandıracağıq. Əgər ədəddə hər hansı rəqəm onluq
#yazılışda ortada yerləşirsə, onu da özü ilə bir cütlük kimi saymaq lazımdır. n ədədinin simmetriya dərəcəsini tapın.
# num= input('istediyiniz uzunluqda bir eded daxil edin: ')
# def simmetrik(n):
#     s = len(n)
#     b = int(s/2)
#     say =0
#     for i in range(1,b):
#        if n[0]==n[s-1]:
#            say+=1
#        if n[i]==n[s-i]:
#            say +=1
#     return say
# print(simmetrik(num))     
# ========================================================================================================================
#6) Robotun yerdəyişməsi hər bir əmri latın əlifbasının 3 böyük hərfinə - L, R, S hərflərinə uyğun proqramla müəyyənləşir.
#  L əmri icra edildikdə robot bir dama sola, R əmrində bir dama sağa hərəkət edir, S əmrində isə olduğu damada qalır.
# Giriş faylının yeganə sətri robot üçün yazılmış proqram - L, R, S simvollarından ibarət sətirdir. 
# Verilmiş bu proqram 10000 -dən çox olmayan əmrdən ibarətdir.
# Çıxış faylına bir ədədi - öz proqramını icra edərək robotun gəzdiyi müxtəlif damaların sayını göstərən ədədi vermək lazımdır.
# st =input('RSL den ibaret text daxil edin: ') 
# def myfunc(s):
#      say = 0
#      sayl =0
#      for i in s:
#         if i=='R':
#             say +=1
#         if i =='S':
#             say +=0
#         if i== 'L':
#             sayl += 1
        
#      print(say - sayl)
# myfunc(st)
