#Given 
  # an array nums, 
# write a function 
  # to move all zeroes to the end of it 
  # while maintaining the relative order of the non-zero elements.

nums=[0,1,0,2,0]

def movezeros(nums):
  zeros=[]
  nonzeros=[]
  for i in range(len(nums)):
    if nums[i]==0:
      zeros.append(0)
    else:
      nonzeros.append(nums[i])
  return nonzeros+zeros

def movezeros1(nums):
  for i in nums:
    if i==0:
      nums.remove(0)
      nums.append(0)
  return nums

nums=[0,1,0,2,0]
array2 = [1,7,0,0,8,0,10,12,0,4]

print(movezeros1(array2))



