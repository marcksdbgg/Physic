import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Definimos los paramentros
theta=int(input("Ingrese el angulo de inclinacion: "))
#20theta=(theta*np.pi)/180 #Definiendo el ángulo
h=float(input("Ingrese la altura deseada: "))
x0=0. #Posicion inicial x
y0=0. #Posicion inicial y
g=9.8 #Gravedad
v0=float(input("Ingrese la velocidad deseada: ")) #Velocidad inicial
vy0=np.sin(theta)*v0 #Velocidad inicial en y
#Parametros auxiliares para hallar el tiempo
v2sin2=math.pow(v0,2)*math.pow(np.sin(theta),2)
aux=(2*vy0)/g
dosgh=2*g*h
aux2=(-vy0+math.sqrt(v2sin2+dosgh))/g
time= aux+aux2 #Se calcula el tiempo de vuelo
print("La distancia alcanzada es: ",time*v0," y el tiempo es: ",time)

#Ecuación de la posición en x
def x_pos(theta,t,v0,x0):
    x=x0+v0*np.cos(theta)*t
    return x

#Ecuación de la posición en y
def y_pos(theta,t,v0,y0):
    y=y0+(v0*np.sin(theta)*t)-((g*t**2)/2)
    return y

#Asignando los valores de x,y según las marcas de tiempo
t=np.linspace(0,time,50)
x=x_pos(theta,t,v0,0)
y=y_pos(theta,t,v0,0)
N=len(t)

#Definiendo la vista de la cuadricula en x,y
fig, ax=plt.subplots()
ln, = plt.plot(x,y,'ro')
ax.set_title('Movimiento Parabólico')
ax.set_xlim(0,100)
ax.set_ylim(-100,0)

#Actualizador para animación de la partícula
def actualizar(i):
    ln.set_data(x[i],y[i])
    return ln,
ani = animation.FuncAnimation(fig,actualizar,range(N),interval=0.00001)
plt.plot(x,y)
plt.grid()
plt.show()