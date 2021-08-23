class myClass():
  def method1(self):
    print("myclass method1")
  
  def method2(self,somestring):
    print(somestring)

class anotherClass(myClass):
  def method1(self):
    myClass.method1(self)
    print("another class method")
  
  def method2(self,somestring):
    print("another class method2")

def main():
  #c = myClass()
  #c.method1()
  #c.method2("this is my string")

  d = anotherClass()
  d.method1()
  d.method2("anotherclass")

if __name__ == "__main__":
  main()

