# Buscaminas,Programa de Bustos Daniel.
from operator import truediv
from random import randrange
from tkinter.font import BOLD
from turtle import Turtle,Screen, delay
from time import sleep
def crea_matriz(filas,columnas):
    
    resultadox = []
    for i in range(filas):
        resultadox.append([False]*columnas)
    return resultadox

def pone_minas(minas,x,y): # x:y es la posicion a evitar (sirve por si el 1er click ocurre en una mina)
 
 for i in range(minas):
    [f1,c1] = [randrange(filas), randrange(columnas)]
    if not tablero[f1][c1] == True and (f1 != y and c1 != x):
        tablero[f1][c1] = True
    else:
        i - 1


def crea_numerosminas(filas,columnas):
    
    resultado = crea_matriz(filas,columnas)
    total = 0
    for i in range(filas):
        for j in range(columnas):
            total = 0
            if not tablero[i][j] :
             if j > 0 and tablero[i][j-1]:#atras
                total += 1
             if j > 0 and i > 0 and  tablero[i-1][j-1]:#atras arriba
                total += 1
             if i > 0 and tablero[i-1][j]:#arriba
                total += 1
             if i > 0 and j < (columnas - 1) and tablero[i-1][j+1]:#arriba adelante
                total += 1
             if j < (columnas - 1)and tablero[i][j+1]:#adelante
                total += 1
             if j < (columnas - 1)and i < (filas - 1 )and tablero[i+1][j+1]:#abajo adelante
                total += 1
             if i < (filas - 1 )and tablero[i+1][j]:#abajo
                total += 1
             if i < (filas - 1 ) and j > 0 and tablero[i+1][j-1]:#abajo atras
                total += 1
             else:
                resultado[i][j] = 0
             resultado[i][j] = total
            else:
                resultado[i][j] = None
    return resultado
  
def dibuja_tablero(tablero):
    for i in range(filas):
        for j in range(columnas):
            dibuja_celda(i,j)

def dibuja_celda(i,j):
    global tortuga,simbolo
    
    tortuga.penup()
    tortuga.goto(j +.5,i)
    tortuga.begin_fill()
    if simbolo[i][j] == celdaabierta :
        if tablero[i][j]:
            tortuga.fillcolor("black")
            tortuga.circle(.5)
            mostrar_minas()
            pantalla.exitonclick()
       

        elif not tablero[i][j]:
            tortuga.fillcolor("light gray")
            tortuga.circle(.5)
            tortuga.end_fill()
            if numeros[i][j] == 0:
                tortuga.end_fill()
                tortuga.pendown()
                return
            
            elif numeros[i][j] == 1:
                tortuga.color("blue")
                tortuga.goto(j+.5,i+.25)
                tortuga.write(numeros[i][j])
            elif numeros[i][j] == 2:
              tortuga.color("green")
              tortuga.goto(j+.5,i+.25)
              tortuga.write(numeros[i][j])
            elif numeros[i][j] == 3:
              tortuga.color("red")
              tortuga.goto(j+.5,i+.25) 
              tortuga.write(numeros[i][j])
            elif numeros[i][j] == 4:
              tortuga.color("purple")
              tortuga.goto(j+.5,i+.25) 
              tortuga.write(numeros[i][j])
            elif numeros[i][j] == 5:
              tortuga.color("brown")
              tortuga.goto(j+.5,i+.25) 
              tortuga.write(numeros[i][j])
            elif numeros[i][j] == 6:
              tortuga.color("turquoise")
              tortuga.goto(j+.5,i+.25) 
              tortuga.write(numeros[i][j])
            elif numeros[i][j] == 7:
              tortuga.color("black")
              tortuga.goto(j+.5,i+.25) 
              tortuga.write(numeros[i][j])
            elif numeros[i][j] == 8:
              tortuga.color("gray")
              tortuga.goto(j+.5,i+.25) 
              tortuga.write(numeros[i][j])
    elif simbolo[i][j] == bandera:
        tortuga.fillcolor("red")
        tortuga.circle(.5)        
    else:
        tortuga.fillcolor("gray")
        tortuga.circle(.5)
    tortuga.end_fill()
    tortuga.pendown()


def incializa_tablero():
    resultado = []
    for i in range(filas):
     for j in range(columnas):
      resultado.append([celdacerrada]*columnas)
    return resultado

def clic_Izquierdo(x,y):
    global simbolo,numeros,tablero
    pantalla.onclick(None)
    
    [j,i] = [int(x),int(y)]
    
    if 0 <= i <len(tablero) and 0 <= j < len(tablero[0]):
        global primeravez
        
        if primeravez: #checkea si el 1er click fue en una mina, if true la saca de ahi y pone otra mina en otro lado disntinto
            primeravez = False
            if tablero[i][j] == True:
                tablero[i][j] = False
                pone_minas(1,x,y)
        
        simbolo[i][j] = celdaabierta
        dibuja_celda(i,j)
        if numeros[i][j] == 0:
            limpiar_adyacentes(i,j)
    pantalla.onclick(clic_Izquierdo)
   

def clic_Derecho(x,y):
    global simbolo,numeros,t_banderas
    pantalla.onclick(None)

    [j,i] = [int(x),int(y)]
    
    if 0 <= i < len(tablero) and 0 <= j < len(tablero[0]):
        if simbolo[i][j] == celdacerrada:
         simbolo[i][j] = bandera
         t_banderas[i][j] = True
        elif simbolo[i][j] == bandera:
         simbolo[i][j] = celdacerrada
         t_banderas[i][j] = False
        dibuja_celda(i,j)
    if t_banderas == tablero:
        Ganar()
    else:
        pantalla.onclick(clic_Izquierdo)

def Ganar():
   
    tortuga.penup()
    tortuga.color("Orange")
    tortuga.goto(columnas/2,filas/2)
    tortuga.write("Ganaste", font=("arial",50,"bold"), align="center")
    pantalla.exitonclick()
    

    

def mostrar_minas():
            
            sleep(0.3)
            for y in range(len(tablero)):
                for x in range(len(tablero[0])):
                    if tablero[y][x]:
                        tortuga.begin_fill()
                        tortuga.fillcolor("black")
                        tortuga.goto(x+.5,y)
                        tortuga.circle(.5)
                        tortuga.end_fill()
                    elif simbolo[y][x] == bandera: #borra banderas mal puestas
                        tortuga.begin_fill()
                        tortuga.fillcolor("grey")
                        tortuga.goto(x+.5,y)
                        tortuga.circle(.5)
                        tortuga.end_fill()
            tortuga.goto(columnas/2,filas/2)
            tortuga.color("blue")
            tortuga.write("Perdiste :(", font=("arial", 50,"bold"), align= "center")       
            pantalla.exitonclick()
            


def limpiar_adyacentes(i,j):
    global columnas,filas, simbolo
    adelante = True if j < columnas - 1 else False
    abajo = True if i < filas - 1 else False
    atras = True if j > 0 else False
    arriba = True if i > 0 else False
    recursion_arriba,recursion_atrasarriba,recursion_adelantearriba,recursion_adelante,recursion_abajoadelante,recursion_abajo,recursion_abajoatras,recursion_atras = False,False,False,False,False,False,False,False
    #Las coordenadas estan al reves asi que todas las notas de arriba abajo etc.. se representan a la inversa en el tablero
    if arriba and not tablero[i-1][j] and simbolo[i-1][j] != celdaabierta: #arriba
        simbolo[i-1][j] = celdaabierta
        dibuja_celda(i-1,j)
        if numeros[i-1][j] == 0:
         recursion_arriba = True
    if arriba and atras and not tablero[i-1][j-1] and simbolo[i-1][j-1] != celdaabierta:#atras arriba
        simbolo[i-1][j-1] = celdaabierta
        dibuja_celda(i-1,j-1)       
        if numeros[i-1][j-1] == 0:
         recursion_atrasarriba = True
    if arriba and adelante and not tablero[i-1][j+1] and simbolo[i-1][j+1] != celdaabierta: #adelante arriba
        simbolo[i-1][j+1] = celdaabierta
        dibuja_celda(i-1,j+1)
        if numeros[i-1][j+1] == 0:
         recursion_adelantearriba = True
    if adelante and not tablero[i][j+1] and simbolo[i][j+1] != celdaabierta: #adelante
        simbolo[i][j+1] = celdaabierta
        dibuja_celda(i,j+1)
        if numeros[i][j+1] == 0:
         recursion_adelante = True
    if abajo and adelante and not tablero[i+1][j+1] and simbolo[i+1][j+1] != celdaabierta: #abajo adelante 
        simbolo[i+1][j+1] = celdaabierta
        dibuja_celda(i+1,j+1)
        if numeros[i+1][j+1] == 0:
         recursion_abajoadelante = True
    if abajo and not tablero[i+1][j] and simbolo [i+1][j] != celdaabierta:#abajo
        simbolo [i+1][j] = celdaabierta
        dibuja_celda(i+1,j)
        if numeros[i+1][j] == 0:
         recursion_abajo = True
    if abajo and atras and not tablero[i+1][j-1] and simbolo[i+1][j-1] != celdaabierta: #abajo atras
        simbolo [i+1][j-1] = celdaabierta
        dibuja_celda(i+1,j-1)
        if numeros[i+1][j-1] == 0:
         recursion_abajoatras = True
    if atras and not tablero[i][j-1] and simbolo[i][j-1] != celdaabierta: #atras
        simbolo[i][j-1] = celdaabierta
        dibuja_celda(i,j-1)
        if numeros[i][j-1] == 0:
         recursion_atras = True
    #La recursion solo ocurre DESPUES de haber checkeado las adyacentes de la original, para asi evitar un bucle infinito y dobles checkeos, para eso estan los booleans
    if recursion_abajo:
        limpiar_adyacentes(i+1,j)
    if recursion_abajoadelante:
        limpiar_adyacentes(i+1,j+1)
    if recursion_abajoatras:
        limpiar_adyacentes(i+1,j-1)
    if recursion_adelante:
        limpiar_adyacentes(i,j+1)
    if recursion_adelantearriba:
        limpiar_adyacentes(i-1,j+1)
    if recursion_arriba:
        limpiar_adyacentes(i-1,j)
    if recursion_atras:
        limpiar_adyacentes(i,j-1)
    if recursion_atrasarriba:
        limpiar_adyacentes(i-1,j-1)
    
    
   

#------------------Programa Principal ---------------          
filas = 14
columnas = 18
minas = 40
primeravez = True
celdacerrada,celdaabierta,bandera = 1,2,3
pantalla = Screen()
pantalla.title("Buscaminas")
pantalla.delay(0)
pantalla.setup(columnas*50,filas*50)
pantalla.screensize(columnas*50,filas*50)
pantalla.setworldcoordinates(-.5,-.5,columnas+.5,filas+.5)
tortuga = Turtle()
tortuga.hideturtle()

tablero = crea_matriz(filas,columnas)
t_banderas = crea_matriz(filas,columnas)
simbolo = incializa_tablero()
pone_minas(minas,None,None)
numeros = crea_numerosminas(filas,columnas)
dibuja_tablero(tablero)




pantalla.onclick(clic_Izquierdo)
pantalla.onclick(clic_Derecho,3)

pantalla.mainloop()

#debug
# print("Los numeros son: \n")
# for i in range(filas):
#     for j in range(columnas):
#         print(numeros[i][j], end = ",")
#     print()
# print("El tablero: \n")
# for i in range(filas):
#     for j in range(columnas):
#         print(tablero[i][j], end = ",")
#     print()
# def mostrarclic(x,y):
#     print("Fila:{0} columna :{1}".format(int(y),int(x)))
# pantalla.onclick(mostrarclic)