from turtle import Turtle, Screen

def crea_matriz(filas,columnas):
 resultado = []
 for i in range(filas):
    resultado.append([celda_vacia]*columnas)
 return resultado

def incializa_tablero(filas,columnas):
 resultado = []
 for i in range(filas):
  resultado.append([False]*columnas)
 return resultado

def dibuja_simbolo(filas,columnas,simbolo):
 for i in range(filas):
    for j in range(columnas):
        dibuja_celda(i,j)

def dibuja_celda(y,x):
    global simbolo
    
    if simbolo[y][x] == celda_vacia:

pantalla = turtle.Screen()
pantalla.setup(8*filas,8*columnas)    
pantalla.screensize(8*filas + .5, 8*columnas + .5)    

tortuga = turtle.Turtle
tortuga.Hide_Turtle()
