# Task
# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following: 
# Hello firstname lastname! You just delved into python.

# firstname = input().rstrip()
# lastname = input().rstrip()

# print(f"Hello {firstname} {lastname}! You just delved into python")

# def print_full_name(a, b):
#     print(f"Hello {a} {b}! You just delved into python")

# if __name__ == '__main__':
#     first_name = input().rstrip()
#     last_name = input().rstrip()
#     print_full_name(first_name, last_name)

def print_full_name(a, b):
    # String formating tutorial: https://www.w3schools.com/python/ref_string_format.asp
    print("Hello {} {}!  You just delved into python".format(a, b))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)