# Source: https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2020/courseware/0de4fecc5a9a4749923133fcf4de181f/38007cdb67c44b46b124cdbce33510b5/?activate_block_id=block-v1%3AMITx%2B6.00.1x%2B2T2020%2Btype%40sequential%2Bblock%4038007cdb67c44b46b124cdbce33510b5
# Write an iterative function, gcdIter(a, b), that implements this idea. 
# One easy way to do this is to begin with a test value equal to the smaller of the two input arguments, and iteratively reduce this test value by 1 until you either reach a case where the test divides both a and b without remainder, or you reach 1. 


def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    range_max = b if a > b else a

    for i in range(range_max, 0, -1):
        if a%i == 0 and b%i == 0:
            return i

print(gcdIter(225, 25))