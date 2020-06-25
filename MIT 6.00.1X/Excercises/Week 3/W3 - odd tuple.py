# Source: https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2020/courseware/

def oddTuples(aTup):
    '''
    aTup: a tuple
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    te = ()
    
    # Loop v1
    # for i in range(len(aTup)):
    #     if i % 2 == 0:
    #         te = te + aTup[i:i+1]

    # # Loop v2. This uses a step in range to skip if condition
    # for i in range(0, len(aTup), 2):
    #     # te = te + aTup[i:i+1] # v1
    #     # te += aTup[i:i+1]     # v2
    #     te += (aTup[i],)        # v3

    # Loop v3
    for i in range(0, len(aTup), 2): te += (aTup[i],)
    return te

testTuple = ('I', 'am', 'a', 'test', 'tuple')

print(oddTuples(testTuple))