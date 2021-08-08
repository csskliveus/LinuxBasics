# Given an array containing None values 
  # fill in the None values with most recent 
  # non None value in the array 



def nonNoneValue(nums):
  nonzero=''
  for i in range(len(nums)):
    #print(nums[i])
    #print(i)
    if nums[i] != None:
      nonzero=nums[i]
    else:
      nums[i] = nonzero
  return nums

array1 = [1,None,2,3,None,None,5,None]
print(nonNoneValue(array1))

