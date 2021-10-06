#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#nums = [3,2,3]
  # nums = [2,7,11,15]
  # target = 9

  # def twoSum(nums, target):
  #   """
  #   :type nums: List[int]
  #   :type target: int
  #   :rtype: List[int]
  #   """
  #   for j,k in enumerate(nums):
  #     match = target - k
  #     if match in  nums:
  #       if (nums.index(match) != j):
  #         return [j,nums.index(match)]

  # print(twoSum(nums,target))



#Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# x = 1534236469
# def myfun(x):
#   if x.__str__()[0] == '-':
#     result= -(int(x.__str__()[1::][::-1])) 
#     if (-2**31) <= result:
#       return result
#     else:
#       return 0
#   else:
#     result = (int(x.__str__()[::-1]))
#     if result <=(2**31 - 1): 
#         return result
#     else:
#       return 0
# print(myfun(x))


# Palindrome Number

# def fun(x):
#   y = -(int(x.__str__()[1::][::-1])) if x<0 else int(x.__str__()[::-1])
#   #print(y)
#   if (x - int(y)) == 0:
#       return True
#   else:
#       return False
# print(fun(-123))



# Longest common prefix
  #Input: strs = ["flower","flow","flight"]
  #Output: "fl"
  #strs = ["a"] #,"flow","flight"]
  #strs = ["d","racecar","car"]

  #strs = ["","a","a"]
  #print(strs.__len__())
  # def func(strs):
  #   i =1
  #   val1=False
    # if (strs.__len__() >= 1 and strs.__len__() <= 200): 
    #     #print(strs[0].__len__())
    #     if strs[0].__len__() > 1:
    #       val = strs[0][0:2] 
    #     elif strs[0].__len__() == 1:
    #        val = strs[0][0:1] 
    #     elif strs[0].__len__() == 0:
    #       val = ""
        
    #     while i <= (strs.__len__())-1:
    #         if (strs[i].__len__() >= 0) and (strs[i].__len__() <= 200) and strs[i].islower():
    #             #print(strs[i])
    #             if (val != (strs[i][:2])):
    #                 #print(val1)
    #                 val1=False
    #                 break
    #             else:
    #                 val1= True
    #         else:
    #             val1=False
    #         i +=1
    # else:
    #     return ""
    
    # return val if val1 or (strs.__len__() == 1) else ""

  #print(func(strs))

  # strs = ["flower","flow","flight"]
  # def lcp(self, str1, str2):
  #       i = 0
  #       while (i < len(str1) and i < len(str2)):
  #           if str1[i] == str2[i]:
  #               i = i+1
  #           else:
  #               break
  #       return str1[:i]

  #   # @return a string                                                                                                                                                          
  # def longestCommonPrefix(self, strs):
  #     if not strs:
  #         return ''
  #     else:
  #         return reduce(self.lcp,strs)

# Valid parenthesis

# s = '{[]]}'

# #print(list(enumerate(zip(s))))
# def func1(s):
#   while '()' in s or '[]' in s or '{}' in s:
#     s= s.replace('()','').replace('[]','').replace('{}','')
    
#     return True if s.__len__() == 0 else False

# print(func1(s))
  


#35. Search Insert Position
# nums = [1,3,5,6]
# target= 7
# nums.sort()
# position=0
# if len(nums) >= 1 and len(nums) <=10**4:
#       if target in nums:
#           position = nums.index(target)
#       elif target > max(nums):
#           position = (len(nums))
#       elif target < min(nums):
#           position = 0
#       else:
#           for i in range(len(nums)):
#               if nums[i] < target and nums[i+1] > target:
#                   position = (i+1)
#                   break
# else:
#   print("list is empty")
# print(position)
  

# contiguous sub array

nums = [-2,1,-3,4,-1,2,1,-5,4]
i=1
sum=0
for i in range(len(nums)):
   sum = sum +  nums[i]

#print(sum)

curSum = maxSum = nums[0]

for num in nums[1:]:
  curSum = max(num, (curSum+num))
  maxSum = max(maxSum, curSum)
  #print(num)
print(maxSum)
print(curSum)









