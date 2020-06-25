# Source: https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2020/courseware/
# 


def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    return L

def timesFive(a):
    return a * 5

def absVal(a):
    return abs(a)

def plusOne(a):
    return a + 1

def sqrVal(a):
    return a ** 2


testList = [1, -4, 8, -9]

# print(applyToEach(testList, timesFive))
# print(applyToEach(testList, absVal))
# print(applyToEach(testList, sqrVal))
print(applyToEach(testList, plusOne))