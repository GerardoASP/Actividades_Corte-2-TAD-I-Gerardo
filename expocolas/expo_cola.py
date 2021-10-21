import math

class Cola:
  #Metodo Constructor de la clase Cola
  def __init__(self):
    self.items = []
  
  #Metodos de la clase Cola
  #Metodo #1: Encolar los elementos de la cola
  def encolar(self,x):
    self.items.append(x)
  
  #Metodo #2: descolar un elemento de la cola
  def desencolar(self):
    if self.es_vacia():
      print('La cola ya no tiene elementos')
    else:
      return self.items.pop(0)
  #Metodo #3: Validar si la esta vacía
  def es_vacia(self):
    return print(self.items == [])
  
  #Metodo #4: Cantidad de elementos de la cola
  def cantidad_elementos(self):
    return print(f'La cantidad de elementos en la cola es: {len(self.items)}')
  
  #Metodo #5: Mostrar los elementos de la cola
  def mostrar_elementos(self):
    print(f'Los elementos de la cola son: {self.items}')
  
  #Metodo #6: Mostrar el ultimo elemento de la cola
  def mostrar_ultimo_elemento(self):
    print(f'El ultimo elemento de la cola es {self.items[-1]}')
  
  #Metodo #7: Mostrar el primer elemento de la cola
  def mostrar_primer_elemento(self):
    print(f'El primer elemento de la cola es: {self.items[0]}')
  
  #Metodo #8: Obtener posición de un elemento en la cola
  def obtener_posicion_elemento(self,valor):
    pos_elemento = -1
    contador = 0
    while contador < len(self.items):
      if self.items[contador] == valor:
        pos_elemento = contador
      contador += 1
    
    return pos_elemento
  
  #Metodo #9:Obtener valor de un elemento de la cola a partir de un indice ingresado por el usuario
  def obtener_valor_por_posicion(self):
    ind = int(input('Digite el indice del elemento: '))
    while True:
      try:
        if ind < 0 and ind > len(self.items):
          ind = int(input('Indice por fuera de los rangos\n Digita nuevamente el indice: '))
        else:
          break
        break
      except ValueError:
        print('Se espera un numero no una palabra')
        ind = int(input('Indice por fuera de los rangos\n Digita nuevamente el indice: '))
    
    return self.items[ind]
  
  #Metodo #10:Invertir la Cola
  def invertir_cola(self):
    i= 0
    for n in range(math.floor(len(self.items)/2)):
      i = i-1
      self.items[n],self.items[i] = self.items[i],self.items[n]