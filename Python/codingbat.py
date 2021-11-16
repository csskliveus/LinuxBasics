

# def make_tags(tag, word):
#   sampleFormat='<'+tag+'>'+word+'</'+tag+'>'
#   return sampleFormat

# print(make_tags('i','myword'))


# def make_out_word(out, word):
#   return out[0:2]+word+out[2:4]

# print(make_out_word('<<>>', 'Yay'))

# # https://codingbat.com/prob/p148853

# def extra_end(str):
#   return str[-2:]+str[-2:]+str[-2:]

# print(extra_end('Hello'))

# # https://codingbat.com/prob/p184816
# # Given a string, return the string made of its first two chars, so the String "Hello" yields "He"
# def first_two(str):
#   #print(str)
#   if len(str)<=2:
#     return str
#   else:
#     return str[0:2]

# print(first_two('He'))

# https://codingbat.com/prob/p107010
# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
def first_half(str):
  if len(str)>1:
    strLen=int(len(str)/2)
    print(strLen)
    return str[0:strLen]
  else:
    return str
print(first_half('WooHoo'))

nums=[1,2,3]
#k=nums.pop(0)
nums.append(nums.pop(0))
print(nums)
nums.reverse()
print(nums)


print(nums)




