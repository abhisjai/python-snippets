# You are given a dictionary aDict that maps integer keys to integer values. Write a Python function that returns a list of keys in aDict that map to dictionary values that appear exactly once in aDict.

#     This function takes in a dictionary and returns a list.
#     Return the list of keys in increasing order.
#     If aDict does not contain any values appearing exactly once, return an empty list.
#     If aDict is empty, return an empty list.

# For example:
# If aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0} then your function should return [1, 3, 8]
# If aDict = {1: 1, 2: 1, 3: 1} then your function should return []

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    temp_val_list = []

    # Create a new dictionary of values as keys with keys as lists
    o = {}
    for k,v in aDict.items():
        if v in o:
            o[v].append(k)
        else:
            o[v] = [k]

    # Loop through this new dictionary to find keys with length of values = 1 and add it to returning list

    for k, v in o.items():
        if len(v) == 1:
            temp_val_list.append(v[0])
    
    temp_val_list.sort()
    return temp_val_list
    
    

uniqueValues({1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}) # returns [1, 3, 8]
uniqueValues({1: 1, 2: 1, 3: 1}) # returns []