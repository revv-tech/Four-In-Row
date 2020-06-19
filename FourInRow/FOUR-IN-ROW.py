#Marco Antonio Reveiz Rojas
#Carne: 2019053583


import pygame
import time
import random
import sys , glob
import math
from pygame.locals import *

pygame.init()

#=================================================================
#FOUR IN A ROW GAME                                              =
#=================================================================


#VARIABLES GLOBALES===========================

#TABLERO

matrizTablero=[[0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0]]

#JUGADORES

player1=''
player2=''


#INDICES LISTAS

indiceColumnas=[0,1,2,3,4,5,6]
indiceFilasI=[0,1,2,3,4,5]
listaPartidasGuardadas=[]


#RANGOS FICHAS
rangoLados=7
rangoVertical=6
inicioRangoC=0
inicioRangoF=0


#RANGO INDICE FILAS
rangoIndiceFilas=6
rangoIndiceFilasInicio=0


#RANGO INDICE COLUMNAS
rangoIndiceColumnasInicio=0
rangoIndiceColumnas=7




#==============================================


#===================
#MANEJO DE ARCHIVOS=
#===================


#E: El path del archivo, un string con formato de lista
#S: Ninguna
#D: Guarda el archivo
def guardar (archivo, strLista):
     fo = open(archivo, "w")
     fo.write(strLista)
     fo.close()

#E:El path del archivo
#S:Un string con el contenido del archivo
#D: Lee el archivo
def leer (archivo):
     fo = open(archivo, "r")
     resultado = fo.read()
     fo.close()
     return resultado


#E: El path del archivo
#S:Una lista
#D:lee un archivo y hace las validaciones para colocarlo en la lista
def cargarArchivo(archivo):
     strResultado = leer(archivo)
     if strResultado != "":
          return eval(strResultado)
     else:
          return []



#================================================================================================================================================
#================================================================================================================================================
#E:No tiene
#S:No tiene
#D: Restaura todas las variables globales a default al reiniciar la partida

def restartJuego():
     global matrizTablero
     global player1
     global player2
     global indiceColumnas
     global indiceFilasI
     global listaPartidasGuardadas
     global inicioRangoC
     global inicioRangoF
     global rangoIndiceFilas
     global rangoIndiceFilasInicio
     global rangoIndiceColumnasInicio
     global rangoIndiceColumnas
     
     matrizTablero=[[0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0]]
     player1=''
     player2=''
     indiceColumnas=[0,1,2,3,4,5,6]
     indiceFilasI=[0,1,2,3,4,5]
     listaPartidasGuardadas=[]
     rangoLados=7
     rangoVertical=6
     inicioRangoC=0
     inicioRangoF=0
     numeroIndice=0
     #RANGO INDICE FILAS
     rangoIndiceFilas=6
     rangoIndiceFilasInicio=0


     #RANGO INDICE COLUMNAS
     rangoIndiceColumnasInicio=0
     rangoIndiceColumnas=7
     return


#PROCESO DEL JUEGO
     
#E: Un numero
#S: El juego
#D: Empieza el proceso del juego

def game_loop(play,turno):
     global matrizTablero
     global player1
     global player2

     
     while True:
          for i in range(len(matrizTablero)):

               #Verifica si la celda de columna ultima esta vacia y la celda de columna penultima es diferente a vacio
               if analisisFila(matrizTablero,play):
                    matrizTablero=agregaFila(matrizTablero)
                    break
               
               #Si la celda esta vacia pone la ficha (1/2) del jugador 1 o 2
               if matrizTablero[i][play] ==0:
                    matrizTablero[i][play]=turno
                    break
               
          if ganador(matrizTablero,counterFilas(matrizTablero),counterColumnas(matrizTablero)):
               if turno==1:
                    actualizadorRanking(player1)
                    return True
               if turno==2:
                    actualizadorRanking(player2)
                    return True      
               
          mostrar(matrizTablero)
          return False


#GUARDA PARTIDA=========================================================================================================================

#E: Un numero
#S: Un archivo txt
#D: Guarda la partida

def saver(turno,multiplayer):
     global matrizTablero
     global player1
     global player2
     global listaPartidasGuardadas
     
     if multiplayer:
          listaJugadores=player1+player2
          listaJuego=[player1]+[player2]+[turno]+[matrizTablero]
          guardar ((str(listaJugadores)+'.txt'), str(listaJuego))
          restartJuego()
          listaPartidasGuardadas+=[[player1]+[player2]]
          return menuJugar()
     else:
             
          listaJugadores=player1
          listaJuego=[player1]+[player2]+[turno]+[matrizTablero]
          guardar ((str(listaJugadores)+'.txt'), str(listaJuego))
          restartJuego()
          listaPartidasGuardadas+=[[player1]]
          return menuJugar()

#CARGAR PARTIDA==========================================
#E: Un string
#S: El juego
#D: Cambia las varibales globales y reactiva la partida

def partidaCargada(nombre):
     
     global matrizTablero
     global player1
     global player2
     partida=partidaCargada_aux(nombre)
     player1=partida[0]
     player2=partida[1]
     turno=partida[2]
     matrizTablero=partida[3]
     if player2=='JUAN':
          return tableroJuegoI(turno)
     else:
          return tableroJuego(turno)
     

#AUXILIAR

#E: Un string
#S: Una lista
#D: Reactiva la partida cargada

def partidaCargada_aux(nombre):
     nombrePartida=nombre+'.txt'
     return cargarArchivo(nombrePartida)

     
     
     
#TABLERO
#=================================#=================================#=================================#=================================

#Juego
#REEMPLAZADOR FICHA
#E: Una matriz y una ficha
#S: Una matriz
#D: Reemplaza la ficha en el tablero


def reemplazaFicha(M,ficha,turno):
     for i in range(len(M)):
          if analisisFila(M,ficha):
               M=agregaFila(M)
          if M[i][ficha]==0:
               M[i][ficha]=turno
               return M


#EXTIENDE TABLERO HACIA ARRIBA

#E: Una matriz
#S: No tiene
#D: Agrega una fila a la matriz
def agregaFila(M):
     
     global indiceFilasI
     global inicioRangoF
     global rangoVertical
     global matrizTablero
     counter=0
     global rangoIndiceFilas
     global rangoIndiceFilasInicio
     
     while counter<counterFilas(matrizTablero):
          contador=counterColumnas(M)
          fila=[0]*contador
          M=M+[fila]
          counter+=1
          indiceFilasI=indiceFilasI+[counterFilas(M)-1]
          
     rangoIndiceFilas+=6
     rangoIndiceFilasInicio+=6
     
     return M


#=================================#=================================#=================================#=================================
#ANALIZADOR DE FILAS LLENAS

#E: Una matriz y un numero
#S: Una matriz
#D: Analiza cada fila para verificar si esta llena

def analisisFila(M,columna):
     if columna in range(len(M[0])):
          for i in range(len(M)):
               
               if M[i][columna] == 0:
                    return False
               continue
          return True
     return True

#=================================#=================================#=================================#=================================

#EXTIENDE TABLERO COSTADOS
#E: Un string
#S: Una matriz
#D: Extiende las filas del tablero

def extendorTableroI():
     
     global matrizTablero
     global indiceColumnas
     global rangoIndiceColumnasInicio
     global rangoIndiceColumnas
     #--------------------
     
     M=[]
     contI=indiceColumnas[0]
     counter=0
     
     for fila in matrizTablero:
          M+=[[0,0,0,0,0,0,0]+fila]
     while counter<7:
          indiceColumnas = [contI-1] + indiceColumnas
          contI-=1
          counter+=1
          
     rangoIndiceColumnasInicio-=7
     rangoIndiceColumnas-=7
     
     matrizTablero = M
     
#E: Un string
#S: Una matriz
#D: Extiende las filas del tablero

def extendorTableroD():
     
     global matrizTablero
     global indiceColumnas
     
     M=[]
     contD=indiceColumnas[0]
     counter=0
     
     for fila in matrizTablero:
          M+=[fila+[0,0,0,0,0,0,0]]
     
     while counter<7:
          indiceColumnas =  indiceColumnas+[indiceColumnas[counter]+counterColumnas(matrizTablero)]
          contD+=1
          counter+=1

     matrizTablero = M

#=================================#=================================#=================================#=================================
#GANADOR

#E: Una matriz y dos numeros
#S: Una expresion booleana
#D: Determina si hay un ganador

def ganador(M,filas,columnas):
     
     for i in range(filas):
          for j in range(columnas):
               if M[i][j]!=0:
                    if filasGanador(M,i,j)or verificadorColumnas(M,i,j):
                         return True
                    if diagonalDerecha(M,i,j) or diagonalesIzquierda(M,i,j):
                         print(i,j)
                         return True
               continue
     return False              
     
#VERIFICADOR GANADOR VERTICAL

#E: Una matriz y dos numeros
#S: Una expresion booleana
#D: Verifica las filas de la matriz para determinar si hay un ganador

def filasGanador(M,i,j):
     
     for celda in range(1,4):
        try:
            if M[i][j+celda] != M[i][j]:
                return False
        except:
            return False

     return True

#VERIFICADOR GANADOR HORIZONTAL

#E: Una matriz
#S: Una expresion booleana
#D: Verifica las columnas de la matriz para determinar si hay un ganador

def verificadorColumnas(M,i,j):

    for celda in range(1,4):
        try:
            if M[i+celda][j] != M[i][j]:
                return False
        except:
            return False

    return True

#VERIFICADOR DIAGONALES

#E: Una matriz y dos numeros
#S: Una expresion booleana
#D: Revisa las diagonales de la matriz


def diagonalDerecha(M,i,j):

     for x in range(1,4):
          try:
               if M[i+x][j+x] != M[i][j]:
                    return False
          except:
               return False
          
     return True

#E: Una matriz, dos numeros
#S: Una expresion booleana
#D: Revisa las diagonales(Derecha) de la matriz

def diagonalesIzquierda(M,i,j):

     for x in range(1,4):
          try:
               if M[i+x][j-x] != M[i][j]:
                    return False
          except:
               return False
          
     return True



#=================================#=================================#=================================#=================================

#E: Una lista
#S: Un string
#D: Lee la ficha del ganador y lo retorna

def nombreJugadorGanador(turno):
     listaJugadores=creadorListaPlayers()
     
     if turno==1:
          return listaJugadores[0]
     else:
          return listaJugadores[1]

#=================================#=================================#=================================#=================================

#E: No tiene
#S: Una lista
#D: Crea una lista con los nombre de los jugadores

def creadorListaPlayers():
     global player1
     global player2
     return creadorLista_aux(player1,player2)

#=================================#=================================#=================================#=================================

#E: Dos strings
#S: Una lista
#D: Recibe los dos nombres de los jugadores

def creadorLista_aux(p1,p2):
     listaNombres=[]
     listaNombres+=[p1]+[p2]
     return listaNombres

#=================================#=================================#=================================#=================================
#E: Una matriz
#S: No tiene
#D: Imprime el tablero    
     
def mostrar(tablero):
     #tablero = tablero[::-1]
     for i in range(len(tablero)):
          for j in range(len(tablero[i])):
               print(tablero[i][j],end=' ')
          print()
     print()

#*************************************************************************************************************************************************
#*************************************************************************************************************************************************

#E: Una matriz
#S: Un numero
#D: Cuenta el numero de columnas de la matriz

def counterColumnas(M):
     counter=0
     for fila in M:
          for columna in fila:
               counter+=1
          return counter
               
#*************************************************************************************************************************************************
#*************************************************************************************************************************************************

#E: Una matriz
#S: Un numero
#D: Cuenta el numero de filas de la matriz


def counterFilas(M):
     counter=0
     for fila in M:
          counter+=1
     return counter
    
#====================================================================================================================================================================================================================================================================
#====================================================================================================================================================================================================================================================================

#IMPRIMIR RANKING
#E:No tiene
#S: Lista Ranking
#D: imprimir la lista del ranking de jugadores

def rankingJugadoresI():
     lista=ordenadorListaRanking(cargarArchivo('Record.txt'))
     x=200
     y=130
     if lista ==[]:
          return texto(x,y,'No hay jugadores registrados',20,blanco)
     for player in  lista:
          playerI=font2.render (str(player[0]),False,blanco)
          four_In_A_Row.blit(playerI,(x,y))
          
          #texto(x,y,player[0],35,blanco)
          x+=400
          #texto(x,y,str(player[1]),35,blanco)
          playerI=font2.render (str(player[1]),False,blanco)
          four_In_A_Row.blit(playerI,(x,y))
          lista=lista[1:]
          x=200
          y+=70
          continue
     return

#ACTUALIZADOR RANKING

#E: Un string
#S: No tiene
#D: Verifica que el jugador no este en el ranking, y si no esta lo agrega. Si esta le suma uno

def actualizadorRanking(nombre):
     listaRanking=cargarArchivo('Record.txt')

     for jugador in listaRanking:
          if jugador[0]== nombre:
               jugador[1]=jugador[1]+1
               return guardar ('Record.txt', str(listaRanking))
          continue
     listaRanking+=[[nombre]+[1]]
     return guardar ('Record.txt', str(listaRanking))
     
     
     
#====================================================================================================================================================================================================================================================================
#=============================================================================================================================================================================================     
     
def ordenadorListaRanking(lista):
     ranking=[]
     listaPartidas=[]
     counter=-1
     for player in lista:
          listaPartidas+=[player[1]]
          continue
     listaPartidas.sort(reverse=True)
     for num in listaPartidas:
          counter+=1
          for player in lista:
               if num==player[1]:
                    ranking+=[player]
                    lista.remove(player)
                    break
               continue
     return ranking



#====================================================================================================================================================================================================================================================================
#INTERFAZ
#====================================================================================================================================================================================================================================================================

#Crea la ventana
four_In_A_Row= pygame.display.set_mode((720, 720))

#Nombre de la ventana
pygame.display.set_caption('Four In A Row by Marco Reveiz')
reloj=pygame.time.Clock()

#Colores
blanco=(255,255,255)
negro=(0,0,0)
verde=(124,252,0)

#Adjunta las imagenes en el programa

#Boton de Vuelta
back=pygame.image.load('back.png')
#Modifica el fondo
bg=pygame.image.load('noche.png')
bg2=pygame.image.load('fondoExtra.png')
planetasExtra=pygame.image.load('fondoExtraPlaneta.png')
astro=pygame.image.load('astronauta.png')
astro2=pygame.image.load('astronauta2.png')
#Agrega el logo del programador
logo1= pygame.image.load('rev1.png')

#Establece el titulo
titulo= pygame.image.load('titulo.png')

#Agrega el nombre del programador
autor= pygame.image.load('Nombre Marco.png')
rev= pygame.image.load('rev.png')

#Agrega palabras

turnoImagen=pygame.image.load('turno.png')
rank=pygame.image.load('rank.png')
partidaN=pygame.image.load('NuevaP.png')
multi= pygame.image.load('multiB.png')
multiB= pygame.image.load('multi.png')
singleP= pygame.image.load('indi.png')
singlePB= pygame.image.load('indiB.png')
playerOne=pygame.image.load('p1.png')
playerTwo=pygame.image.load('p2.png')
overlayR=pygame.image.load('overlayR.png')
cargarP=pygame.image.load('CargarP.png')
chat=pygame.image.load('chatBubble.png')
feli=pygame.image.load('feli.png')
botonLado1=pygame.image.load('b1.png')
botonLado2=pygame.image.load('b2.png')
#Agrega el boton jugar
jugar1=pygame.image.load('nojugarbrillo.png')
jugar2=pygame.image.load('jugarbrillo.png')

#Agrega el boton cerrar
cerrarImage=pygame.image.load('cerrar.png')

#Agrega el boton record
record=pygame.image.load('record.png')

#Agrega el tablero de juego
overlay=pygame.image.load('overlay.png')

#Agrega las imagenes de las flechas a la Izquierda y Derecha
flechaI= pygame.image.load('flechaI.png')
flechaD= pygame.image.load('flechaD.png')
flechaUp=pygame.image.load('flechaArriba.png')
flechaDown=pygame.image.load('flechaAbajo.png')
#Fichas=============================================

#Planeta1
planetaVerde=pygame.image.load('PlanetaVerde.png')

#Planeta2
planetaAzul=pygame.image.load('PlanetaAzul.png')

#Planeta Gris
planetaGris=pygame.image.load('PlanetaGris.png')

#FUENTE
font = pygame.font.SysFont("Minecraft",20)
font2 = pygame.font.SysFont("Minecraft",40)
font3 = pygame.font.SysFont("Minecraft",10)
#===================================================

#=================================#=================================#=================================

# Configuracion texto
#E:  Un string, un color, un numero
#S:  No tiene
#D:  Verifica la superficie en la que se escribira el texto

def texto_aux(texto,fuente,color):
     superficie = fuente.render(texto,True,color)
     return superficie, superficie.get_rect()

#E: Tres numeros, un color, un string
#S: Un texto
#D: Crea el texto
     
def texto(x,y,texto,tamano,color):
     font = pygame.font.SysFont("Minecraft", tamano)
     superficie,rectangulo = texto_aux(texto, font,color)
     rectangulo.center= ((x),(y))
     four_In_A_Row.blit(superficie,rectangulo)

     pygame.display.update()
          
              

#=================================#=================================#=================================

#Imagenes/Titulos/Botones

#E: Dos numeros
#S: Un cambio en la ventana
#D: Acomodan la imagen en el menu
     
def logo(x,y):
     four_In_A_Row.blit(logo1,(x,y))

#E: Dos numeros
#S: Un cambio en la ventana
#D: Acomodan la imagen en el menu
     
def tituloN(x,y,title):
     four_In_A_Row.blit(title,(x,y))

#E: Dos numeros
#S: Un cambio en la ventana
#D: Acomodan la imagen en el menu

def nombreAutor(x,y):
     four_In_A_Row.blit(autor,(x,y))

#E: Dos numeros
#S: Un cambio en la ventana
#D: Acomodan la imagen en el menu

def jugarBoton1(x,y):
     four_In_A_Row.blit(jugar1,(x,y))
     
#E: Dos numeros
#S: Un cambio en la ventana
#D: Acomodan la imagen en el menu

def jugarBoton2(x,y):
     four_In_A_Row.blit(jugar2,(x,y))
     
#E: Dos numeros
#S: Un cambio en la ventana
#D: Acomodan la imagen en el menu

def recordImage(x,y):
     four_In_A_Row.blit(record,(x,y))
     
#E: Dos numeros
#S: Un cambio en la ventana
#D: Acomodan la imagen en el menu
     
def cerrarBoton(x,y):
     four_In_A_Row.blit(cerrarImage,(x,y))

#E: Dos numeros
#S: Un cambio en la ventana
#D: Acomodan la imagen en el menu

def overlayFondo(x,y):
     four_In_A_Row.blit(overlay,(x,y))

#E: Dos numeros
#S: Un cambio en la ventana
#D: Acomodan la imagen en el menu
     
def backFlecha(x,y):
     four_In_A_Row.blit(back,(x,y))

#E: Dos numeros
#S: Un cambio en la ventana
#D: Acomodan la imagen en el menu
     
def multiJugador(x,y,multi):
     four_In_A_Row.blit(multi,(x,y))

     
#=================================#=================================#=================================
#Botones
#=================================#=================================#=================================
#Boton que registra los records de los jugadores
#E: Cuatro numeros
#S: Una funcion
#D: Crea un boton

def botonRecords(x,y,ancho,altura):
     mouse= pygame.mouse.get_pos()
     click= pygame.mouse.get_pressed()

     if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
          if click[0] != 0:
               pygame.display.flip()
               return rankingJugadores()
          
#=================================#=================================#=================================
#Boton que empieza el juego
#E: Cuatro numeros
#S: Una funcion
#D: Crea un boton


def botonJugar(x,y,ancho,altura):
     mouse= pygame.mouse.get_pos()
     click= pygame.mouse.get_pressed()
     if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
          if click[0] != 0:
               pygame.display.flip()
               return menuJugar()

#=================================#=================================#=================================
#Boton que empieza el juego
#E: Cuatro numeros
#S: Una funcion
#D: Crea un boton


def botonJugar2(x,y,ancho,altura):
     mouse= pygame.mouse.get_pos()
     click= pygame.mouse.get_pressed()
     if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
          if click[0] != 0:
               pygame.display.flip()
               return tableroJuego()

#=================================#=================================#=================================
#Boton que cierra el juego
#E: Cuatro numeros
#S: Una funcion
#D: Crea un boton     
def botonCerrar(x,y,ancho,altura):
     from sys import exit
     mouse= pygame.mouse.get_pos()
     click= pygame.mouse.get_pressed()
     
     if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
          if click[0] != 0:
               pygame.mixer.music.stop()
               pygame.display.quit()
               return exit()

          
#=================================#=================================#=================================
#E: Cuatro numeros
#S: Una funcion
#D: Crea un boton 
def botonBack(x,y,ancho,altura):
     mouse= pygame.mouse.get_pos()
     click= pygame.mouse.get_pressed()
     
     if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
          if click[0] != 0:
               pygame.display.flip()
               return intro()

          
#=================================#=================================#=================================
#E: Cuatro numeros
#S: Una funcion
#D: Crea un boton 
def botonExtendorIzquierda(x,y,ancho,altura):
     mouse= pygame.mouse.get_pos()
     click= pygame.mouse.get_pressed()
     
     if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
          if click[0] != 0:
               pygame.display.flip()
               return extendorTableroI()

#=================================#=================================#=================================
#E: Cuatro numeros
#S: Una funcion
#D: Crea un boton 
def botonExtendorDerecha(x,y,ancho,altura):
     mouse= pygame.mouse.get_pos()
     click= pygame.mouse.get_pressed()
     
     if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
          if click[0] != 0:
               pygame.display.flip()
               return extendorTableroD()

          
#=================================#=================================#=================================

#E: Cuatro numeros
#S: Una funcion
#D: Crea un boton 

def botonMulti(x,y,ancho,altura):
     mouse= pygame.mouse.get_pos()
     
     click= pygame.mouse.get_pressed()
     
     if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
          if click[0] != 0:
               pygame.display.flip()
               return registroPlayers()

#=================================#=================================#=================================

#E: Cuatro numeros
#S: Una funcion
#D: Crea un boton 

def botonIndivi(x,y,ancho,altura):
     mouse= pygame.mouse.get_pos()
     
     click= pygame.mouse.get_pressed()
     
     if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
          if click[0] != 0:
               pygame.display.flip()
               return registroIndivi()

          
#=================================#=================================#=================================
#E: Cuatro numeros
#S: Una funcion
#D: Crea un boton
          
def guardarPartidaB(x,y,ancho,altura,turno,multiplayer):
     mouse= pygame.mouse.get_pos()
     click= pygame.mouse.get_pressed()
     if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
          if click[0] != 0:
               pygame.display.flip()
               return saver(turno,multiplayer)

          
#=================================#=================================#=================================
#E: Cuatro numeros
#S: Una funcion
#D: Crea un boton
          
def guardarPartidaBInicio(x,y,ancho,altura):
     mouse= pygame.mouse.get_pos()
     click= pygame.mouse.get_pressed()
     if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
          if click[0] != 0:
               pygame.display.flip()
               return partidasGuardadas()

#=================================#=================================#=================================
#E: Cuatro numeros
#S: Una funcion
#D: Crea un boton
          
def botonSubir(x,y,ancho,altura):
     
     global rangoVertical
     global inicioRangoF
     global matrizTablero
     global indiceFilasI
     global rangoIndiceFilasInicio
     global rangoIndiceFilas
     
     mouse= pygame.mouse.get_pos()
     click= pygame.mouse.get_pressed()
     if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
          if click[0] != 0:
               if rangoVertical== len(matrizTablero):
                    return
               else:
                    rangoIndiceFilasInicio-=6
                    rangoIndiceFilas-=6
                    inicioRangoF+=6
                    rangoVertical+=6

                    
#=================================#=================================#=================================
#E: Cuatro numeros
#S: Una funcion
#D: Crea un boton
          
def botonBajar(x,y,ancho,altura):
     
     global rangoVertical
     global inicioRangoF
     global rangoIndiceFilasInicio
     global rangoIndiceFilas
     
     mouse= pygame.mouse.get_pos()
     click= pygame.mouse.get_pressed()
     if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
          if click[0] != 0:
               if inicioRangoF==0:
                    return
               else:
                    rangoIndiceFilasInicio+=6
                    rangoIndiceFilas+=6
                    inicioRangoF-=6
                    rangoVertical-=6
                    
#=================================#=================================#=================================
#E: Cuatro numeros
#S: Una funcion
#D: Crea un boton
          
def botonCorrerIzq(x,y,ancho,altura):
     
     global rangoLados
     global inicioRangoC
     global rangoIndiceColumnasInicio
     global rangoIndiceColumnas
     
     mouse= pygame.mouse.get_pos()
     click= pygame.mouse.get_pressed()
     if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
          if click[0] != 0:
               if inicioRangoC==0:
                    return
               else:
                    rangoIndiceColumnasInicio-=7
                    rangoIndiceColumnas-=7
                    rangoLados-=7
                    inicioRangoC-=7
                    
#=================================#=================================#=================================
#E: Cuatro numeros
#S: Una funcion
#D: Crea un boton
          
def botonCorrerDer(x,y,ancho,altura):
     
     global matrizTablero
     global rangoLados
     global inicioRangoC
     global rangoIndiceColumnasInicio
     global rangoIndiceColumnas
     
     mouse= pygame.mouse.get_pos()
     click= pygame.mouse.get_pressed()
     if x+ancho>mouse[0]>x and y+altura> mouse[1]>y:
          if click[0] != 0:
               if rangoLados==len(matrizTablero[0]):
                    return 
               else:
                    rangoIndiceColumnasInicio+=7
                    rangoIndiceColumnas+=7
                    rangoLados+=7
                    inicioRangoC+=7
                    
               

#=================================#=================================#=================================
#Menus Juego Y Tablero
#=====================================================================================================


#INTRO AL JUEGO


def intro():
     
     pygame.mixer.music.load('music.mp3')
     pygame.mixer.music.play(-1)
     
     intro= True
     
     while intro:
          four_In_A_Row.blit(bg,(0,0))
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
          #IMAGENES Y BOTONES===========================
          mouse= pygame.mouse.get_pos()
          botonJugar(280,355,180,60)
          cerrarBoton(0,600)
          botonRecords(320,440,120,70)
          logo((270),(150))
          nombreAutor(500,150)
          tituloN((60),(50),titulo)
          botonCerrar(0,600,50,80)
          recordImage(320,450)
          
          if 270+270> mouse[0]>350 and 400> mouse[1]>350:
               jugarBoton2(270,350)
          else:
               jugarBoton1(270,350)
          #=============================================
          pygame.display.update()
          reloj.tick(5)


#=================================#=================================#=================================#=================================   
          
#E: No tiene
#S: No tiene
#D: Edita la ventana y pone otro menu a la orden del usuario

def menuJugar():
     pygame.init()
     
     
     play=True
     
     while play:
          four_In_A_Row.blit(bg,(0,0))
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
          mouse= pygame.mouse.get_pos()
          
          #IMAGENES=====================
          nombreAutor(500,150)
          backFlecha(650,660)
          botonBack(650,660,78,55)
          botonCerrar(0,650,50,80)
          cerrarBoton(0,650)
          tituloN((60),(50),titulo)
          
          if 230+300> mouse[0]>300 and 350> mouse[1]>230:
               multiJugador(230,300,multi)
          else:
               multiJugador(230,300,multiB)
               
          if 263+400> mouse[0]>263 and 500> mouse[1]>350:
               multiJugador(263,400,singlePB)
          else:
               multiJugador(263,400,singleP)
          #MULTIJUGADOR====================
          botonMulti(230,300,292,62)
          multiJugador(230,300,multi)
          #INDIVIDUAL======================
          multiJugador(263,400,singleP)
          botonIndivi(263,400,222,62)
          #CARGAR PARTIDA==================
          multiJugador(200,500,cargarP)
          guardarPartidaBInicio(200,500,350,65)
          #================================
          
          pygame.display.update()
          reloj.tick()
     
          
          
#=================================#=================================#=================================#=================================          
#E:No tiene
#S:No tiene
#D: Edita la ventana y muestra el ranking

def rankingJugadores():
     pygame.init()
     pygame.mixer.music.load('musicRecord.mp3')
     pygame.mixer.music.play(-1)
     play=True
     while play:
          four_In_A_Row.blit(bg2,(0,0))
          #IMPRESION DE JUGADORES============
          rankingJugadoresI()
          #==================================
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
               if event.type == pygame.KEYDOWN:
                    if event.key == K_RSHIFT:
                         return intro()
          #IMAGENES========================
          multiJugador(240,40,rank)
          botonCerrar(0,650,50,80)
          cerrarBoton(0,650)
          #=================================
          texto(350,20,'PARA REGRESAR INICIO PRESIONA EL SHIFT DERECHO',20,verde)
          pygame.display.update()
          reloj.tick(1)


#=================================#=================================#=================================#=================================

#PANTALLA GANADOR

#E: No tiene
#S:  No tiene
#D:  Crea la pantalla de ganador


def ganadorInterfaz(turno):
     global player1
     global player2
     global matrizTablero
     pygame.init()
     play=True
     pygame.mixer.music.load('ganador.mp3')
     pygame.mixer.music.play(-1)
     
     while play:
          
          #IMAGENES==================================
          
          four_In_A_Row.blit(bg,(0,0))
          multiJugador(300,310,astro)
          multiJugador(190,240,feli)
          #TEXTO=====================================
          
          texto(350,30,'PARA REVISAR EL RANKING DE JUGADORES',10,blanco)
          texto(350,50,'PRESIONA ESPACIO',10,blanco)
          texto(350,670,'PARA REGRESAR INICIO PRESIONA SHIFT DERECHO',20,verde)
          
          #NOMBRE GANADOR=============================
          
          if turno==1:
               texto(350,100,'¡HAS GANADO!',50,blanco)
               texto(350,190,str(player1),50,verde)
          if turno==2:
               texto(350,100,'¡HAS GANADO!',50,blanco)
               texto(350,190,str(player2),50,verde)
               
          #EVENTOS====================================
               
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
               if event.type == pygame.KEYDOWN:
                    if event.key == K_RSHIFT:
                         restartJuego()
                         return menuJugar()
                    if event.key == pygame.K_SPACE:
                         restartJuego()
                         return rankingJugadores()
                    
          #============================================
          pygame.display.update()
          reloj.tick(1)

#=================================#=================================#=================================#=================================
#REGISTRAR JUGADORES


#E: No tiene
#S: Mneu Registro
#D: Registra a los jugadores


def registroPlayers():
     pygame.init()
     play=True
     
     while play:
          #EVENTOS============================
          four_In_A_Row.blit(bg,(0,0))
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
               if event.type == pygame.KEYDOWN:
                    if event.key == K_RSHIFT:
                         return menuJugar()
          mouse= pygame.mouse.get_pos()
          #IMAGENES=========================
          multiJugador(50,40,playerOne)
          multiJugador(400,40,playerTwo)
          multiJugador(130,100,planetaVerde)
          multiJugador(490,100,planetaAzul)
          #INSTRUCCIONES====================
          texto(350,20,'INGRESA EL NOMBRE DE LOS JUGADORES:',20,blanco)
          texto(350,670,'PARA REGRESAR INICIO PRESIONA SHIFT DERECHO',20,verde)
          texto(350,250,'PRESIONA ENTER AL TERMINAR DE REGISTRAR EL NOMBRE DEL JUGADOR',15,blanco)
          texto(550,310,'INSTRUCCIONES:',20,verde)
          texto(550,350,'1. HAZ CLICK EN LA COLUMNA',15,blanco)
          texto(550,370,'PARA AGREGAR LA FICHA',15,blanco)
          texto(550,390,'2. AL TENER CUATRO EN LINEA',15,blanco)
          texto(550,410,'EN FORMA:',15,blanco)
          texto(550,430,'VERTICAL, HORIZONTAL O DIAGONAL',15,blanco)
          texto(550,450,'GANARAS AUTOMATICANTE',15,blanco)
          texto(550,480,'¡SUERTE!',15,verde)
          #=================================
          cuadroText()
          pygame.display.update()
          reloj.tick(5)


          
#AUXILIAR=======================================================================================
#E: No tiene
#S: No tiene 
#D: Muestra el tablero de juego

def registroIndivi():
     pygame.init()
     play=True
     
     while play:
          four_In_A_Row.blit(bg,(0,0))
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
               if event.key == K_RSHIFT:
                    return menuJugar()
          mouse= pygame.mouse.get_pos()
               
          #IMAGENES=========================
          
          multiJugador(240,40,playerOne)
          multiJugador(310,400,rev)
          multiJugador(330,100,planetaVerde)
          multiJugador(330,360,chat)
          
          #INSTRUCCIONES====================
          
          texto(360,20,'INGRESA TU NOMBRE:',20,blanco)
          texto(360,240,'JUGARAS CONTRA JUAN',20,blanco)
          texto(360,260,'¡SUERTE!',20,blanco)
          texto(350,650,'PRESIONA DOS VECES ENTER PARA EMPEZAR',20,verde)
          texto(350,700,'PARA REGRESAR INICIO PRESIONA SHIFT DERECHO',20,verde)
          
          #=================================

          cuadroTextIndividual()
          pygame.display.update()
          reloj.tick(5)
     
#=================================#=================================#=================================#=================================
#E: No tiene
#S: No tiene 
#D: Muestra el tablero de juego


          
def tableroJuego(turno=1):
     
     #VARIABLES GLOBALES========
     global matrizTablero
     global player1
     global player2
     global indiceColumnas
     global indiceFilasI
     #==========================
     listaJugadores=creadorLista_aux(player1,player2)
     jugada=-1
     pygame.init()
     play=True
     while play:
          
          four_In_A_Row.blit(bg,(0,0))
          for event in pygame.event.get():
               
               if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

          #MOUSE================================================
               if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                    
                    if turno==1:

                         
                         positionX=int(event.pos[0])
                         jugada= colocaJugada(positionX)
                         positionY=int(event.pos[1])
                         print(jugada)

                         
                         if jugada==None:
                              continue
                         if game_loop(jugada,turno):
                              reloj.tick(5)
                              mostrar(matrizTablero)
                              print(player1)
                              return ganadorInterfaz(turno)
                              
                         turno=2
                         break

                        
                    if turno==2:
                         positionX=int(event.pos[0])
                         jugada= colocaJugada(positionX)
                         print(jugada)
                         
                         
                         if jugada==None:
                              continue
                         if game_loop(jugada,turno):
                              reloj.tick(5)
                              mostrar(matrizTablero)
                              print(player2)
                              return ganadorInterfaz(turno)
                              
                         turno=1
                         break
          
          #IMAGENES============================================
          
          multiJugador(670,90,astro2)
          guardarPartidaB(670,90,50,50,turno,True)
          botonCerrar(0,650,50,80)
          cerrarBoton(0,650)
          overlayFondo(50,70)
          multiJugador(70,10,turnoImagen)
          multiJugador(620,10,flechaI)
          multiJugador(670,10,flechaD)
          botonExtendorIzquierda(620,10,60,60)
          botonExtendorDerecha(670,10,60,60)
          extendor=font3.render ('EXTENDER LADOS',True,blanco)
          four_In_A_Row.blit(extendor,(620,5))
          
          #FLECHAS MUEVEN TABLERO==============================
          
          #VERTICAL-----------------------------
          multiJugador(665,170,flechaUp)
          botonSubir(670,225,40,57)
          multiJugador(670,225,flechaDown)
          botonBajar(665,170,40,57)
          #LADOS--------------------------------
          multiJugador(60,600,botonLado1)
          botonCorrerIzq(60,600,50,50)
          multiJugador(590,600,botonLado2)
          botonCorrerDer(590,600,50,50)
          #-------------------------------------
          #INDICE==============================================
          printIndicesC(indiceColumnas)
          printIndicesF(indiceFilasI)
          
          #IMPRIMIR TABLERO====================================
          M=matrizTablero[::-1]
          tableroJuegoMatriz(M)
          
          #NOMBRE TURNO========================================
          if turno==1:
               texto(400,30,player1,30,blanco)
          if turno==2:
               texto(400,30,player2,30,blanco)
          #====================================================
          pygame.display.update()
          reloj.tick(5)


#AUXILIAR=======================================================================================
#E:  Una matriz
#S:  Una imagen
#D:  Dibuja las fichas en el tablero conforme pasa el juego


def tableroJuegoMatriz(M):
     #VARIABLES GLOBALES------
     global inicioRangoC
     global inicioRangoF
     global rangoLados
     global rangoVertical
     global numeroIndice
     #------------------------
     
     
     for i in range(0,7):
          for j in range(0,6):
               multiJugador(int(i*60+60/2+120),int(j*60+60/2+160),planetaGris)
               
     
     for i in range(inicioRangoC,rangoLados):
          for j in range(inicioRangoF,rangoVertical):

               #TURNO 1--------------------------------------------------------------------------------------------------
               
               if M[j][i]==1:
                    if i in range(0,7) and j in range(0,6):
                         multiJugador(int(i*60+60/2+120),int(j*60+60/2+160),planetaVerde)
                    
                    else:
                         #-----------------------------------------
                         #FILAS
                         nuevoRangoColumna=i
                         nuevoRangoColumna=tableroJuegoMatriz_aux(i)
                         #COLUMNAS
                         nuevoRangoFila=j
                         nuevoRangoFila=tableroJuegoMatriz_aux_2(j)
                         #-----------------------------------------
                         multiJugador(int(nuevoRangoColumna*60+60/2+120),int(nuevoRangoFila*60+60/2+160),planetaVerde)
                         
               #TURNO 2---------------------------------------------------------------------------------------------------
               
               if M[j][i]==2:
                    if i in range(0,7) and j in range(0,6):
                         multiJugador(int(i*60+60/2+120),int(j*60+60/2+160),planetaAzul)
                    
                    else:
                         #-----------------------------------------
                         #FILAS
                         nuevoRangoColumna=i
                         nuevoRangoColumna=tableroJuegoMatriz_aux(i)
                         #COLUMNAS
                         nuevoRangoFila=j
                         nuevoRangoFila=tableroJuegoMatriz_aux_2(j)
                         #-----------------------------------------
                         multiJugador(int(nuevoRangoColumna*60+60/2+120),int(nuevoRangoFila*60+60/2+160),planetaAzul)
                         
               #----------------------------------------------------------------------------------------------------------          


#--------------------------------------------
#AUXILIAR                        
#E: Un numero
#S: Un numero
#D: Retorna un numero en el rango adecuado
               
def tableroJuegoMatriz_aux(num):
     while num not in range(0,7):
          num=num-7
     return num

#---------------------------------------------
#AUXILIAR
#E: Un numero
#S: Un numero
#D: Retorna un numero en el rango adecuado
               
def tableroJuegoMatriz_aux_2(num):
     while num not in range(0,6):
          num=num-6
          
     return num



#AUXILIAR=======================================================================================
#E:Un numero
#S:Un numero
#D: Verifica la posicion del click y recorna jugada(columna) en donde quiere colocar la ficha


def colocaJugada(num):
     global inicioRangoC
     global rangoLados
     columna=0
     if num<570 and num>150:
          if 150<num<210:
               columna = 0
          elif  210<num<270:
               columna = 1
          elif 270<num<330:
               columna = 2
          elif 330<num<390:
               columna = 3
          elif 390<num<450:
               columna = 4
          elif 450<num<510:
               columna = 5
          elif 510<num<570:
               columna = 6
          while columna not in range(inicioRangoC,rangoLados):
               columna += 7
          return columna
     else:
          return  

#AUXILIAR INDICE COLUMNAS
#E: Una lista
#S: El indice del juego
#D: Imprime el indice de las columnas en el juego

def printIndicesC(indices):
     
     global rangoIndiceColumnasInicio
     global rangoIndiceColumnas
     
     x = 179
     y= 150
     corredorX=0
     columna= 0
     nuevoX=0
     
     for columna in indices:
          while columna in range(rangoIndiceColumnasInicio,rangoIndiceColumnas):
               if nuevoX>539:
                    return
               
               if columna==rangoIndiceColumnasInicio:
                    numero=font.render (str(columna),False,blanco)
                    four_In_A_Row.blit(numero,(x,y))
                    
                    
               elif columna!=rangoIndiceColumnas:
                    corredorX=corredorX+60
                    nuevoX=corredorX+x
                    numero=font.render (str(columna),False,blanco)
                    four_In_A_Row.blit(numero,(nuevoX,y))
                    
                    
               break    
          continue
     return
               

    
#AUXILIAR INDICE FILAS
#E: Una lista
#S: El indice del juego
#D: Imprime el indice de las filas en el juego

def printIndicesF(indices):
     
     global rangoIndiceFilasInicio
     global rangoIndiceFilas
     
     font = pygame.font.SysFont("Minecraft",20)
     x = 120
     y= 510
     nuevoY=0
     corredorY=0

     for fila in indices:
          while fila in range(rangoIndiceFilasInicio,rangoIndiceFilas):
               if nuevoY>550 and nuevoY<210:
                    return
               if fila==rangoIndiceFilasInicio:
                    numero=font.render (str(indiceFilasI[fila]),False,blanco)
                    four_In_A_Row.blit(numero,(x,y))
                    
               elif fila!=rangoIndiceFilas:
                    corredorY=corredorY-60
                    nuevoY=corredorY+y
                    numero=font.render (str(indices[fila]),False,blanco)
                    four_In_A_Row.blit(numero,(x,nuevoY))
               break    
          continue
     return
             

#INDIVIDUAL========================================================================================


#E: No tiene
#S: El tablero de juego
#D: Proyecta en la pantalla el tablero de juego 

def tableroJuegoI(turno=1):
     
     #VARIABLES GLOBALES========
     
     global matrizTablero
     global player1
     global player2
     
     #==========================
     
     listaJugadores=creadorLista_aux(player1,player2)
     jugada=-1
     pygame.init()
     play=True
     while play:
          
          four_In_A_Row.blit(bg,(0,0))
          for event in pygame.event.get():
               
               if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

          #MOUSE================================================
               if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                    
                    
                    if turno==1:

                         
                         positionX=int(event.pos[0])
                         jugada= colocaJugada(positionX)
                         jugadaAnterior=colocaJugada(positionX)
                         positionY=int(event.pos[1])
                         print(jugada)

                         
                         if jugada==None:
                              continue
                         if game_loop(jugada,turno):
                              reloj.tick(5)
                              mostrar(matrizTablero)
                              print(player1)
                              return ganadorInterfaz(turno)
                         turno=2
                         break
          
                    
          
          #IMAGENES============================================
          multiJugador(670,90,astro2)
          guardarPartidaB(670,90,50,50,turno,False)
          botonCerrar(0,650,50,80)
          cerrarBoton(0,650)
          overlayFondo(50,70)
          multiJugador(70,10,turnoImagen)
          multiJugador(620,10,flechaI)
          multiJugador(670,10,flechaD)
          extendor=font3.render ('EXTENDER LADOS',True,blanco)
          four_In_A_Row.blit(extendor,(620,5))
          botonExtendorIzquierda(620,10,60,60)
          botonExtendorDerecha(670,10,60,60)
          multiJugador(665,170,flechaUp)
          multiJugador(670,225,flechaDown)
          multiJugador(60,600,botonLado1)
          botonCorrerIzq(60,600,50,50)
          multiJugador(590,600,botonLado2)
          botonCorrerDer(590,600,50,50)
          #IMPRIMIR TABLERO====================================
          
          M= matrizTablero[::-1]
          tableroJuegoMatriz(M)

          #INDICE================================
          printIndicesC(indiceColumnas)
          printIndicesF(indiceFilasI)
          
          #FLECHAS MUEVEN TABLERO==============================
          
          #VERTICAL-----------------------------
          multiJugador(665,170,flechaUp)
          botonSubir(670,225,40,57)
          multiJugador(670,225,flechaDown)
          botonBajar(665,170,40,57)
          #LADOS--------------------------------
          multiJugador(60,600,botonLado1)
          botonCorrerIzq(60,600,50,50)
          multiJugador(590,600,botonLado2)
          botonCorrerDer(590,600,50,50)
          #-------------------------------------
          
          #NOMBRE TURNO=======================================
          
          if turno==1:
               texto(400,30,player1,30,blanco)
          if turno==2:
               texto(400,30,player2,30,blanco)

          #TURNO DE JUAN====================================
          if turno==2:
               jugada= random.randint(0,jugadaAnterior)
               pygame.time.wait(500)
               if jugada==None:
                    continue
               if game_loop(jugada,turno):
                    reloj.tick(5)
                    mostrar(matrizTablero)
                    print(player2)
                    return ganadorInterfaz(turno)
                              
               turno=1    
          #======================================
          pygame.display.update()
          reloj.tick(5)


#AUXILIAR=======================================================================================
#E:  Una matriz
#S:  Una imagen
#D:  Dibuja las fichas en el tablero conforme pasa el juego


def tableroJuegoMatrizI(M):
     global inicioRangoC
     global inicioRangoF
     global rangoLados
     global rangoVertical
     global numeroIndice

     for i in range(0,7):
          for j in range(0,6):
               multiJugador(int(i*60+60/2+120),int(j*60+60/2+160),planetaGris)
               
     
     for i in range(inicioRangoC,rangoLados):
          for j in range(inicioRangoF,rangoVertical):
               #print(rangoLados)
               if M[j][i]==1:
                    if i in range(0,7):
                         multiJugador(int(i*60+60/2+120),int(j*60+60/2+160),planetaVerde)
                    else:
                         nuevoRango=i
                         nuevoRango=tableroJuegoMatriz_aux(i)
                         multiJugador(int(nuevoRango*60+60/2+120),int(j*60+60/2+160),planetaVerde)
                         
               if M[j][i]==2:
                    if i in range(0,7):
                         multiJugador(int(i*60+60/2+120),int(j*60+60/2+160),planetaAzul)
                    else:
                         nuevoRango=i
                         nuevoRango=tableroJuegoMatriz_aux(i)
                         multiJugador(int(nuevoRango*60+60/2+120),int(j*60+60/2+160),planetaAzul)
                   

#PARTIDAS GUARDADAS=======================================================================================
#E: No tiene
#S: No tiene
#D:  Le pregunta al jugador el nombre de los jugadores que fueron parte de la partida
          

def partidasGuardadas():
     
     pygame.init()
     
     pygame.mixer.music.load('naruto.mp3')
     pygame.mixer.music.play(-1)
     
     new= True
     while new: 
          four_In_A_Row.blit(bg,(0,0))
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
          nombreAutor(500,150)
          tituloN((60),(50),titulo)
              
          #INSTRUCCIONES====================
          texto(350,230,'INGRESA EL NOMBRE DE LOS JUGADORES JUNTOS SIN ESPACIOS:',15,blanco)
          texto(350,245,'SI SOLO ES UN JUGADOR, SOLO ESCRIBE SU NOMBRE',15,blanco)
          texto(350,265,'RESPETA EL USO DE MAYUSCULAS',15,verde)
          texto(350,670,'PRESIONA ENTER PARA EMPEZAR',20,verde)
          texto(350,700,'PARA REGRESAR INICIO PRESIONA SHIFT DERECHO',20,verde)
          cuadroTextPartidasCargadas()
          pygame.display.update()
          reloj.tick(5)
   
#=======================================================================================================================================


#INPUTS

#MULTIJUGADOR

#E: No tiene
#S: El juego
#D: Registra a los jugadores
                    
def cuadroText():
     import pygame as pg

     
     pg.init()
     COLOR_INACTIVE = pg.Color('lightskyblue3')
     COLOR_ACTIVE = pg.Color('whitesmoke')
     FONT = pg.font.SysFont('Minecraft', 32)
     

     class InputBox:
          
         def __init__(self, x, y, w, h, text=''):
             self.rect = pg.Rect(x, y, w, h)
             self.color = COLOR_INACTIVE
             self.text = text
             self.txt_surface = FONT.render(text, True, self.color)
             self.active = False


         def handle_event(self, event):
               global player1
               global player2
               if event.type == pg.MOUSEBUTTONDOWN:
                    if self.rect.collidepoint(event.pos):
                         self.active = not self.active
                    else:
                         self.active = False
                    self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
               if event.type == pg.KEYDOWN:
                    if event.key == K_RSHIFT:
                         matrizTablero=[[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0]]
                         player1=''
                         player2=''
                         return menuJugar()
                    if self.active:
                         if event.key == pg.K_RETURN: 
                              if player1==player2:
                                   player1=self.text
                              else:
                                   player2=self.text
                                   return tableroJuego()
                         elif event.key == pg.K_BACKSPACE:
                              self.text = self.text[:-1]
                         else:
                              self.text += event.unicode
                         self.txt_surface = FONT.render(self.text, True, self.color)


         def update(self):
             width = max(200, self.txt_surface.get_width()+10)
             self.rect.w = width


         def draw(self, screen):
             four_In_A_Row.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
             pg.draw.rect(four_In_A_Row, self.color, self.rect, 2)



     def main():
          clock = pg.time.Clock()
          input_box1 = InputBox(60, 170, 140, 32)
          input_box2 = InputBox(420, 170, 140, 32)
          input_boxes = [input_box1, input_box2]
          
          done = False
          while not done:
               for event in pg.event.get():
                    if event.type == pg.QUIT:
                         done = True
                    for box in input_boxes:
                         box.handle_event(event)

               for box in input_boxes:
                    box.update()

             
               for box in input_boxes:
                    box.draw(four_In_A_Row)
               
               pg.display.flip()
               clock.tick(5)
          pg.display.quit()
          
               
               

     if __name__ == '__main__':
          main()
          pg.quit()

#===========================================================================================================================================================

#INDIVIDUAL
#E: No tiene
#S: El juego
#D: Registra a los jugadores
                    
def cuadroTextIndividual():
     import pygame as pg

     
     pg.init()
     COLOR_INACTIVE = pg.Color('lightskyblue3')
     COLOR_ACTIVE = pg.Color('whitesmoke')
     FONT = pg.font.SysFont('Minecraft', 32)
     

     class InputBox:
          
         def __init__(self, x, y, w, h, text=''):
             self.rect = pg.Rect(x, y, w, h)
             self.color = COLOR_INACTIVE
             self.text = text
             self.txt_surface = FONT.render(text, True, self.color)
             self.active = False


         def handle_event(self, event):
               global player1
               global player2
               if event.type == pg.MOUSEBUTTONDOWN:
                    if self.rect.collidepoint(event.pos):
                         self.active = not self.active
                    else:
                         self.active = False
                    self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
               if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RSHIFT:
                         matrizTablero=[[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0]]
                         player1=''
                         player2=''
                         return menuJugar()
                    if self.active:
                         
                         if event.key == pg.K_RETURN: 
                              if player1==player2:
                                   player1=self.text
                              else:
                                   player2='JUAN'
                                   return tableroJuegoI()
                         elif event.key == pg.K_BACKSPACE:
                              self.text = self.text[:-1]
                         else:
                              self.text += event.unicode
                         self.txt_surface = FONT.render(self.text, True, self.color)


         def update(self):
             width = max(200, self.txt_surface.get_width()+10)
             self.rect.w = width


         def draw(self, screen):
             four_In_A_Row.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
             pg.draw.rect(four_In_A_Row, self.color, self.rect, 2)



     def main():
          clock = pg.time.Clock()
          input_box1 = InputBox(260, 170, 140, 32)
          input_box2 = InputBox(900, 170, 140, 32)
          input_boxes = [input_box1, input_box2]
          
          done = False
          while not done:
               for event in pg.event.get():
                    if event.type == pg.QUIT:
                         done = True
                    for box in input_boxes:
                         box.handle_event(event)

               for box in input_boxes:
                    box.update()

             
               for box in input_boxes:
                    box.draw(four_In_A_Row)
               
               pg.display.flip()
               clock.tick(5)
          pg.display.quit()
          
               
               

     if __name__ == '__main__':
          main()
          pg.quit()

#===========================================================================================================================================================

          

#E: No tiene
#S: El juego
#D: Busca a los jugadores
          
def cuadroTextPartidasCargadas():
     import pygame as pg

     
     pg.init()
     COLOR_INACTIVE = pg.Color('lightskyblue3')
     COLOR_ACTIVE = pg.Color('whitesmoke')
     FONT = pg.font.SysFont('Minecraft', 32)
     

     class InputBox:
          
         def __init__(self, x, y, w, h, text=''):
             self.rect = pg.Rect(x, y, w, h)
             self.color = COLOR_INACTIVE
             self.text = text
             self.txt_surface = FONT.render(text, True, self.color)
             self.active = False


         def handle_event(self, event):
               global player1
               global player2
               if event.type == pg.MOUSEBUTTONDOWN:
                    if self.rect.collidepoint(event.pos):
                         self.active = not self.active
                    else:
                         self.active = False
                    self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
               if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RSHIFT:
                         return menuJugar()
                    if self.active:
                         
                         if event.key == pg.K_RETURN: 
                              if player1==player2:
                                   player1=self.text
                                   nombre=player1+player2
                                   return partidaCargada(nombre)
                         elif event.key == pg.K_BACKSPACE:
                              self.text = self.text[:-1]
                         else:
                              self.text += event.unicode
                         self.txt_surface = FONT.render(self.text, True, self.color)


         def update(self):
             width = max(200, self.txt_surface.get_width()+10)
             self.rect.w = width


         def draw(self, screen):
             four_In_A_Row.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
             pg.draw.rect(four_In_A_Row, self.color, self.rect, 2)



     def main():
          clock = pg.time.Clock()
          input_box1 = InputBox(260, 300, 190, 32)
          input_box2 = InputBox(900, 170, 140, 32)
          input_boxes = [input_box1, input_box2]
          
          done = False
          while not done:
               for event in pg.event.get():
                    if event.type == pg.QUIT:
                         done = True
                    for box in input_boxes:
                         box.handle_event(event)

               for box in input_boxes:
                    box.update()

             
               for box in input_boxes:
                    box.draw(four_In_A_Row)
               
               pg.display.flip()
               clock.tick(5)
          pg.display.quit()
          
               
               

     if __name__ == '__main__':
          main()
          pg.quit()



     
ganadorInterfaz(1)

