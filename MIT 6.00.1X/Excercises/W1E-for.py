# num = 0
# for num in range(2, 11, 2):
#     print(num)
# print("Goodbye!")

# num = 10
# print("Hello!")
# for num in range(num, 0, -2):
#     print(num)

end = int(input("A number: "))

total = 0
for num in range(end+1):
    total = total + num
    # print(total, num)

print(total)
