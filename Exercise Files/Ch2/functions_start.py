#
# Example file for working with functions
#

# define a basic function
def func1():
    print("I am a function")

# func1() 
# Braces means to execute a function
# value on console was any print command inside the function
# If there was any return value, it was not assigned to any variable

# print(func1()) 
# Execute a function and print its value
# While executing it also prints any Print statements to console
# It also prints return value = None as there was no return value from inside the function

# print(func1) 
# Function does not executes at all
# It only prints function defination which means functions are objects that can be passed around

# function that takes arguments
def func2 (argv1, argv2):
    print(argv1, " ", argv2)

# func2(10, 20)
# print(func2(10, 20)) 

# function that returns a value
def cube(x):
    return x*x*x

# cube(3) # This does not print any value. Return value is not assigned to any variable.
# print(cube(3))

# function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        #Multiple number by itself for 
        result = result * num
    return result

# print(power(2))
# # In case of missing parameters, function used default assigned value of x

# print(power(2, 3))
# # Even if x was assigned a value, you can override it when calling a function

# print(power(x=5, num=2))
# # order of arguments does not matter if you absolutely define them

#function with variable number of arguments
def multi_add(*argv):
    result = 0
    for x in argv:
        result = result + x
    return result

print(multi_add(5, 10, 25, 5))
print(multi_add(1, 2, 3, 4, 5))

# You can combine variable argument list with formal parameters
# Keep in mind, varibale argument list is last parameter