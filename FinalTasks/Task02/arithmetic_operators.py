# Task
# The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.
# Input Format/ The first line contains the first integer, a. The second line contains the second integer, b.
# Constraints / a,b =[1,10^10]
a = int(input('1-ci ededi daxil edin:'))
b = int(input('2-ci ededi daxil edin:'))
if 1 <= a <= 10**10 and 1<= b <= 10**10:
    print('ededlerin cemi:',a+b)  #daha qisa olsun deye bu sekilde yazdim ayrica cem deyisenine menibsedib pritde onu da yaza bilerdim.
    print('ededlerin ferqi:',a-b)
    print('ededlerin hasili:',a*b)
