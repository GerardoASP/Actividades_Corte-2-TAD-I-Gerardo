import math
class DoubleLinkedLinkd:
    class Nodo:
    #Constructor de la clase nodo
      def __init__(self, value):
        self.value = value
        self.previous_node = None
        self.next_node = None
    #Constructor de la clase DoubleLinkeLis
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

    def append(self, value):
      new_node = self.Nodo(value)
      if self.head == None and self.tail == None:
        self.head = new_node
        self.tail = self.head
      else:
        self.tail.next_node = new_node
        new_node.previous_node = self.tail
        self.tail = new_node
      self.length += 1
      return print(new_node.value)

    def unshift(self, value):
      new_node = self.Nodo(value)
      if self.head == None and self.tail == None:
        self.head = new_node
        self.tail = self.head
      else:
        self.head.previous_node = new_node
        new_node.next_node = self.head
        self.head = new_node
        self.length +=1
      return print(new_node.value)

    def pop(self):
      if self.length == 1:
        self.head = None
        self.tail = None
      else:
        remove_node = self.tail
        self.tail = remove_node.previous_node
        self.tail.next_node = None
        remove_node.previous_node = None
        self.length -= 1
        #return remove_node.value
  
    def shift(self):
      if self.length == 1:
        self.head = None
        self.tail = None
      elif self.head != None:
        remove_node = self.head
        self.head = remove_node.next_node
        remove_node.previous_node = None
        self.length -= 1
        #return remove_node.value
      else:
        return None
  
    def get(self, index):
      cont_posicion = 0
      if index == self.length-1:
        #print(self.tail.value)
        return self.tail
      elif index == 0:
        #print(self.head.value)
        return self.head
      elif not (index < 1 or index > self.length):
        current_node = self.head
        while cont_posicion != index:
          current_node = current_node.next_node
          cont_posicion += 1
        #print(current_node.value)
        return current_node
      else:
        return None

    def set(self, index, value):
      update_node = self.get(index)
      if update_node != None:
        update_node.value = value
      else:
        return None
    
    def calculate_length_dll(self):
      cant = 0
      current_node = self.head
      while(current_node != None):
        current_node = current_node.next_node
        cant += 1
      
      return cant
    
    def insert(self, index, value):
      # Agrega un elemento en donde sea en la linkedlist dado el index
      if index == self.length - 1:
        return self.append(value)
      elif not (index >= self.length or index < 0):
        new_node = self._Nodo(value)
        ant_nodes = self.get(index)
        sig_node = ant_nodes.next_node
        ant_nodes.next_node = new_node
        new_node.nodo_anterior = ant_nodes
        new_node.next_node = sig_node
        sig_node.nodo_anterior = new_node
        self.length += 1
      else:
        return None
    
    def remove(self):
      ind = int(input(' Digita el indice del Nodo a Eliminar: '))

      bandera = True
      
      while bandera:
        if ind == 0:
          self.shift()
          bandera = False
        elif ind == self.length-1:
          self.pop()
          bandera = False
        elif not(ind >= self.length or ind < 0):
          nodo_usuario = self.get(ind)
          nodo_antecesor = nodo_usuario.previous_node
          nodo_sucesor = nodo_usuario.next_node
          nodo_antecesor.next_node = nodo_sucesor
          nodo_sucesor.previous_node  = nodo_antecesor
          nodo_usuario.previous_node = None
          nodo_usuario.next_node = None
          self.length -= 1
          return nodo_usuario
          bandera = False
        else:
          ind = int(input(' Error\n Digita nuevamente el indice del nodo a eliminar: '))
    
    def reverse(self):
      enlace_importante = None
      nodo_actual = self.head 
      self.tail = nodo_actual
      while nodo_actual != None:
        enlace_importante = nodo_actual.previous_node
        nodo_actual.previous_node = nodo_actual.next_node
        nodo_actual.next_node = enlace_importante
        nodo_actual = nodo_actual.previous_node
      self.head = enlace_importante.previous_node
    
    
    def reverse_2(self):
      enlace_importante = None
      nodo_actual = self.head
      self.tail = nodo_actual
      while nodo_actual != None:
        enlace_importante = nodo_actual.previous_node
        nodo_actual.previous_node = nodo_actual.next_node
        nodo_actual.next_node = enlace_importante
        nodo_actual.value = math.pow(nodo_actual.value,2)
        nodo_actual = nodo_actual.previous_node
      self.head = enlace_importante.previous_node
      self.head.value = math.pow(self.head.value,2)