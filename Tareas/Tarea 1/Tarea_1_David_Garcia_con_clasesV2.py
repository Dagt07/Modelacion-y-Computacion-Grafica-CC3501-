import pyglet
import numpy as np
import random
from pyglet.app import run

window= pyglet.window.Window(1200,720,"Tarea 1 David Garcia Naves y estrellas",resizable=False, visible=True)

#Creamos Batch de las estrellas
estrellas= pyglet.graphics.Batch()

class StarClass:
    def __init__(self,DespX=0, DespY=0):

        #Construimos la lista para dar aletoriedad a las estrellas, es decir, la separacion
        a=[]
        for k in range(0,14):
            a.append(random.randint(200,400))

        #Creamos el body de cada estrella
        self.body= pyglet.shapes.Star(x=600+DespX, y=960+DespY-a[0], outer_radius=12, inner_radius=5, rotation=0, num_spikes=5,color=(255,255,0),batch=estrellas)
        self.body2= pyglet.shapes.Star(x=600+DespX, y=940+DespY-a[1], outer_radius=12, inner_radius=5, rotation=0, num_spikes=5,color=(255,255,0),batch=estrellas)
        self.body3= pyglet.shapes.Star(x=600+DespX, y=920+DespY-a[2], outer_radius=12, inner_radius=5, rotation=0, num_spikes=5,color=(255,255,0),batch=estrellas)
        self.body4= pyglet.shapes.Star(x=600+DespX, y=900+DespY-a[3], outer_radius=12, inner_radius=5, rotation=0, num_spikes=5,color=(255,255,0),batch=estrellas)
        self.body5= pyglet.shapes.Star(x=600+DespX, y=880+DespY-a[4], outer_radius=12, inner_radius=5, rotation=0, num_spikes=5,color=(255,255,0),batch=estrellas)
        self.body6= pyglet.shapes.Star(x=600+DespX, y=860+DespY-a[5], outer_radius=12, inner_radius=5, rotation=0, num_spikes=5,color=(255,255,0),batch=estrellas)
        self.body7= pyglet.shapes.Star(x=600+DespX, y=840+DespY-a[6], outer_radius=12, inner_radius=5, rotation=0, num_spikes=5,color=(255,255,0),batch=estrellas)
        self.body8= pyglet.shapes.Star(x=600+DespX, y=840+DespY-a[7], outer_radius=12, inner_radius=5, rotation=0, num_spikes=5,color=(255,255,0),batch=estrellas)
        self.body9= pyglet.shapes.Star(x=600+DespX, y=820+DespY-a[8], outer_radius=12, inner_radius=5, rotation=0, num_spikes=5,color=(255,255,0),batch=estrellas)
        self.body10= pyglet.shapes.Star(x=600+DespX, y=800+DespY-a[9], outer_radius=12, inner_radius=5, rotation=0, num_spikes=5,color=(255,255,0),batch=estrellas)
        self.body11= pyglet.shapes.Star(x=600+DespX, y=780+DespY-a[10], outer_radius=12, inner_radius=5, rotation=0, num_spikes=5,color=(255,255,0),batch=estrellas)
        self.body12= pyglet.shapes.Star(x=600+DespX, y=760+DespY-a[11], outer_radius=12, inner_radius=5, rotation=0, num_spikes=5,color=(255,255,0),batch=estrellas)
        self.body13= pyglet.shapes.Star(x=600+DespX, y=740+DespY-a[12], outer_radius=12, inner_radius=5, rotation=0, num_spikes=5,color=(255,255,0),batch=estrellas)
        self.body14= pyglet.shapes.Star(x=600+DespX, y=720+DespY-a[13], outer_radius=12, inner_radius=5, rotation=0, num_spikes=5,color=(255,255,0),batch=estrellas)

        #parametros de movimiento
        self.advance= 2
        self.rotate= 0
        self.movement_speed = 2
        self.vx = 1
        self.vy = 1
    
    def update(self,DespY=0):
        
        listaBodys= [self.body,self.body2,self.body3,self.body4,self.body5,self.body6,self.body7,self.body8,self.body9,self.body10,
                     self.body11,self.body12,self.body13,self.body14]
        
        i= 0
        j=1
        for body in listaBodys: 
            if body.y <=0: #Condición que evalua si salen de pantalla para updatear arriba
                
                a= []
                for k in range(0,14): #Para generar aleatoriedad entre estrellas
                    a.append(random.randint(200,400))

                #for body in listaBodys: #Basicamente con este ciclo hago el posicionamiento arriba nuevamente de las estrellas self.body.y = 960+DespY-a[0], #self.body2.y = 940+DespY-a[1], ....
                i = j*30
                body.y = 960-i+DespY-a[j-1] 
                j += 1

        #Creamos un array con los bodys (cada estrella) y los movemos accediendo a su parametro .y
        for body in listaBodys:
            body.y -= self.vy*self.advance*self.movement_speed
        pass

#Creamos objetos tipo StarClass dandole desplazamientos a cada uno para orientarlos en la ventana
estrella_1= StarClass(-500,DespY=300)
estrella= StarClass(-400,DespY=300)
estrella1= StarClass(-300,DespY=300)
estrella2= StarClass(-200,DespY=300)
estrella3= StarClass(-100,DespY=300)
estrella4= StarClass(DespY=300)
estrella5= StarClass(100,DespY=300)
estrella6= StarClass(200,DespY=300)
estrella7= StarClass(300,DespY=300)
estrella8= StarClass(400,DespY=300)
estrella9= StarClass(500,DespY=300)

#Creamos Batch de la nave
nave= pyglet.graphics.Batch()

class Nave:
    def __init__(self,Xtamano=1,DespX=0, DespY=0):#Xtamano #Para ponderar el tamaño de las figuras #DespX Desplaza en X und la nave #DespY Desplaza en Y und la nave
        
        #Construimos la nave, lo que vendría siendo como nuestro main body
        #Cuerpo Central Nave
        self.cuerpo_central_izq= pyglet.shapes.Triangle(Xtamano*100+DespX,Xtamano*90+DespY,Xtamano*90+DespX,Xtamano*90+DespY,Xtamano*100+DespX,Xtamano*120+DespY,color=(6, 161, 243),batch=nave) 
        self.cuerpo_central_der= pyglet.shapes.Triangle(Xtamano*100+DespX,Xtamano*90+DespY,Xtamano*110+DespX,Xtamano*90+DespY,Xtamano*100+DespX,Xtamano*120+DespY,color=(6, 161, 243),batch=nave)
        self.linea_central= pyglet.shapes.Line(Xtamano*100+DespX,Xtamano*90+DespY,Xtamano*100+DespX,Xtamano*120+DespY,color=(0,0,0),batch=nave)
        self.cuerpo_central2_izq= pyglet.shapes.Triangle(Xtamano*100+DespX,Xtamano*90+DespY,Xtamano*90+DespX,Xtamano*90+DespY,Xtamano*100+DespX,Xtamano*70+DespY,color=(6, 161, 243),batch=nave)
        self.cuerpo_central2_der= pyglet.shapes.Triangle(Xtamano*100+DespX,Xtamano*90+DespY,Xtamano*110+DespX,Xtamano*90+DespY,Xtamano*100+DespX,Xtamano*70+DespY,color=(6, 161, 243),batch=nave)
        self.linea_central_2= pyglet.shapes.Line(Xtamano*100+DespX,Xtamano*90+DespY,Xtamano*100+DespX,Xtamano*70+DespY,color=(0,0,0),batch=nave)
        self.cabina_izq= pyglet.shapes.Triangle(Xtamano*100+DespX,Xtamano*110+DespY,Xtamano*97+DespX,Xtamano*110+DespY,Xtamano*100+DespX,Xtamano*120+DespY,color=(255, 255, 0),batch=nave)
        self.cabina_der= pyglet.shapes.Triangle(Xtamano*100+DespX,Xtamano*110+DespY,Xtamano*103+DespX,Xtamano*110+DespY,Xtamano*100+DespX,Xtamano*120+DespY,color=(255, 255, 0),batch=nave)

        #Motor Nave
        self.llama_externa_izq= pyglet.shapes.Triangle(Xtamano*98+DespX,Xtamano*79+DespY,Xtamano*89+DespX,Xtamano*79+DespY,Xtamano*95+DespX,Xtamano*55+DespY,color=(255,0,0),batch=nave)
        self.llama_externa_der= pyglet.shapes.Triangle(Xtamano*102+DespX,Xtamano*79+DespY,Xtamano*111+DespX,Xtamano*79+DespY,Xtamano*105+DespX,Xtamano*55+DespY,color=(255,0,0),batch=nave)
        self.llama_interna_izq= pyglet.shapes.Triangle(Xtamano*97+DespX,Xtamano*85+DespY,Xtamano*90+DespX,Xtamano*85+DespY,Xtamano*95+DespX,Xtamano*65+DespY,color=(219,147,3),batch=nave)
        self.llama_interna_der= pyglet.shapes.Triangle(Xtamano*103+DespX,Xtamano*85+DespY,Xtamano*110+DespX,Xtamano*85+DespY,Xtamano*105+DespX,Xtamano*65+DespY,color=(219,147,3),batch=nave)

        #Alas Nave
        self.ala_izq= pyglet.shapes.Triangle(Xtamano*95+DespX,Xtamano*85+DespY,Xtamano*80+DespX,Xtamano*90+DespY,Xtamano*60+DespX,Xtamano*60+DespY,color=(6,161,243),batch=nave)
        self.ala_der= pyglet.shapes.Triangle(Xtamano*105+DespX,Xtamano*85+DespY,Xtamano*120+DespX,Xtamano*90+DespY,Xtamano*140+DespX,Xtamano*60+DespY,color=(6,161,243),batch=nave)

        #Alerones 
        self.aleron_central_izq= pyglet.shapes.Triangle(Xtamano*95+DespX,Xtamano*85+DespY,Xtamano*85+DespX,Xtamano*85+DespY,Xtamano*85+DespX,Xtamano*105+DespY,color=(24,91,181),batch=nave)
        self.aleron_central_der= pyglet.shapes.Triangle(Xtamano*105+DespX,Xtamano*85+DespY,Xtamano*115+DespX,Xtamano*85+DespY,Xtamano*115+DespX,Xtamano*105+DespY,color=(24,91,181),batch=nave)
        self.aleron_central_izq2= pyglet.shapes.Triangle(Xtamano*95+DespX,Xtamano*85+DespY,Xtamano*85+DespX,Xtamano*85+DespY,Xtamano*85+DespX,Xtamano*65+DespY,color=(24,91,181),batch=nave)
        self.aleron_central_der2= pyglet.shapes.Triangle(Xtamano*105+DespX,Xtamano*85+DespY,Xtamano*115+DespX,Xtamano*85+DespY,Xtamano*115+DespX,Xtamano*65+DespY,color=(24,91,181),batch=nave)

        self.advance = 0
        self.rotate = 0

#Creamos objetos tipo Nave dandole desplazamientos a cada uno para orientarlos en la ventana
nave1= Nave(2,100,50) #Le ponderamos el tamaño por 2
nave2= Nave(2,400,150) #La desplazamos en X DespX=300 und, en Y DespY= 100 und
nave3= Nave(2,700,50)
nave4= Nave(2,400,-50)

#Creamos Batch y Clase Asteroide
asteroides= pyglet.graphics.Batch()

class AsteroideClass:
    def __init__(self,Xtamano=1,DespX=0, DespY=0):
        self.body = pyglet.shapes.Circle(Xtamano*100+DespX,Xtamano*600+DespY,radius=50, color=(140,136,133),batch=asteroides)
        self.crater1= pyglet.shapes.Circle(Xtamano*120+DespX,Xtamano*600+DespY,radius=13, color=(30,16,16),batch=asteroides)
        self.crater2= pyglet.shapes.Circle(Xtamano*85+DespX,Xtamano*620+DespY,radius=16, color=(30,16,16),batch=asteroides)
        self.crater3= pyglet.shapes.Circle(Xtamano*98+DespX,Xtamano*580+DespY,radius=9, color=(30,16,16),batch=asteroides)
        self.crater4= pyglet.shapes.Circle(Xtamano*72+DespX,Xtamano*570+DespY,radius=13, color=(30,16,16),batch=asteroides)
        
        self.advance= 3
        self.rotate= 1
        self.rotation_speed = np.pi
        self.movement_speed = 2
        self.vx = 1
        self.vy = 1
    
    def update(self,DespY=0):   #agregar rotación a asteorides

        if self.body.y <=0 and self.crater1.y <=0 and self.crater2.y <=0 and self.crater3.y and self.crater4.y <=0:
            self.body.y = 600+200
            self.crater1.y= 600+200
            self.crater2.y= 620+200
            self.crater3.y= 580+200
            self.crater4.y= 570+200
        
        self.body.y -= self.vy*self.advance*self.movement_speed
        self.crater1.y -= self.vy*self.advance*self.movement_speed
        self.crater2.y -= self.vy*self.advance*self.movement_speed
        self.crater3.y -= self.vy*self.advance*self.movement_speed
        self.crater4.y -= self.vy*self.advance*self.movement_speed

asteroide = AsteroideClass()
asteroide2= AsteroideClass(DespX=650)
asteroide3= AsteroideClass(Xtamano=1.3,DespX=1030)

@window.event
def on_draw():
    #Limpiamos ventana
    window.clear()

    #Movemos estrellas y otros objetos
    estrella_1.update(DespY=300)
    estrella.update(DespY=300)
    estrella1.update(DespY=300)
    estrella2.update(DespY=300)
    estrella3.update(DespY=300)
    estrella4.update(DespY=300)
    estrella5.update(DespY=300)
    estrella6.update(DespY=300)
    estrella7.update(DespY=300)
    estrella8.update(DespY=300)
    estrella9.update(DespY=300)

    asteroide.update()
    asteroide2.update()
    asteroide3.update()

    #Dibujamos los batch
    estrellas.draw()
    asteroides.draw()
    nave.draw()

run()