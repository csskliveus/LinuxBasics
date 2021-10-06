# https://realpython.com/linked-lists-python/
# class LinkedList:
#   def __init__(self):
#     self.head = None
  
#   def __repr__(self):
#     node = self.head
#     nodes = []
#     while node is not None:
#       nodes.append(node.data)
#       node = node.next
#     nodes.append("None")
#     return " -> ".join(nodes) 


# class Node:
#   def __init__(self,data):
#     self.data = data
#     self.next = None

#   def __repr__(self):
#     return self.data

# llist = LinkedList()

# print(llist)

# first_node = Node("a")
# llist.head = first_node
# print(llist)

# https://www.youtube.com/watch?v=JlMyYuY1aXU&ab_channel=BrianFaure

class node:
  def __init__(self,data=None):
    self.data=data
    self.next=None

class linked_list:
  def __init__(self):
    self.head = node()
  def append(self,data):
    new_node = node(data)
    cur = self.head
    while cur.next!=None:
      cur = cur.next
    cur.next = new_node
  def length(self):
    cur = self.head
    total = 0
    while cur.next != None:
      total += 1
      cur = cur.next
    return total
  def display(self):
    elems = []
    cur_node = self.head
    while cur_node.next!=None:
      cur_node=cur_node.next
      elems.append(cur_node.data)
    print(elems)
  def get(self,index):
    if index >= self.length():
      print("error")
      return None

  
my_list = linked_list()



my_list.append(1)
my_list.append(2)
my_list.display()

# https://www.youtube.com/watch?v=Ast5sKQXxEU&ab_channel=JoeJames