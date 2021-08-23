# 2 looping strategies while and for
def main(x):
  #x = 0
  while (x<5):
    print(x)
    x = x+1
  print("-----------")
# define a for loop over a range of numbers
  for y in range(5,10):
    print(y)
    if (y==7): break
  
  days=["mon","tue","wed","thu","fri","sat","sun"]
  for i,d in enumerate(days):
    print(d)
    print("index,",i)

main(3)