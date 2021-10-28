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

  #punto 1
  #def append2(self):
    #value = int(input('Digite un numero: '))
    #contador = 3
    #current_node = self.head
    #new_node = self.Node(value)
    #while current_node != None:
      #if current_node
      #current_node = current_node.next
  
  #punto 1
  def append3(self):
    contador_nodos = 0
    cant_nodos = int(input('Digite la cantidad de nodos: '))
    while contador_nodos < cant_nodos:
      value = int(input('Digite un numero: '))
      contador = 3
      new_node = self.Node(value)
      current_node = self.head

      if self.head == None and self.tail == None:
        self.head = new_node
        self.tail = self.head
      else:
        while current_node != None:
          if value == current_node.prev.value + contador:
            self.append(value)
          else:
            print('No se puede agregar ese valor: ')
          contador += 2
          current_node = current_node.next
      
      contador_nodos += 1
    