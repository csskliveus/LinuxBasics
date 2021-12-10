# x = 50
# def printWords():
#   global x
#   x= 200 
#   print(x)
#   print(f'X is {x}')

# printWords()
# print(x)

A='10101'
P='00111'

def countlikesAndDislikes(A,P):
    i=0
    likeCount=0
    while i < len(A):
      if A[i] == P[i]:
          likeCount = likeCount + 1
      i = i + 1
    return likeCount
print(countlikesAndDislikes(A,P))