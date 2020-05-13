# Task
# Let's learn about list comprehensions! 
# You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n. 
# You have to print a list of all possible coordinates given by on a 3D grid where the sum of x+y+z is not equal to n.
# Source: https://www.hackerrank.com/challenges/list-comprehensions/problem

x = int(input())
y = int(input())
z = int(input())
n = int(input())

# Code without list comprehension
# l = []

# for i in range(x +1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if (i + j + k != n):
#                 l.append([i,j,k])

# print(l)

# Code with list comprehension

print([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])