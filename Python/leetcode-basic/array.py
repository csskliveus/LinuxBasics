# Given an integer array nums sorted in non-decreasing order, 
# remove the duplicates in-place such that each unique element appears only once.
#  The relative order of the elements should be kept the same.

#nums = [1,1,2,2,3,3,4,4,4,4,3]
#nums = [1,1,2]

# nums.sort()
# print (nums)
# print (len(nums))
# i=0
# remove duplicates in array
  # while i < len(nums)-1:
  #   if nums[i] == nums[i+1]:
  #     #nums.remove(nums[i])
  #     del nums[i]
  #   else:
  #     i +=1
  # print(nums)

# remove selected item from array
#nums = [1,1,2,2,3,3,4,4,4,4,3]
  #nums = [1]
  # nums = [2,3,3,2]
  # nums.sort()
  # i=0
  # print(len(nums))
  # val = 3
  # while i <= len(nums)-1:
  #   print(i)
  #   if nums[i] == val:
  #     nums.remove(nums[i])
  #   #elif nums[i+1] == val:
  #    # nums.remove(nums[i+1])
  #   else:
  #     i += 1
  # print(nums)

# count prime numbers
  # n = 10
  # i = 2
  # primaryCount=0

  # while i < n:
  #   isprime= False
  #   for k in range(2,n):
  #     if i!=k and i%k == 0:
  #       #print(" not prime number",i)
  #       isprime = False
  #       break
  #     else:
  #       isprime = True
  #   if isprime:
  #     print("prime number",i)
  #     primaryCount += 1
  #   i += 1

  # print(primaryCount)

# isomorphic words
mapping_a_b = {}
mapping_b_a = {}

a = "egg"
b = "add" 

s = "foo"
t = "bar"

result0 = zip(a,b)
result01 = zip(b,a)
result1 = zip(s,t)
result2 = zip(t,s)
print(list(result1))
print(list(result2))
print(list(result0))
print(list(result01))

for c1,c2 in zip(a,b):
  print(c1)
  print(c2)
  if (c1 not in mapping_a_b) and (c2 not in mapping_b_a):
    mapping_a_b[c1]=c2
    mapping_a_b[c2]=c1
  elif (mapping_a_b.get(c1) != c2 or mapping_b_a.get(c2) != c1):
    print('somthing')

print(mapping_a_b)
print(mapping_b_a)

# for l in b:
#   for k in a:
#     if l in mapping_b_a.keys(): # if key already present in dictionary
#       print("exists")
#       keyvalue= mapping_b_a[l]
#       if keyvalue == k:  
#         break
#     else:      # if key is a new key
#       print("new key ")
#       mapping_b_a[l]=k
    
# print (mapping_a_b)
# print (mapping_b_a)



        