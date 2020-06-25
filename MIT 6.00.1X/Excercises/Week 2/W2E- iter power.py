# Source: https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2020/courseware/
# Write an iterative function iterPower(base, exp) that calculates the exponential baseexp by simply using successive multiplication. 
# For example, iterPower(base, exp) should compute baseexp by multiplying base times itself exp times. Write such a function below.
# This function should take in two values - base can be a float or an integer; exp will be an integer ≥ 0. It should return one numerical value. 
# Your code must be iterative - use of the ** operator is not allowed. 

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''

    temp_base = 1
    # Your code here
    for i in range(1, exp+1):
        temp_base = temp_base * base
        print(i, temp_base)
    
    return temp_base


print(iterPower(7.9, 0))