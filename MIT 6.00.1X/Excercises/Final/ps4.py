def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    # Your code here
    # Create a dictionary of all integers in list L
    list_dict = {}

    for i in L:
        if i in list_dict:
            list_dict[i] += 1
        else:
            list_dict[i] = 1
    
    temp_val = None
    
    # Loop through the list of values in dictionary
    for k, v in list_dict.items():

        # Check if v is odd
        if v % 2 != 0:
            
            # check if k is greater than temp_val
            if temp_val == None or k > temp_val:
                temp_val = k

    return temp_val


largest_odd_times([2,2,4,4]) #returns None
largest_odd_times([3,9,5,3,5,3]) #returns 9
largest_odd_times([3, 0, 5, 3, 5, 3]) #returns 3
largest_odd_times([6, 8, 6, 8, 6, 8, 6, 8, 6, 8]) #returns 8
largest_odd_times([2, 4, 5, 4, 5, 4, 2, 2]) #returns 4