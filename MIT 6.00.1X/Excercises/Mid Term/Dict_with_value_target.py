# Write a Python function that returns a list of keys in aDict with the value target. 
# The list of keys you return should be sorted in increasing order. The keys and values in aDict are both integers. 
# (If aDict does not contain the value target, you should return an empty list.)
# 
# This function takes in a dictionary and an integer and returns a list.
# def keysWithValue(aDict, target):
#     '''
#     aDict: a dictionary
#     target: an integer
#     '''
#     # Your code here  

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    # Your code here  
    # Return --sort-- list of --keys-- where value = target 
    temp_keys = [k for (k,v) in aDict.items() if v == target]
    temp_keys.sort()
    
    return temp_keys

print(keysWithValue({56:23,2:32,20:34,4:59,5:23,6:23,7:23},20))