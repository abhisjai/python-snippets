# Assume that two variables, varA and varB, are assigned values, either numbers or strings.
# Write a piece of Python code that evaluates varA and varB, and then prints out one of the following messages:
#     "string involved" if either varA or varB are strings
#     "bigger" if varA is larger than varB
#     "equal" if varA is equal to varB
#     "smaller" if varA is smaller than varB
# Source: https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2020/courseware/fc8f42302c644118adfcfa720f9f403e/35f82f6c3ecb4e9e913dc279a9b73a9f/?child=first

temp_var = ""

try:
    #varA = int(input("Provide value for A: "))
    varA = int(varA)
except ValueError:
    temp_var = "string"
    
try:
    #varB = int(input("Provide value for B: "))
    varB = int(varB)
except ValueError:
    temp_var = "string"

if temp_var == "string":
    print("string involved")
elif (varA > varB):
    print("bigger")
elif(varA == varB):
    print("equal")
elif (varA < varB):
    print("smaller")