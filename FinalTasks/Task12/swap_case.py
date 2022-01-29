# Complete the swap_case function in the editor below.
# swap_case has the following parameters:
# string s: the string to modify
# Returns
# string: the modified string
# Input Format
# A single line containing a string s.
# Constraints / len(s) =[1,1000]
def swap_case(s):
    if 1<= len(s) <= 1000:
        my_str = s.swapcase()
    return my_str

s = input('cumle daxil edin: ')
print(swap_case(s))