# basic function

def func1():
  print("am basic function definition")

#print(func1())

# function that takes arguments
def func2(arg1, arg2):
  print(arg1," ",arg2)

#func2("myname","yourname")

def cube(x):
  return x*x


# conditions

def func4():
  x,y = 100,100
  # conditional flow uses if, elif else
  if(x < y):
    st = "x in less than y"
  elif(x == y):
    st = "x is equal to y"
  else:
    st = "x is greater"
  print(st)


a=1
b=2
def func5():
  global b
  print(a)
  print(b)
  b= a+b

def func6():
  print(hello)

#func2
#print(cube(2))
func4()
func5()
print(b)
func6()


