# mystring='mynewcity'
# for letter in mystring:
#   print(letter)

# Inheritance

  # class parentclass(object):
  #   def __init__(self,name):
  #     self.name=name
  #   def printname(self):
  #     return self.name

  # class childclass(parentclass):
  #   def childfun():
  #     print('child class object')


  # par = parentclass("my name is chandra")
  # print(par.printname())

  # childobj = childclass("child")
  # print(childobj.printname())

# for letters in 'myname':
#   print(letters)

# mylist = [(1,2),(2,3),(3,4),(4,5),(5,6)]
# mylist.sort()
# print(len(mylist))
# for (a,b) in mylist:
#   print(a)
#   print(b)

# d = {'k1':1,'k2':2,'k3':3}
# for item in d.items():
#   print(item)
# for item in d:
#   print(item)

# x =[1,2,3]

# for item in x:
#   pass
# print("my name")

#print(list(range(0,5)))

word = 'abcdes'

for index,letter in enumerate(word):
  print(index)
  print(letter)
  print('\n')

mylist1 = [1,2,3]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]

for item in zip(mylist1,mylist2,mylist3):
  print(item)
  #   (1, 'a', 100)
  # (2, 'b', 200)
  # (3, 'c', 300)