#
# Example file for working with classes
#


class myclass():
  def method1(self):
    print("myclass method1")

  def method2(self, somestring):
    print("myclass method2 " + somestring)

def main():
  c = myclass()
  c.method1()
  c.method2("This is a string")
  
if __name__ == "__main__":
  main()
