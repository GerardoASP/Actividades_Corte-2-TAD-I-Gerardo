import math

class Circular_Liked_List:
  class Nodo:
    #metodo constructor de la clase Nodo
    def __init__(self,value):
      self.value = value
      self.next_node = None
  
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
  
  #Metodos de la clase Circular_Liked_List
  #Metodo #1: mostrar los elementos de la lista
  def show_circular_list(self):
    array = []
    current_node = self.head
    pivote = True
    contador = self.length
    while contador != 0:
      if pivote != False or current_node != self.head:
        array.append(current_node.value)
        current_node = current_node.next_node
        pivote = False
        contador -= 1
      else:
        break
    return print(array)
  
  def append(self,value):
    nuevo_nodo = self.Nodo(value)
    if self.head == None and self.tail == None:
      self.head = nuevo_nodo
      self.tail = nuevo_nodo
    else:
      self.tail.next_node = nuevo_nodo
      nuevo_nodo.next_node = self.head
      self.tail = nuevo_nodo
    self.length += 1
  
  def unshift(self,value):
    nuevo_nodo = self.Nodo(value)

    if self.head == None and self.tail == None:
      self.head = nuevo_nodo
      self.tail = nuevo_nodo
    else:
      nuevo_nodo.next_node = self.head
      self.tail.next_node = nuevo_nodo
      self.head = nuevo_nodo
    self.length += 1
  
  #Punto 2
  def insert(self):
    indice = int(input('Digite el indice del nodo a agregar: '))
    contador = 0
    intentos = 3
    if indice == 0:
      value = int(input('Digite el valor a agregar: '))
      return self.unshift(value)
    elif indice == self.length -1:
      value = int(input('Digite el valor a agregar: '))
      while contador < intentos:
        if 