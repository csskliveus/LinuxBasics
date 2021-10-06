# https://www.interviewbit.com/python-interview-questions/
# class
  # class student:
  #   def __init__(self,fname,myname,yourname):
  #     self.firstname = fname
  #     self.myname = myname
  #     self.yourname = yourname

# Decorators

  # def lowercase_decorator(function):
  #   def wrapper():
  #     func = function()
  #     string_lowercase = func.lower()
  #     return string_lowercase
  #   return wrapper

  # def splitter_decorator(function):
  #   def wrapper():
  #     func = function()
  #     string_split = func.split()
  #     return string_split
  #   return wrapper


  # @splitter_decorator
  # @lowercase_decorator
  # def hello():
  #   return 'Hello World'

  # print(hello())

# Iterators

  # class ArrayList:
  #   def __init__(self,number_list):
  #     self.numbers = number_list
    
  #   def __iter__(self):
  #     self.pos = 0 
  #     return self
    
  #   def __next__(self):
  #     if(self.pos < len(self.numbers)):
  #       self.pos += 1
  #       return self.numbers[self.pos - 1]
  #     else:
  #       raise StopIteration

  # array_obj = ArrayList([1,2,3])  

  # it= iter(array_obj)
  # print(next(it))
  # print(next(it))
#------------------------------------------------------------------------------#
# OOPS interview questions
# class InterviewbitEmployee:
#   def __init__(self,emp_name):
#     self.emp_name = emp_name

# emp_1 = InterviewbitEmployee("mr employee")

#--------------------------------------------------------------------

# generate a random number
# import random
# print(random.random())

# print(random.randrange(5,100,2)) # (start,stop,step)

# # is alpha numeric
# "abdc1321".isalnum()

# Coding questions -------------------------------------------------
# 1. Pass multiple values into list
  # def fun(*var):
  #   for i in var:
  #     print(i)
  # fun(1,2,3,5)

# 2. Check whether values in a list are unique.
  # given a list
  # conver list into set
  # check count of the list and set
  # l1 = [1,1]
  # l2 = set(l1)
  # print(len(l1)==len(l2))

# 3. Counting the number of every character of a given text file
  # import collections
  # import pprint

  # with open("questions.txt",'r') as data:
  #   count_data = collections.Counter(data.read().upper())
  #   count_value = pprint.pformat(count_data)
  # print(count_value)

# 4. Write a program to add 2 numbers with out plus operator

def add_number(num1,num2):
  while num2 != 0:
    data = num1 & num2
    #print(data)
    num1 = num1 ^ num2
    num2 = data << 1
    print(num2)
  return num1

print(add_number(2,10))