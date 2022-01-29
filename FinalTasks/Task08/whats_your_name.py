# Prints

# string: 'Hello firstname lastname ! You just delved into python' where firstname and lastname are replaced
#  with first and last.
# Input Format
# The first line contains the first name, and the second line contains the last name.
# Constraints
# The length of the first and last names are each ≤ 10.
def print_full_name(first, last):
    if len(first) <=10 and len(last) <=10:
        print(f'Hello {first} {last}! You just delved into python.')

first_name = input('Adinizi daxil edin: ')
last_name = input('Soyadinizi daxil edin: ')
print_full_name(first_name, last_name)