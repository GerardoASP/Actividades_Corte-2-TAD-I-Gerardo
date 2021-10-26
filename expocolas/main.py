from expo_cola import Cola

inst_cola = Cola()

inst_cola.es_vacia()

inst_cola.encolar("Sebas")
inst_cola.encolar("Gerardo")
inst_cola.encolar("Jhonotan")
inst_cola.encolar("Juan Ca")
inst_cola.encolar("Luis")
inst_cola.mostrar_elementos()
inst_cola.cantidad_elementos()
#inst_cola.mostrar_elementos()
inst_cola.mostrar_ultimo_elemento()
inst_cola.mostrar_primer_elemento()
print(inst_cola.obtener_posicion_elemento("Luis"))
print(inst_cola.obtener_valor_por_posicion())
inst_cola.invertir_cola()
inst_cola.mostrar_elementos()
