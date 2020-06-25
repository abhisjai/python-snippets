# Write a program that prints the longest substring of s in which the letters occur in alphabetical order

# s = 'abcdeelaymsbkrprvyuaieitpwpurp'
# s = 'azcbobobegghakl'
# s = 'abcbcd'
s = 'abcdefghzijklmnopqrstuvwxyz'

# string = ''

# tempIndex = 0
# prev = ''
# curr = ''

# index = 0
# while index < len(s):
#     curr = s[index]
#     if index != 0:
#         if curr < prev:
#             if len(s[tempIndex:index+1]) > len(string):
#                 string = s[tempIndex:index]
#             tempIndex=index
#         elif index == len(s)-1:
#             if len(s[tempIndex:index+1]) > len(string):
#                 string = s[tempIndex:index]
#     prev = curr
#     index += 1

# print('Longest substring in alphabetical order is: ' + string)

# Temp array to hold all alphabetical substrings
string_array = []

# Temp index to hold start index of current processed substring
start_index = 0
prev_char = ''

for curr_index, char in enumerate(s):
    # print("String Order: " + prev_char, char)
    # print("Various Indexes: " + str(start_index), str(curr_index))
    
    # If string is no longer in alphabetical order, append string array with slice till current index 
    # This condition will never allow last string to be added to the array
    if prev_char > char:
        # print("Not in alphabetical order")
        string_array.append(s[start_index:curr_index])
        start_index = curr_index
    # With elimination of end_index, we dont need this else check
    # else:
    #     print("In alphabetical order")
    #     end_index = curr_index
    
    # This is to ensure we also capture longest alphabetical string even if it is the last one
    if curr_index == len(s)-1:
        string_array.append(s[start_index:curr_index+1])

    prev_char = char

# print(string_array)


# Loop through the string_array to find the biggest string
longest_string = 0
longest_string_index = 0

for temp_index, i in enumerate(string_array):
    if longest_string < len(i):
        print("Longest string so far: " + i)
        longest_string = len(i)
        longest_string_index = temp_index

print('Longest substring in alphabetical order is: '+ string_array[longest_string_index])