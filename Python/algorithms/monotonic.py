
# Monotonic arrays



def monotonic_solution1(nums): 
    return (all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) or 
            all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1))) 


def monotonic_solution2(nums):
  print(len(nums))
  decrease=False
  increase=False
  for i in range(len(nums)-1):
    if nums[i] <= nums[i+1]: 
      increase=True
    else:
      increase=False
      break

  if increase==False: 
    for i in range(len(nums)-1):
      if nums[i] >= nums[i+1]:
        decrease=True
      else:
        decrease=False
        break
        
  return increase,decrease

A = [6, 5, 4, 4] 
B = [1,1,1,3,3,4,3,2,4,2]
C = [1,1,2,3,7]
d =[5,4,3]
e1= [3,4,5]

increase,decrease=monotonic_solution2(d)
print("increase "+str(increase))
print("decrease "+str(decrease))