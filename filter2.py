

lista_numeros = [15, 27, 43, 10, 68, 92, 31, 76, 52, 84, 7, 19, 55, 36, 63, 88, 41, 99, 24, 59]
print(lista_numeros)

def pares(num): #hay que recordar que en py las funciones tienen que estar definidas antes de ser llamadas
    if num % 2 ==0:
        return num


ListaPares = list(filter(pares,lista_numeros)) #no hay que hacer una llamada a pares ya que en filter los argumentos se ponen en el segundo espacio
print(ListaPares)


impares = lambda num: True if num % 2 !=0 else False 

listaImpares = list(filter(impares,lista_numeros))
print(listaImpares)

# listaSeprada = listaImpares #no hay que hacer esto ya que al decir que son iguales cualquier modificación afectará a los dos
# listaSeprada[0] = "HOLA"
# print(listaImpares)
# print(listaSeprada)

listaSeprada = listaImpares.copy()
print(listaSeprada)

listaSeprada.extend(ListaPares)
print(listaSeprada)


nombres = ["Ana", "Juan", "María", "Pedro", "Luisa", "Carlos", "Sofía", "Miguel", "Laura", "Pablo"]

nombresConM = lambda nombres: True if nombres.startswith("M") else False

listaM = list(filter(nombresConM, nombres))
print(listaM)