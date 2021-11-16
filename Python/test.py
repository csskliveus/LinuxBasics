# # # mystring='mynewcity'
# # # for letter in mystring:
# # #   print(letter)

# # # Inheritance

# #   # class parentclass(object):
# #   #   def __init__(self,name):
# #   #     self.name=name
# #   #   def printname(self):
# #   #     return self.name

# #   # class childclass(parentclass):
# #   #   def childfun():
# #   #     print('child class object')


# #   # par = parentclass("my name is chandra")
# #   # print(par.printname())

# #   # childobj = childclass("child")
# #   # print(childobj.printname())

# # # for letters in 'myname':
# # #   print(letters)

# # # mylist = [(1,2),(2,3),(3,4),(4,5),(5,6)]
# # # mylist.sort()
# # # print(len(mylist))
# # # for (a,b) in mylist:
# # #   print(a)
# # #   print(b)

# # # d = {'k1':1,'k2':2,'k3':3}
# # # for item in d.items():
# # #   print(item)
# # # for item in d:
# # #   print(item)

# # # x =[1,2,3]

# # # for item in x:
# # #   pass
# # # print("my name")

# # #print(list(range(0,5)))

# # word = 'abcdes'



# # # for index,letter in enumerate(word):
# # #   print(index)
# # #   print(letter)
# # #   print('\n')

# # mylist1 = [1,2,3]
# # # mylist2 = ['a','b','c']
# # # mylist3 = [100,200,300]



# # # for item in zip(mylist1,mylist2,mylist3):
# # #   print(item)
# #   #   (1, 'a', 100)
# #   # (2, 'b', 200)
# #   # (3, 'c', 300)

# # car = {
# #   "brand": "Ford",
# #   "model": "mustang",
# #   "year": 1964
# # }

# # print(car.keys())
# # print(car.values())

# # car["place"] = "la"

# # print(car)

# # t = (1,2,3)
# # print(type(t))
# # print(t[0])
# # print(t.count(1))

# # myquestions = open("C:\\WorkingDirectory\\vca\\voyager\\Code\\LinuxBasics\\Python\\questions.txt")
# # print(myquestions.read())
# # print(myquestions.readlines())

# # For loops
# # d = {'d1':1,'d2':2,'d3':3}
# # for key,value in d.items():
# #   print(key,value)

# # while loop
# # x=0
# # while x < 5:
# #   print(x)
# # else:
# #   print(f'print value of x is {x}') 

# # word = 'losangeles'

# # for item in enumerate(word):
# #   print(item)

# # i = 0
# # print(len(word))
# # for i in range(0,len(word)):
# #   print(word[i])

# # for index,letter in enumerate(word):
# #   print(index)
# #   print(letter)
# #   print('\n')

# # mylist1 = [1,2,3]
# # mylist2 = ['a','b','c','d']
# # for item in zip(mylist1,mylist2):
# #   print(item)

# #print (zip(mylist1,mylist2))

# # st = 'Print only the words that start with s in this sentence'

# # for st1 in st.split(' '):
# #   if st1[0]=='s':
# #     print(st1)

# # mystlist = [str1  for str1 in st.split(' ') if str1[0]=='s']
# # print(mystlist)

# # mylist2 = [n for n in range(0,50) if n%3==0]
# # print(mylist2)


# # st = 'Print every word in this sentence that has an even number of letters'

# # mylist3=[wrd for wrd in st.split(' ') if len(wrd)%2!=0]
# # print(mylist3)

# # st = 'Create a list of the first letters of every word in this string'

# # mylist3=[wrd[0] for wrd in st.split(' ')]
# # print(mylist3)

# # # mylist5 = [1,1,2,3,4,5]
# # # mylist5.sort()
# # # def myfun(mylist):
# # #   mylist=list(set(mylist))
# # #   return mylist
# # # print(myfun(mylist5))

# # # a = [1,2,3]
# # # b = [4,5,6]
# # # for a in zip(a,b):
# # #   print(a)

# # # print([(x,y) for y in b for x in a])

# # # print([(x,y) for (x,y) in zip(a,b)])

# # # tup1=(1,2,3)
# # tup2=(4,5,6)
# # print(tup1+tup2)

# # # lambda is an anonymous function 

# # mul=lambda a,b: a*b
# # print(mul(4,5))

# # def myWrapper(n):
# #   return lambda a : a*n 
# # mulFive = myWrapper(5)
# # print(mulFive(2))


# # class myclassname:
# #   def __init__(self,empname):
# #     self.empname = empname

# # emp1 = myclassname('vca')
# # print(emp1.empname)

# # class A:
# #   def __init__(self,a_name):
# #     self.a_name
# a = [1,1,2,4]
# def uniqueNumbers(numlist):
#   if len(numlist) == set(numlist):
#     print('No duplicate values present')
#   else:
#     print('List contains duplicate values')

# uniqueNumbers(a)

# # count of character in a given text file

# # aValue = 'chandrasekharkonda'
# # import collections
# # import pprint
# # def countCharacters():
# #   with open('C:\\WorkingDirectory\\vca\\voyager\\Code\\LinuxBasics\\sampledata.txt','r') as data:
# #     print(data.readlines())
# #     count_data = collections.Counter(data.read().upper())
# #     count_value = pprint.pformat(count_data)
# #   print(count_value)
# # countCharacters()

# def add_nums(num1,num2):
#   while num2 !=0:
#     data = num1 & num2
#     num1 = num1 ^ num2
#     num2 = data << 1
#   return num1
# print(add_nums(3,4))

# import re
# def match_text(txt_data):
#   pattern = 'ab{4,8}'
#   if re.search(pattern,txt_data):
#     return 'Match Found'
#   else:
#     return 'No match found'

# print(match_text("abbbbbbbbbbbbc"))

# from collections import Counter
# print(Counter('adfsfasfaaaasfasdf'))



# class Human(object):
#   def __init__(self,name):
#     self.human_name = name
#   def getHumanName(self):
#     return self.human_name
#   def isEmployee(self):
#     return False

# class IBEmployee(Human):
#   def __init__(self,name,emp_id):
#     super(IBEmployee,self).__init__(name)
#     self.emp_id = emp_id
#   def isEmployee(self):
#     return True
#   def get_emp_id(self):
#     return self.emp_id
#   def getHumanName(self):
#     return self.human_name

# employee = IBEmployee("Mr Employee", "IB007") 
# print(employee.isEmployee(),employee.getHumanName())

# from re import A


# a=0
# b=3
# c=0
# for i in range(7):
  
#   b=3+c
#   c=b
#   print(c)



# def stringTimes(str, n):
#   i=1
#   c=''
#   while i <= 4:
#     c=c+str
#     i=i+1
#   return c

# print(stringTimes("HI",4))

# def stringTimes(str, n):
#   i=0
#   c=0
#   while i < n: #0-0,1-3
#     if i==0:
#       c=0
#     else:
#       c=c+3
#     i=i+1
#     print(c)
#   return c
  
# stringTimes(0,5)


# make_ends = [1,2,3]

# test = [make_ends[0],make_ends[len(make_ends)-1]]
# print(test)
# print(type(test))
# ## print(type(test))

#nums=[3,5,5,6,6,7]
#nums.r
#a = [x+x for x in has23]
#print(type(a))
#print(a)

# original_list = [1,2,3,4]
# reversed_list = []
# for i in range(len(original_list)):
#   reversed_list.append(original_list.pop())

#print(reversed_list)

# https://codingbat.com/prob/p189616
#Return the number of even ints in the given array. Note: 
#  the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
# count_evens([2, 1, 2, 3, 4]) → 3
  # def count_evens(nums):
  #   evenCount=0
  #   for i in range(len(nums)):
  #     if nums[i]%2 == 0:
  #       evenCount=evenCount+1
  #   return evenCount

  # nums=[1,3,5]
  # print(count_evens(nums))

# Given an array length 1 or more of ints, 
 #return the difference between the largest and smallest values in the array.
 # Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
 # big_diff([10, 3, 5, 6]) → 7
# def big_diff(nums):
#   print(nums)
#   return max(nums)-min(nums)

  # def big_diff1(nums):
  #   max=nums[0]
  #   min=nums[0]
  #   for i in range(len(nums)):
  #     if max < nums[i]: 
  #       max=nums[i]
  #     if min > nums[i]:
  #       min=nums[i]
  #   return max,min
  # nums=[7,3,1,6,10,30,40,100,150,160,151,4,6]
  # print(big_diff(nums))
  # print(big_diff1(nums))


# Return the sum of the numbers in the array, returning 0 for an empty array. 
# Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
# sum13([1, 2, 2, 1]) -> 6 

  # def sum13(nums):
  #   sum=0
  #   i =0
  #   while i < len(nums):
  #     print(i)
  #     if nums[i]==13:
  #       i=i+1
  #     else:
  #       sum = sum + nums[i]
  #     i = i + 1
  #   return sum

  # nums = [1,2,1,5,13,1,2,13,1]
  # print(sum13(nums))

# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and 
# extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
#sum67([1, 2, 2, 6, 99, 99, 7]) → 5

def sum67(nums):
  i=0
  j=0
  sum =0 
  while i < len(nums):
    if nums[i]==6:
      while j < len(nums):
        if nums[j]==7:
          break
        j = j+1
      i = i + (j-i)
    else:
      sum = sum + 0
    i = i + 1
  return sum

nums=[1, 2, 2, 6, 99, 99, 7]
print(sum67(nums))