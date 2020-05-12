# Task
# Take random set of commands from stdin and execute them in a sequence
# Consider a list (list = []). You can perform the following commands:
# insert i e: Insert integer i at e position
# print: Print the list.
# remove e: Delete the first occurrence of integer
# append e: Insert integer at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Source: https://www.hackerrank.com/challenges/python-lists/problem

# N = Number of commands that would be passed to this program
N = int(input())
l = []

# execute for N number of time
for _ in range(N):
    # be ready for an input and split it into command and arguments
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        print(cmd)
        # l is the list and .cmd is the way you perform an operation on a list.
        # Lists once created cannot be modified other than using list operators
        eval("l."+cmd)
    else:
        print(l)