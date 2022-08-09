# 343 Ta te ti con ia
from random import randrange
from time import sleep
from turtle import Screen,Turtle



def crea_matriz(filas,columnas):
    resultado = []
    for i in range(filas):
        resultado.append([celdavacia]*columnas)
    return resultado
     
def dibuja_tablero(filas,columnas):
    for i in range(filas):
     for j in range(columnas):
      dibuja_celda(i,j)

def dibuja_celda(i,j):
    global tortuga
    tortuga.penup()
    tortuga.begin_fill()
    tortuga.goto(j+.5,i)
    if simbolo[i][j] == celdavacia:
        tortuga.fillcolor("light gray")
        tortuga.circle(.5)
    elif simbolo[i][j] == equis:
        tortuga.fillcolor("blue")
        tortuga.circle(.5)
    elif simbolo[i][j] == circulo:
        tortuga.fillcolor("red")
        tortuga.circle(.5)
    tortuga.end_fill()

def randomizador(limite):
    return randrange(limite)
def click(x,y):
    global turno1,simbolo,tablero,pantalla,ia
    pantalla.onclick(None)
    [j,i] = [int(x), int(y)]
    if 0 <= i < len(tablero) and 0 <= j < len(tablero[0]) and  simbolo[i][j] == celdavacia:
        
        if turno1 :
            simbolo[i][j] = equis
            dibuja_celda(i,j)
            ganaste(simbolo)
        
            turno1 = False
            
        elif not ia:
            simbolo[i][j] = circulo
            dibuja_celda(i,j)
            ganaste(simbolo)
            turno1 = True
            
            
        
        if ia:
           sleep(0.4)
           CPU()
           ganaste(simbolo)   
           turno1 = True
    
    pantalla.onclick(click)
def CPU():
    i,j = Movida_IA()
    simbolo[i][j] = circulo
    dibuja_celda(i,j)
def Movida_IA():
  

    #ganar
    for i in range(3): #checkeo horizontales
     if (simbolo[i][0] == circulo and simbolo[i][1] == circulo) and simbolo[i][2] == celdavacia: 
      return (i,2)
     elif (simbolo[i][0] == circulo and simbolo[i][2] == circulo)and simbolo[i][1] == celdavacia:
      return(i,1)
     elif (simbolo[i][1] == circulo and simbolo[i][2] == circulo)and simbolo[i][0] == celdavacia:
      return(i,0)
    for j in range(3):#checkeo verticales
     if (simbolo[0][j] == circulo and simbolo[1][j] == circulo)and simbolo[2][j] == celdavacia: 
      return (2,j)
     elif (simbolo[0][j] == circulo and simbolo[2][j] == circulo)and simbolo[1][j] == celdavacia:
      return(1,j)
     elif (simbolo[1][j] == circulo and simbolo[2][j] == circulo)and simbolo[0][j] == celdavacia:
      return(0,j)
    
    #checkeo diagonal izquierda derecha
    if simbolo[0][0] == circulo and simbolo[1][1] == circulo and simbolo[2][2] == celdavacia:
        return (2,2)
    elif simbolo[0][0] == circulo and simbolo[2][2]== circulo and simbolo[1][1] == celdavacia:
        return (1,1)
    elif simbolo[1][1] == circulo and simbolo[2][2] == circulo and simbolo[0][0] == celdavacia:
        return(0,0)
    #chekeo diagonal derecha izquierda
    if simbolo[0][2] == circulo and simbolo[1][1] == circulo and simbolo[2][0] == celdavacia:
        return (2,0)
    elif simbolo[0][2] == circulo and simbolo[2][0]== circulo and simbolo[1][1] == celdavacia:
        return (1,1)
    elif simbolo[1][1] == circulo and simbolo[2][0] == circulo and simbolo[0][2] == celdavacia:
        return(0,2)
    


    
    
    #defender
    for i in range(3): #checkeo horizontales
     if (simbolo[i][0] == equis and simbolo[i][1] == equis)and simbolo[i][2] == celdavacia: 
      return (i,2)
     elif (simbolo[i][0] == equis and simbolo[i][2] == equis)and simbolo[i][1] == celdavacia:
      return(i,1)
     elif (simbolo[i][1] == equis and simbolo[i][2] == equis)and simbolo[i][0] == celdavacia:
      return(i,0)
    for j in range(3):#checkeo verticales
     if (simbolo[0][j] == equis and simbolo[1][j] == equis)and simbolo[2][j] == celdavacia: 
      return (2,j)
     elif (simbolo[0][j] == equis and simbolo[2][j] == equis)and simbolo[1][j] == celdavacia:
      return(1,j)
     elif (simbolo[1][j] == equis and simbolo[2][j] == equis)and simbolo[0][j] == celdavacia:
      return(0,j)
     #checkeo diagonal izquierda derecha
    if simbolo[0][0] == equis and simbolo[1][1] == equis and simbolo[2][2] == celdavacia:
        return (2,2)
    elif simbolo[0][0] == equis and simbolo[2][2]== equis and simbolo[1][1] == celdavacia:
        return (1,1)
    elif simbolo[1][1] == equis and simbolo[2][2] == equis and simbolo[0][0] == celdavacia:
        return(0,0)
    #chekeo diagonal derecha izquierda
    if simbolo[0][2] == equis and simbolo[1][1] == equis and simbolo[2][0] == celdavacia:
        return (2,0)
    elif simbolo[0][2] == equis and simbolo[2][0]== equis and simbolo[1][1] == celdavacia:
        return (1,1)
    elif simbolo[1][1] == equis and simbolo[2][0] == equis and simbolo[0][2] == celdavacia:
        return(0,2)
    
    #diagonales libres?
    if simbolo[0][0] == celdavacia :
        return(0,0)
    elif simbolo[0][2] == celdavacia:
        return(0,2)
    elif simbolo[2][0] == celdavacia:
        return(2,0)
    elif simbolo[2][2] == celdavacia:
        return(2,2)

    #centro
    if simbolo[1][1] == celdavacia:
        return(1,1)
    
    #lados
    if simbolo[0][1] == celdavacia:
        return(0,1)
    elif simbolo[1][0] == celdavacia:
        return(1,0)
    elif simbolo[2][1] == celdavacia:
        return(2,1)
    elif simbolo[1][2] == celdavacia:
        return(1,2)
def ganaste(lista):
  ganador = False
  if turno1 == True:
      simbolcheck = equis
      jugador = "Jugador 1"
  elif ia:
      simbolcheck = circulo
      jugador = "BOT" 
  else:
    simbolcheck = circulo
    jugador = "Jugador 2"
  for j in range(0,3):
   
    if lista[0][j]== simbolcheck and lista[1][j] == simbolcheck and lista[2][j] == simbolcheck:
     ganador = True
     terminar_programa(ganador,jugador)
  for x in range(0,3):
   
    if lista[x][0]== simbolcheck and lista[x][1] == simbolcheck and lista[x][2] == simbolcheck:
     ganador = True
     terminar_programa(ganador,jugador)
 
   
  if lista[0][0]== simbolcheck and lista[1][1] == simbolcheck and lista[2][2] == simbolcheck:
     ganador = True 
     terminar_programa(ganador,jugador)
  if lista[0][2]== simbolcheck and lista[1][1] == simbolcheck and lista[2][0] == simbolcheck:
     ganador = True
     terminar_programa(ganador,jugador)
  terminar_programa(ganador,jugador)

def terminar_programa(ganador,jugador):
  
  if ganador:
   tortuga.goto(columnas/2,filas/2)
   
   tortuga.write("Gana el {0}".format(jugador), font= ("arial",20,"bold"), align= "center")
   
            
   sleep(0.5)
   pantalla.exitonclick()
  elif celdavacia not in simbolo[0] and celdavacia not in simbolo[1] and  celdavacia not in simbolo[2] :
    tortuga.goto(columnas/2,filas/2) 
    tortuga.write("Empate",font= ("arial",20, "bold"), align= "center")
    sleep(0.5)
    pantalla.exitonclick()

#----Programa Principal----
decision = "Nada"
while decision != "B" and decision != "P":
 decision = (input("Queres jugar contra otra persona o contra un bot?(B/P): ")).upper()
 if decision == "B":
  ia = True
 else:
  ia = False
if randomizador(2) == 0:
    turno1 = True
else :
 turno1 = False



filas,columnas = 3,3
celdavacia, circulo, equis = 0,1,2

simbolo = crea_matriz(filas,columnas)
tablero = crea_matriz(filas,columnas)

pantalla = Screen()
pantalla.delay(0)
pantalla.setup(columnas*100,filas*100)
pantalla.screensize(columnas*50,filas*50)
pantalla.setworldcoordinates(-.5,filas+.5,columnas+.5,-.5)

tortuga = Turtle()
tortuga.hideturtle()



dibuja_tablero(filas,columnas)

if ia and not turno1: #1er turno de cpu
    sleep(0.4)
    CPU()
    turno1 = True

pantalla.onclick(click)

#debug
# def mostrarclic(x,y):
#print("Fila:{0} columna :{1}".format(int(y),int(x)))
#pantalla.onclick(mostrarclic)
pantalla.mainloop()