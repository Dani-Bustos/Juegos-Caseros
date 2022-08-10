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
       tortuga.goto(1*x,(y*1)+1)
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
  
  if turno1: #Rojas
    if y > 0:
        if x > 0 and not tablero[y-1][x-1] :
            simbolo[y-1][x-1] = celdapotencial
            dibuja_celda(y-1,x-1)
        if x < columnas - 1 and not tablero[y-1][x+1]:
            simbolo[y-1][x+1] = celdapotencial
            dibuja_celda(y-1,x+1)
    #Comer
    if y > 1:    
        if x > 1 and tablero[y-1][x-1] and simbolo[y-1][x-1] == celdanegra:
             simbolo[y-2][x-2] = celdapotencial
             dibuja_celda(y-2,x-2)
        if x < columnas-2 and tablero[y-1][x+1] and simbolo[y-1][x+1] == celdanegra:
             simbolo[y-2][x+2] = celdapotencial
             dibuja_celda(y-2,x+2)     
  
  elif not turno1: #negras
   
   if y < columnas - 1:
        if x > 0 and not tablero[y+1][x-1]:
            simbolo[y+1][x-1] = celdapotencial
            dibuja_celda(y+1,x-1)
        if x < columnas - 1 and not tablero[y+1][x+1]:
            simbolo[y+1][x+1] = celdapotencial
            dibuja_celda(y+1,x+1)
   #comer
   if y < columnas -2:    
        if x > 1 and tablero[y+1][x-1] and simbolo[y+1][x-1] == celdaroja:
             simbolo[y+2][x-2] = celdapotencial
             dibuja_celda(y+2,x-2)
        if x < columnas-2 and tablero[y+1][x+1] and simbolo[y+1][x+1] == celdaroja:
             simbolo[y+2][x+2] = celdapotencial
             dibuja_celda(y+2,x+2)
                  
     
        
 

def limpiar_potenciales(y,x):
  global columnas,simbolo,tablero
  
  if turno1:
    if y > 0:
        if x > 0 and not tablero[y-1][x-1] :
            simbolo[y-1][x-1] = celdasinnada
            dibuja_celda(y-1,x-1)
        if x < columnas - 1 and not tablero[y-1][x+1]:
            simbolo[y-1][x+1] = celdasinnada    
            dibuja_celda(y-1,x+1)
    if y > 1:    
        if x > 1 and tablero[y-1][x-1] and simbolo[y-1][x-1] == celdanegra:
             simbolo[y-2][x-2] = celdasinnada
             dibuja_celda(y-2,x-2)
        if x < columnas-2 and tablero[y-1][x+1] and simbolo[y-1][x+1] == celdanegra:
             simbolo[y-2][x+2] = celdasinnada
             dibuja_celda(y-2,x+2)
  elif not turno1:
   
   if y < columnas - 1:
        if x > 0 and not tablero[y+1][x-1]:
            simbolo[y+1][x-1] = celdasinnada
            dibuja_celda(y+1,x-1)
        if x < columnas - 1 and not tablero[y+1][x+1]:
            simbolo[y+1][x+1] = celdasinnada
            dibuja_celda(y+1,x+1)  
   if y < columnas -2:    
        if x > 1 and tablero[y+1][x-1] and simbolo[y+1][x-1] == celdaroja:
             simbolo[y+2][x-2] = celdasinnada
             dibuja_celda(y+2,x-2)
        if x < columnas-2 and tablero[y+1][x+1] and simbolo[y+1][x+1] == celdaroja:
             simbolo[y+2][x+2] = celdasinnada
             dibuja_celda(y+2,x+2)    

          
        
def click(x,y):
    global pantalla,tablero,simbolo, turno1,ficha_elegida,ficha_select
    pantalla.onclick(None)
    j,i = int(x) , int(y)
    if 0 <= i < len(tablero) and 0 <= j < len(tablero[0]):
      
      if ficha_select: # Si hay una ficha ya elegida
         
        if simbolo[i][j] == celdapotencial: #Me muevo a la elegida si esta en las posibles
            limpiar_potenciales(ficha_elegida[0],ficha_elegida[1])
            simbolo[i][j] = ficha_elegida[2]
            tablero[i][j] = True
            dibuja_celda(i,j)
            simbolo[ficha_elegida[0]][ficha_elegida[1]] = celdasinnada
            tablero[ficha_elegida[0]][ficha_elegida[1]] = False
            dibuja_celda(ficha_elegida[0],ficha_elegida[1])
            
            ficha_select = False

            if turno1:
                turno1 = False
            else:
                turno1 = True
        
        elif (simbolo[i][j] != celdapotencial): 
         limpiar_potenciales(ficha_elegida[0],ficha_elegida[1])
         if (i == ficha_elegida[0] and j == ficha_elegida[1]):  #limpio las potenciales al tocar de vuelta la misma
            ficha_select = False
            ficha_elegida = [None,None,None]
         elif simbolo[i][j] == ficha_elegida[2]: #cambio a la nueva ficha
            elegirficha(i,j)
        
        

      
      elif tablero[i][j]: #Elijo una ficha para moverme
        elegirficha(i,j)
        
    pantalla.onclick(click)
 
def elegirficha(i,j):
    global ficha_elegida,ficha_select,simbolo
    if simbolo[i][j] == celdanegra and not turno1:
            ficha_elegida = [i,j,celdanegra]
            ficha_select = True
            mov_Potenciales(i,j)
            
    elif simbolo[i][j] == celdaroja and turno1:
            ficha_elegida = [i,j,celdaroja]
            ficha_select = True
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
