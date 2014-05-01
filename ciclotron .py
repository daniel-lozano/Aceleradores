import pylab as plt
import math as mt
import numpy as np

#constantes--------------------------

q=1#1.6*10**(-19)
m=1#1.672*10**(-27)
Vxo=0.0
Vyo=0.0
Yo=0.0
Xo=-0.05
d=0.00
R=10000.0
Eo=2.0
B=1.0
fi=0.0
dt=0.01
w=q*B/m
x=[]
y=[]
vx=[]
vy=[]
ac=[]
t=[]
i=0

##_----------------------------------------------------------

vx.append(Vxo)
vy.append(Vyo)
x.append(Xo)
y.append(Yo)
print "frecuencia de ciclotron",w

#aceleracion-----------------------------------------------

def aceleracion(x,y,vx,vy,t):
    
    ax=-q*x*B*mt.sqrt((vx**2+vy**2)/(x**2+y**2))/m
    ay=-q*y*B*mt.sqrt((vx**2+vy**2)/(x**2+y**2))/m

    if(-d/2<=y and y<=d/2):
        ay=ay+q*Eo*mt.cos(w*t+fi)/m
        
    A=[ax,ay]
    return A

#tomando el campo electrico-------------------------------------------

time=np.linspace(0,10,1000)
EF=np.zeros(len(time),dtype="float")

for i in range(len(time)):
    
    EF[i]=Eo*mt.cos(w*time[i])
    
print len(EF),len(time)

#plt.plot(time,EF)
#plt.xlabel("$tiempo $")
#plt.ylabel("$Campo\ Electrico\ $")
#plt.savefig("campo_electrico.png")
#plt.close()
##EVOLUCION DE LOS DATOS ------------------------------

for i in range(1000):
#while(sqrt(x[-1]**2+y[-1]**2) < R) :
        
        t.append(i*dt)
        
        #paso 1------------------------------
        EF[i]=Eo*mt.cos(w*t[i])
        t1=t[i]
        x1=x[i]
        y1=y[i]
        vx1=vx[i]
        vy1=vy[i]
        ax1,ay1=aceleracion(x1,y1,vx1,vy1,t1)
        
        kx1=vx1*dt
        lx1=ax1*dt
        ky1=vy1*dt
        ly1=ay1*dt
        
        #paso2-------------------------------
        
        t2=t[i]+0.5*dt
        x2=x[i]+0.5*kx1
        y2=y[i]+0.5*ky1
        vx2=vx[i]+0.5*lx1
        vy2=vy[i]+0.5*ly1
        ax2,ay2=aceleracion(x2,y2,vx2,vy2,t2)
        
        kx2=vx2*dt
        lx2=ax2*dt
        ky2=vy2*dt
        ly2=ay2*dt
        
        #paso3-------------------------------
        
        t3=t[i]+0.5*dt
        x3=x[i]+0.5*kx2
        y3=y[i]+0.5*ky2
        vx3=vx[i]+0.5*lx2
        vy3=vy[i]+0.5*ly2
        ax3,ay3=aceleracion(x3,y3,vx3,vy3,t3)
        
        kx3=vx3*dt
        lx3=ax3*dt
        ky3=vy3*dt
        ly3=ay3*dt
        
        #paso4-------------------------------
        
        t4=t[i]+dt
        x4=x[i]+kx3
        y4=y[i]+ky3
        vx4=vx[i]+lx3
        vy4=vy[i]+ly3
        ax4,ay4=aceleracion(x4,y4,vx4,vy4,t4)
        
        kx4=vx4*dt
        lx4=ax4*dt
        ky4=vy4*dt
        ly4=ay4*dt
        
        Kx=(kx4+2*kx3+2*kx2+kx1)/6
        Ky=(ky4+2*ky3+2*ky2+ky1)/6
        Lx=(lx4+2*lx3+2*lx2+lx1)/6
        Ly=(ly4+2*ly3+2*ly2+ly1)/6
        
        x.append(x1+Kx)
        y.append(y1+Ky)
        vx.append(vx1+Lx)
        vy.append(vy1+Ly)
        
        
plt.scatter(x,y)
#plot(x,y)
plt.scatter(0,-0.005)
plt.scatter(0,0.005)
plt.savefig("trayectoria.png")



