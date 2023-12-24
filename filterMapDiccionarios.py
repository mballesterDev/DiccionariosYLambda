empleados = {
    'empleado1':1000,
    'empleado2':2000,
    'empleado3':3000,
    'empleado4':4000
}
 
subidaSueldo = lambda empleado: "ESTE EMPLEADO TIENE UN NUEVO SEULDO " + empleado[0] #utilizando la tupla 0 nos referimos a las claves

nuevosSueldos = list(map(subidaSueldo, empleados))
print(nuevosSueldos)


porcentajeSubida = lambda empleado: empleado[1] *1.07 #de esta forma ns referimos a las defeniciones o valores

nuevosSueldos = list(map(porcentajeSubida, empleados.items()))
print()
print(nuevosSueldos)