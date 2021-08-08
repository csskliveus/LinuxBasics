#Given two sentences, 
# return an array 
# that has the words that appear in one sentence and not the other 
# and an array with the words in common. 

sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'

sentencelist1=[]
sentencelist2=[]

sentencelist1=sentence1.split()
sentencelist2=sentence2.split()

setenceset1=(set(sentencelist1))
setenceset2=(set(sentencelist2))

print(setenceset1.difference(setenceset2))

