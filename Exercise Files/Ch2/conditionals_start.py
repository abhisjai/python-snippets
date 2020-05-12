#
# Example file for working with conditional statements
#

def main():
  x = 10
  y = 100

  # conditional flow uses if, elif, else  

  if (x < y):
    str = "x is less than y"
  elif (x == y):
    str = "x is equal to y" 
  else:
    str = "x is greater than y"

  print(str)
  # conditional statements let you use "a if C else b"
  
  str = "x is less than y" if (x < y) else "x is greater than y"
  print(str)

if __name__ == "__main__":
  main()
