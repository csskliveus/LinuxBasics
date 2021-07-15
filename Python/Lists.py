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