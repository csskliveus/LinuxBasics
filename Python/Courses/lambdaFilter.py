# Map

def addition(n):
  return n + n

numbers = (1,2,3,4)
result = map(addition,numbers)
print(list(result))

numbers = (1,2,4,5)
result = map(lambda x: x + x, numbers)
print(list(result))

# add 2 lists
num1 = [1,2,3]
num2 = [3,4,5]
res = map(lambda x,y: x + y, num1,num2)
print(list(res))

# Filter 

def check_even(num):
  return num%2 == 0
even1 = [1,2,3,4,5,5,6,7,8,9,10]
res2 = filter(check_even,even1)
print(list(res2))

nums = [10,20,30]
r1 = map(lambda num:num*2,nums)
print(list(r1))

r2 = map(lambda num:num/2,nums)
print(list(r2))

