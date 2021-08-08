#https://towardsdatascience.com/10-algorithms-to-solve-before-your-python-coding-interview-feb74fb9bc27
# Reverse string

# def solution(x):
#   string = str(x)

#   if string[0] == '-':
#     return int('-'+string[:0:-1])
#   else:
#     return int(string[::-1])

# print(solution(-231))


# Average of words length
  # For a given sentence, return the average word length. 
  # Note: Remember to remove punctuation first.

# sentence1 = "Hi all, my name is Tom...I am originally from Australia."
# sentence2 = "I need to work very hard to learn more about algorithms in Python!"

# def solution(sentence):
#   totallength=0
#   for p in "!?',;.":
#     sentence = sentence.replace(p,'')
#   words= sentence.split()
#   print(words)
#   for word in words: 
#     totallength = sum(totallength+len(word))
#   print(totallength)

# solution(sentence1)



          


