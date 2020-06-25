# Source:  https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2020/courseware/0de4fecc5a9a4749923133fcf4de181f/38007cdb67c44b46b124cdbce33510b5/?activate_block_id=block-v1%3AMITx%2B6.00.1x%2B2T2020%2Btype%40sequential%2Bblock%4038007cdb67c44b46b124cdbce33510b5
# We can use the idea of bisection search to determine if a character is in a string, so long as the string is sorted in alphabetical order.
# First, test the middle character of a string against the character you're looking for (the "test character"). 
#   If they are the same, we are done - we've found the character we're looking for!
# 
# If they're not the same, check if the test character is "smaller" than the middle character. 
#   If so, we need only consider the lower half of the string; otherwise, we only consider the upper half of the string. (Note that you can compare characters using Python's < function.)
# 
# Implement the function isIn(char, aStr) which implements the above idea recursively to test if char is in aStr. 
# char will be a single character and aStr will be a string that is in alphabetical order. The function should return a boolean value.
# As you design the function, think very carefully about what the base cases should be.

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    # Base Case: -ve test case in case you dont have a string to compare against.
    if len(aStr) == 0:
        # print("String length = 0")
        return False
    
    # Base Case: If you only have 1 character. Compare char with aStr and return True or False
    if len(aStr) == 1:
        # print ("String length = 1")
        
        # if aStr[0] == char:
        #     print("Char found")
        # else:
        #     print("Char not found")

        return aStr[0] == char

    temp_string_index = int(len(aStr) / 2)
    # print("Temp string index = ", temp_string_index)
   
    midChar = aStr[temp_string_index]
    # print("Temp Char: ", midChar)

    if midChar == char:
        # print("midChar == char")
        return True
    
    # If midChar is less than char, look for character in Upper half of the string.
    elif midChar < char:
        # print("looking for character in Upper half of the string")
        return isIn(char, aStr[temp_string_index+1:])
    
    # If midChar is greater than char, look for character in Lower half of the string.
    elif midChar > char:
        # print("looking for character in Lower half of the string")
        return isIn(char, aStr[:temp_string_index])

print(isIn("z", "bcdefghijk"))