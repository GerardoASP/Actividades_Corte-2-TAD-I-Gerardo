import math

class DoubleLinkedList:
  class Node:
    def __init__(self,value):
      self.value = value
      self.prev = None
      self.next = None
  
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
  
  def show_elements_list(self):
    array=[]
    current_node = self.head
    #Mientras si exista al menos un nodo entonces
    while(current_node != None):
      array.append(current_node.value)
      current_node = current_node.next_node
    return print(array)
  
  def append(self,value):
    new_node = self.Node(value)

    if self.head == None and self.tail == None:
      self.head = new_node
      self.tail = self.head
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
    self.length += 1
    return print(new_node.value)
  
  
  
  