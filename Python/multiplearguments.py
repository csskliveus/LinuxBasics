# Passing multiple argumnets in python
def fun(*args):
 for arg in args:
   print(arg)

fun('me','la','ca')


# Inheritance in python 

class parentclass(object):
  #Declare contructor in class
  def __init__(self,name):
    self.name=name
  
  def printname(self):
    return self.name

class childclass(parentclass):
  def childfun(self):
    print('child class object')

par=parentclass('This is parent class')
print(par.printname())

child=childclass('mynamepar')
child.childfun()

# What map function

# Map function is used to iterate on a 

def fun(a,b):
  return a+b 
  ## call a function 
x = map(fun,("me","menot"),("you","younot"))
print (x)
print (list(x))

