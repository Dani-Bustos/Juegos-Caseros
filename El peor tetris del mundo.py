
def ganador(lista,jugador):
  if jugador == 1:
      simbolcheck = simb1
  else :
      simbolcheck = simb2
  for x in range(0,3):
   
    if lista[0][j]== simbolcheck and lista[1][j] == simbolcheck and lista[2][j] == simbolcheck:
         
     return True
  for x in range(0,3):
   
    if lista[x][0]== simbolcheck and lista[x][1] == simbolcheck and lista[x][2] == simbolcheck:
         
     return True
 
   
  if lista[0][0]== simbolcheck and lista[1][1] == simbolcheck and lista[2][2] == simbolcheck:
         
     return True
  if lista[0][2]== simbolcheck and lista[1][1] == simbolcheck and lista[2][0] == simbolcheck:
     return True


#simbolos  de jugador 1, 2 y vacio
simb1 = "X"
simb2 = "O"
simbvacio = "*"

lista = []
for i in range(0,3):
    lista.append([simbvacio]*3)

total = 0
turno1 = True
turno2 = False
for i in range(0,3):
 for j in range(0,3):
     print(lista[i][j], end = "  ")
 print()
valido = False
turno1 = True
turno2 = False

for turno in range(0,9):
    print("Turno del jugador 1") if turno1 else print("Turno del jugador 2")
    
    valido = False
    while valido == False:
      
     nuevajugaday = input("Dame la fila donde queres marcar(1,2,3): ")
     
     nuevajugadax = input("dame la columna donde queres marcar(1,2,3): ")
     
     if nuevajugadax in {"1","2","3"} and nuevajugaday in {"1","2","3"} and lista[int(nuevajugaday)-1][int(nuevajugadax)-1] == simbvacio:
         nuevajugaday = int(nuevajugaday) - 1
         nuevajugadax = int(nuevajugadax) - 1
         valido = True
         print("--------------------------------")
     else:
         print("Error, dame un lugar donde haya un {0}".format(simbvacio))

    if turno1:
     lista[nuevajugaday][nuevajugadax] = simb1
     turno1 = False
     turno2 = True
     
    elif turno2:
     lista[nuevajugaday][nuevajugadax] = simb2
     turno1 = True
     turno2 = False
    for i in range(0,3):
     for j in range(0,3):
      print(lista[i][j], end = "  ")
     print()
    
    if ganador(lista,1):
        print("Gano el jugador 1")
        break
    if ganador(lista,2):
        print("Gano el jugador 2")
        break

print("No hay ganadores :(") if not ganador(lista,1) and not ganador(lista,2) else None
         

