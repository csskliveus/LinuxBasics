None # can be used to assign value as None

mylist=['one','two','three']

# indexing
mylist[0]
mylist[1]

#slicing
mylist[1:]  # ['two', 'three']

# adding 2 lists [concatination]
mynewlist = mylist + mylist 

# Append to list [adds an element at the end of the list]

mylist.append('fournewvalue')

# remove last item from the list.

mylist.pop() # removes list item [by default] if no index is specified.


mylist.pop(0) # removes list item at specified index.

mylist.sort() # sort values in the list.

mylist.reverse() # reverse values in list.

mylist[::-1] # reverse values in list

# List comprehention

a = [1,2,3]

squaredlist = [x**2 for x in a]

squareddictionary = {x:x**2 for x in a}

# Conditional filtering

my_list = [2,3,5,7,11]

squared_list = [x**2 for x in my_list if x%2 !=0]

# Combining multiple lists to one

a = [1,2,3]
b = [7,8,9]

[(a + b) for (a,b) in zip(a,b)]

[(x,y) for x in a for y in b]

# Flattning a multi-dimensional list

my_list = [[10,12,20],[11,12,13],[15,16,17]]
flattened = [x for temp in my_list for x in temp ]

