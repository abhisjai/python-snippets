# #  Implement a function that meets the specifications below.
# def max_val(t): 
#     """ t, tuple or list
#         Each element of t is either an int, a tuple, or a list
#         No tuple or list is empty
#         Returns the maximum int in t or (recursively) in an element of t """ 
#     # Your code here
# For example,
#     max_val((5, (1,2), [[1],[2]])) returns 5.
#     max_val((5, (1,2), [[1],[9]])) returns 9.


def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 
    # Your code here
    temp_max = 0

    for i in t:

        if type(i) is int:
            # Compare if it is max in the list before returning
            if temp_max < i:
                temp_max = i
        else:
            # We have another list or tuple for which we need a max
            val = max_val(i)
            if temp_max < val:
                temp_max = val

    return temp_max

# print(max_val((5, (1,2), [[1],[2]])))
print(max_val((5, (15,2), [[32],[9]])))