# Task
# # Given an integer n and n space-separated integers as input, create a tuple t, of those n integers. Then compute and print the result of
# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
# Input Format
# The first line contains an integer, n, denoting the number of elements in the tuple.
# The second line contains space-separated integers describing the elements in tuple . 
# Source: https://www.hackerrank.com/challenges/python-tuples/problem

n = int(input())

# Map: map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
# Syntax: map(fun, iter)
# Parameters :
    # fun : It is a function to which map passes each element of given iterable.
    # iter : It is a iterable which is to be mapped. 

# a single value that denotes how many numbers should be passed to a list
n = int(input())
# print(f"Input from console {n}")

# Convert all inputs from console and type cast them into int.
integer_list = tuple(map(int, input().split()))

# print(integer_list[0])
print(hash(integer_list))


# This is a random string