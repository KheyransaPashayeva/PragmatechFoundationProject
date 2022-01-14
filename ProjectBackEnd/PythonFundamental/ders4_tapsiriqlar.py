#1) Listin elementlerini toplayan alqoritm yazin. Sum funksiyasindan istifade etmeyin.
# my_list = [1,4,6,8,12,45,67,78]
# cem = 0
# for i in my_list :
#     cem += i
# print(cem)
# ========================================================================================
#2) Listin en boyuk elementini max funksiyasini istifade etmededen tapan alqoritm yazin.
# my_list = [1,4,6,8,12,45,67,78,90,1004,24]
# max = my_list[0]
# for i in my_list:
#     if max < i:
#         max = i
# print('En boyuk eded:' ,max)
# ===========================================================================================
#3) Listin en kicik elementini min funksiyasini istifade etmededen tapan alqoritm yazin.
# my_list = [9,4,6,8,12,45,67,78,90,1004,24]
# min = my_list[0]
# for i in my_list:
#     if min > i:
#         min = i
# print('En kicik eded:' ,min)
# =========================================================================================
#4) Write a Python program to count the number of strings where the string length is 2 or
#  more and the first and last character are same from a given list of strings.
#  Sample List : ['abc', 'xyz', 'aba', '1221'] Expected Result : 2
# my_list = ['abc', 'xyz', 'aba', '122','4gf5','2j2','fbhhbf','bfhfjjhb']
# say = 0
# for i in my_list:
#     if len(i) > 1 and i[0]==i[-1]:
#         say +=1
# print(say)
# ========================================================================================
#5) Write a Python program to check a list is empty or not.
# my_list = ['']
# if len(my_list) >0:
#     print('list bos deyil')
# else:
# print('list bosdur')
# ========================================================================================
# 6) my_text = “Write a Python program to count the number of strings where the string 
# length is 2 or more and the first and last character are same from a given list of strings.”
#  my_text stringindeki sozler elifba sirasi ile duzub string formatinda ekrana yazdirin.
# my_text = """Write a Python program to count the number of strings where the string 
#  length is 2 or more and the first and last character are same from a given list of strings."""
# my_list = my_text.split()
# for i in my_list:
#     print(i)

# ==========================================================================================
#7) Write a Python program to select the odd items of a list.
# my_list = [1,2,4,5,6,3,7,9,8]
# for i in my_list:
#     if i % 2 != 0:
#         print(i)