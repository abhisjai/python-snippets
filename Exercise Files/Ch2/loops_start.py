#
# Example file for working with loops
#

def main():
  # # define a while loop
  # x = 0
  # while (x <5):
  #   print(x)
  #   x = x+1

  # # define a for loop
  # for i in range (0,10):
  #   print(i)

  # # use a for loop over a collection
  # days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  # for d in days:
  #   print(d)
 
  # # use the break and continue statements
  # for x in range(5, 10):
  #   if (x ==7): break
  #   print(x)

  # for x in range (5, 10):
  # #Continue statement will skip rest of the code for given interation
  #   if (x % 2 == 0): continue
  #   print(x)

  #using the enumerate() function to get index 
  days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  for i, d in enumerate(days):
    print(i, " ", d)


if __name__ == "__main__":
  main()
