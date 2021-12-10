# https://www.w3resource.com/python-exercises/python-basic-exercises.php

# Write a Python program to create a histogram from a given list of integers. 

# def histogram(items):
#   for n in items:
#     output = ''
#     times=n
#     while(times > 0):
#       output += '*'
#       times = times - 1
#     print(output)

# histogram([3,5,7])

# 27. Write a Python program to concatenate all elements in a list into a string and return it.

  # items = [1,3,5]
  # a=''
  # for n in items:
  #   a += str(n)
  # print(a)


# 28. Write a Python program to print all even numbers from a given numbers 
# list in the same order and stop the printing if any numbers that come after 237 in the sequence.

  # numbers = [    
  #     386, 462, 47, 418, 907, 344, 236, 375, 823, 566,237, 597, 978, 328, 615, 953, 345, 
  #     399, 162, 758 ]

  # for n in numbers:
  #   if n == 237:
  #     break
  #   else:
  #     if n%2 == 0:
  #       print(n)

# 29. Write a Python program to print out a set containing all the 
# colors from color_list_1 which are not present in color_list_2
   
  # color_list_1 = set(["White", "Black", "Red"])
  # color_list_2 = set(["Red", "Green"])
  # Solution
    #print(color_list_1.difference(color_list_2))

    #print(color_list_1-color_list_2)

    # print(set([color for color in color_list_1 if color not in color_list_2]))

# 30. Write a Python program that will accept the base and height of a triangle and compute the area

  # def areaFunction(a,b):
  #   c = a * b
  #   return c

  # print(areaFunction(2,3))

#31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

#32. Write a Python program to get the least common multiple (LCM) of two positive integers


# 35. Write a Python program that will return true if the two given integer 
# values are equal or their sum or difference is 5.

  # def integerEqual(x,y):
  #   if x == y:
  #     return True
  #   elif x+y ==5:
  #     return True
  #   elif x-y == 5:
  #     return True
  #   else:
  #     return False

  # print(integerEqual(10,5))

# 36. Write a Python program to add two objects if both objects are an integer type.
  # x=5
  # y=5
  # def add2Objects(x,y):
  #   if isinstance(x,int) and isinstance(y,int):
  #     return x + y

  # print(add2Objects(x,y))

# 37. Write a Python program to display your details like name, age, address in three different lines

# 38. Write a Python program to solve (x + y) * (x + y).
  # x=4
  # y=3
  # def solveMathProblem(x,y):
  #   return ((x+y)**2)
  # print(solveMathProblem(4,3))

# 41. Write a Python program to check whether a file exists.


# nums = [1,4,5,6]

# def evenNumber(nums):
#   even = []
#   for n in nums:
#     print(n)
#     if n % 2 == 0:
#       even.append(n)
#     else:
#       pass
#   return even
# print(evenNumber(nums))

# def myFunc(*args):
#   print(*args)
#   sum= 0 
#   for i in args:
#     sum = sum + i
#   return sum

# print(myFunc(1,2,3,5,6,))

mywork = 'Thisismyword'

# def evenUpperoddLower(mywork):
#   for i,w in set(mywork):
#     print(i)
#     print(w)

# evenUpperoddLower(mywork)

# sampleInput = raw_input()
# sampleInput = "1"
# def countOccurrence(sampleInput):
#     w1 = ''
#     b = ''
#     for w in sampleInput:
#         i=0
#         wordCount=0
#        # print(w)
#         while i < len(sampleInput):
#             if w == sampleInput[i]:
#                 wordCount = wordCount + 1
#             i = i + 1
#         b = w + str(wordCount)
#         if w not in w1:
#           w1 = w1 + b
#     return w1 
# print(countOccurrence(sampleInput))
# mystring="primeCheck"
# def myfun(mystring):
#   i = 0 
#   a = ''
#   c =''
#   while i < len(mystring):
#     if i == 0 and mystring[i].isupper():
#       c = mystring[i].lower()
#       a = a + c
#     elif i != 0 and mystring[i].isupper():
#       c = "_"+ mystring[i].lower()
#       a = a + c
#     else:
#       a = a + mystring[i]
#     i = i + 1
#   return a
# print(myfun(mystring))

  
numlist = [9,1,2,2]
numlist.sort()
print(numlist)

l1 = (numlist.pop())
print(len(numlist))



