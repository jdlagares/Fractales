import turtle
t=turtle.Turtle()
t.speed(0)
turtle.setup(686,686, 0, 0)
import math
def PorcentajeT(n):
    areaT=153297.3218
    areaS=3**(n)*(math.sqrt(3)/4)*(595/2**n)**2
    resultado=areaS/areaT*100
    print("el porcentaje del area sombreada es:")
    print(resultado);
def PorcentajeB(n):
    areaT=470596
    areaS=(686/3**n)**2*5**n
    resultado=areaS/areaT*100
    print("el porcentaje del area sombreada es:")
    print(resultado);
def FractalH(x,y,n,long,t):
    if n>0:
        #esta parte pinta el lado izquierdo de la H
        t.penup()
        t.setx(x)  #ubico el pincel en la posicion x
        t.sety(y)  #ubico el pincel en la posicion y
        t.pendown()
        x1=x-(long/2) 
        t.goto(x1,y) #pinta desde la posicion (x,y) hasta la (x-(long/2) ,y)
        y1=y+(long/2)
        t.goto(x1,y1)#pinta desde la posicion (x-(long/2),y) hasta la (x-(long/2),y+(long/2)) 
        newpoinx1=x1
        newpointy1=y1
        t.penup()
        t.setx(x1)#ubico el pincel en la posicion x1
        t.sety(y) #ubico el pincel en la posicion y
        t.pendown()
        y1=y-(long/2)
        t.goto(x1,y1)#pinta desde la posicion (x1,y) hasta la (x-(long/2) ,y-(long/2))
        newpointy2=y1
        
        #me ubico en la parte central de la H
        t.penup()
        t.setx(x)
        t.sety(y)
        t.pendown()
        #esta parte pintaria la parte derecha de la H
        
        x1=x+(long/2)
        t.goto(x1,y)  #pinta desde la posicion (x,y) hasta la (x+(long/2) ,y)
        y1=y+(long/2)
        t.goto(x1,y1)#pinta desde la posicion (x,y) hasta la (x+(long/2) ,y+(long/2))
        newpointx2=x1
        newpointy3=y1
        t.penup()
        t.setx(x1)#ubico el pincel en la posicion x1
        t.sety(y)#ubico el pincel en la posicion y
        t.pendown()
        y1=y-(long/2)
        t.goto(x1,y1)#pinta desde la posicion (x1,y) hasta la (x+(long/2) ,y-(long/2))
        newpointy4=y1
        
        newlong=long/2 #Disminiyo la longitud a la mitad
        #por recursion se le envian los puntos centrales de las 4 H's, la iteracion reducida, la nueva longitud y el elemento turtle
        FractalH(newpoinx1, newpointy1,n-1,newlong,t)
        FractalH(newpoinx1,newpointy2,n-1,newlong,t)
        FractalH(newpointx2,newpointy3,n-1,newlong,t)
        FractalH(newpointx2,newpointy4,n-1,newlong,t)    
def boxFractal(x1,y1,x2,y2,x3,y3,x4,y4,n,t):
    if n==0:
        t.penup()
        t.setx(x1)#ubica el pencil en la posicion x1
        t.sety(y1)#ubica el pencil en la posicion y1
        t.pendown()
        t.begin_fill()
        t.goto(x2,y2)#pinta una linea desde (x1,y1) hasta (x2,y2)
        t.goto(x3,y3)#pinta una linea desde (x2,y2) hasta (x3,y3)
        t.goto(x4,y4)#pinta una linea desde (x3,y3) hasta (x4,y4)
        t.goto(x1,y1)#pinta una linea desde (x4,y4) hasta (x1,y1)
        t.end_fill()
    else:
        #Como son 5 cuadrados que se pintan por lo tanto se debe hacer 5 llamados recursivos. Se debe tener en cuenta que requiere..
        #que que el cuadrado se divida en 9 partes iguales y a cada llamado se le envia los respectivos puntos.
        #cuadrado superior izquierdo
        boxFractal(x1,y1,((x2-x1)/3)+x1,y1,((x2-x1)/3)+x1,((y4-y1)/3)+y1,x1,((y4-y1)/3)+y1,n-1,t)
        #cuadrado superior Derecho
        boxFractal(2*((x2-x1)/3)+x1,y1,x2,y2,x2,((y4-y1)/3)+y1,2*((x2-x1)/3)+x1,((y4-y1)/3)+y1,n-1,t)
        #cuadrado central
        boxFractal(((x2-x1)/3)+x1,((y4-y1)/3)+y1,2*((x2-x1)/3)+x1,((y4-y1)/3)+y1,2*((x2-x1)/3)+x1,2*((y4-y1)/3)+y1,((x2-x1)/3)+x1,2*((y4-y1)/3)+y1,n-1,t)
        #cuadrado superior izquierdo
        boxFractal(x4,2*((y4-y1)/3)+y1,((x2-x1)/3)+x1,2*((y4-y1)/3)+y1,((x2-x1)/3)+x1,y4,x4,y4,n-1,t)
        #cuadrado superior derecho
        boxFractal(2*((x2-x1)/3)+x1,2*((y4-y1)/3)+y1,x3,2*((y4-y1)/3)+y1,x3,y3,2*((x2-x1)/3)+x1,y4,n-1,t)
    
def sierspinskySieve(x1,y1,x2,y2,x3,y3,n,t):
    if n==0:
        #dibujar triangulo
        t.penup()
        t.setx(x1) 
        t.sety(y1)
        t.pendown()
        t.begin_fill()
        t.goto(x2,y2)
        t.goto(x3,y3)
        t.goto(x1,y1)
        t.end_fill()
    else:
        vx1 = PuntoMedio(x1, x2);
        vy1 = PuntoMedio(y1, y2); #calcula los puntos medios entre x1,x2 y y1,y2

        vx2 = PuntoMedio(x2, x3); #calcula los puntos medios entre x2,x3 y y2,y3
        vy2 = PuntoMedio(y2, y3); 

        vx3 = PuntoMedio(x3, x1); #calcula los puntos medios entre x3,x1 y y3,y1
        vy3 = PuntoMedio(y3, y1);
        
        sierspinskySieve(x1,y1,vx1,vy1,vx3,vy3,n-1,t)
        sierspinskySieve(vx1,vy1,x2,y2,vx2,vy2,n-1,t)   
        sierspinskySieve(vx3, vy3, vx2, vy2, x3, y3, n - 1,t)
        
def PuntoMedio(x1,x2):
    return (x1+x2)/2

salir = False
while not salir:
    print("digite el numero del fractal que desee ver");
    print("1.Sierspinsky sieve(Regla 90)");
    print("2.Box Fractal");
    print("3.FractalH");
    print("4.Salir");
    respuesta= int(input('Ingrese la respuesta: '));
    if respuesta==1:
        n= int(input('Digite n '));
        turtle.clearscreen()
        t.hideturtle()
        turtle.title("Sierspinsky sieve(Regla 90)")
        sierspinskySieve(-298,-171,0,343,297,-171,n,t)
        PorcentajeT(n)
       
    else:
        if respuesta==2:
            n= int(input('Digite n '))
            turtle.clearscreen()
            t.hideturtle()
            turtle.title("Box Fractal")
            boxFractal(-343,343,343,343,343,-343,-343,-343,n,t)
            PorcentajeB(n)
        else:
            if respuesta==3:
                n= int(input('Digite n '))
                turtle.clearscreen()
                t.hideturtle()
                turtle.title("Fractal H")
                FractalH(0,0,n,250,t)
            else:   
                salir=True
