q=0
w=0
e=0
a=0
s=0
d=0
z=0
x=0
c=0

def setup():
    background(55);
    size(600,600);
    
    
    rect(200,0,20,600,20);
    rect(400,0,20,600,20);
    rect(0,200,600,20,20);
    rect(0,400,600,20,20);

def draw():
    global q
    global w
    global e
    global a
    global s
    global d
    global z
    global x
    global c
    if keyPressed:
         if key == 'q' and q == 0 :
            circle(100,100,100)
            q+=1
         if key == 'w' and w == 0 :
            circle(300,100,100)
            w+=1
         if key == 'e' and e == 0 :
            circle(500,100,100)
            e+=1
         if key == 'a' and a == 0 :
            circle(100,300,100)
            a+=1
         if key == 's' and s == 0 :
            circle(300,300,100)
            s+=1
         if key == 'd' and d == 0 :
            circle(500,300,100)
            d+=1
         if key == 'z' and z == 0 :
            circle(100,500,100)
            z+=1
         if key == 'x' and x == 0 :
            circle(300,500,100)
            x+=1
         if key == 'c' and c == 0 :
            circle(500,500,100)
            c+=1
         if key == 't' and q == 0 :
            ellipse(100,100,100,50)
            q+=1
         if key == 'y' and w == 0 :
            ellipse(300,100,100,50)
            w+=1
         if key == 'u' and e == 0 :
            ellipse(500,100,100,50)
            e+=1
         if key == 'g' and a == 0 :
            ellipse(100,300,100,50)
            a+=1
         if key == 'h' and s == 0 :
            ellipse(300,300,100,50)
            s+=1
         if key == 'j' and d == 0 :
            ellipse(500,300,100,50)
            d+=1
         if key == 'b' and z == 0 :
            ellipse(100,500,100,50)
            z+=1
         if key == 'n' and x == 0 :
            ellipse(300,500,100,50)
            x+=1
         if key == 'm' and c == 0 :
            ellipse(500,500,100,50)
            c+=1

    
   

   
                                               
                              
               


                
