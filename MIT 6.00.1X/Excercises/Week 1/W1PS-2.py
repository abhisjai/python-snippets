# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
# Number of times bob occurs is: 2
# Source: https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2020/courseware/fc8f42302c644118adfcfa720f9f403e/ca19e125470846f2a36ad1225410e39a/?activate_block_id=block-v1%3AMITx%2B6.00.1x%2B2T2020%2Btype%40sequential%2Bblock%40ca19e125470846f2a36ad1225410e39a

s = 'cmbobboboblbobboobobooobob'
slice_string = 'bob'

total=0

for i in range(0, len(s)-len(slice_string)+1):
    if s[i:i+len(slice_string)] == slice_string:
        # print(f"Found {slice_string}")
        total += 1
    # else:
    #     print(f"No {slice_string} in " + s[i:i+len(slice_string)])

print("Number of times bob occurs is: "+ str(total))