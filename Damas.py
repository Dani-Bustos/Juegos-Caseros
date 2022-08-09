from turtle import Turtle, Screen, begin_fill
from time import sleep

#damas
def crea_matriz(filas,columnas):
    resultado = []
    for i in range(filas):
        resultado.append([celdavacia]*columnas)
    return resultado

def incializa_tablero(filas,columnas):
    resultado = []
    for i in range(filas):
     resultado.append([False]*columnas)
    return resultado


def dibuja_tablero(filas,columnas):
  for i in range(filas):
    for j in range(columnas):
        tortuga.penup()
        tortuga.goto(1*j,(i*1)+1)
        dibuja_celda(i,j)

def coloca_damas(filas,columnas):
    global simbolo, tablero
    contador = 0
    for i in range(filas):
        for j in range(columnas):
            if (i+j) % 2 == 0:
               if contador <= 24:
                simbolo[i][j] = celdanegra
                tablero[i][j] = True
                dibuja_celda(i,j)               
               elif contador >= 40:
                simbolo[i][j] = celdaroja  
                tablero[i][j] = True
                dibuja_celda(i,j)          
            contador += 1
def cuadrado(color):
    global tortuga
    tortuga.setheading(0)
    tortuga.begin_fill()
    tortuga.fillcolor(color)
    for i in range(4):
     tortuga.fd(1)
     tortuga.rt(90)
    tortuga.fd(1)
    
    tortuga.end_fill()

def dibuja_celda(y,x):
    global simbolo
    tortuga.penup()
    
    tortuga.begin_fill()
    if simbolo[y][x] == celdavacia:
       
       if (y+x) % 2 == 0: 
        cuadrado("brown")
       else:
        cuadrado("gray")
    elif simbolo[y][x] == celdapotencial:
       tortuga.goto(x+.5,y) 
       tortuga.fillcolor("green")
       tortuga.circle(.5)
    elif simbolo[y][x] == celdanegra:
       tortuga.goto(x+.5,y) 
       tortuga.fillcolor("black")
       tortuga.circle(.5)
    elif simbolo[y][x] == celdaroja:
       tortuga.goto(x+.5,y) 
       tortuga.fillcolor("red")
       tortuga.circle(.5)
    tortuga.end_fill()

def mov_Potenciales(y,x):
  global columnas,simbolo,tablero
  resultado = [] 
  if turno1:
    if y > 0:
        if x > 0 and not tablero[y-1][x-1] :
            simbolo[y-1][x-1] = celdapotencial
            resultado.append([y-1,x-1])
        if x < columnas - 1 and not tablero[y-1][x+1]:
            simbolo[y-1][x+1] = celdapotencial
            resultado.append([y-1,x+1])
    for i in range(len(resultado)):
        
        dibuja_celda(resultado[i])
  elif not turno1:
   
   if y < columnas - 1:
        if x > 0 and not tablero[y+1][x-1]:
            simbolo[y+1][x-1] = celdapotencial
            resultado.append([y+1,x-1]) 
        if x < columnas - 1 and not tablero[y-1][x+1]:
            simbolo[y-1][x+1] = celdapotencial
            resultado.append([y+1,x+1])
        if x < columnas - 1:
            simbolo[y-1][x+1] = celdapotencial
            resultado.append([y-1,y-1])
   for i in range(len(resultado)):
        
        dibuja_celda(resultado[i][0],resultado[i][1])
        

          
        
def click(x,y):
    global tablero,simbolo, turno1
    j,i = int(x) , int(y)
    if 0 <= i < len(tablero) and 0 <= j < len(tablero[0]):
      if ficha_select:
         return
      elif tablero[i][j]:
        mov_Potenciales(i,j)

 
        

filas,columnas = 8,8
celdavacia,celdaocupada = False,True
celdasinnada,celdapotencial,celdanegra,celdaroja = 0,1,2,3
turno1 = True
ficha_select = False
ficha_elegida = [None,None]
pantalla = Screen()
pantalla.setup(filas*50,columnas*50)
pantalla.screensize(filas*50,columnas*50)
pantalla.setworldcoordinates(-.5,filas+.5,columnas+.5,-.5)
pantalla.delay(0)

tortuga = Turtle()
tortuga.hideturtle()
simbolo = crea_matriz(filas,columnas)
tablero = incializa_tablero(filas,columnas)
dibuja_tablero(filas,columnas)

coloca_damas(filas,columnas)

pantalla.onclick(click)



pantalla.mainloop()