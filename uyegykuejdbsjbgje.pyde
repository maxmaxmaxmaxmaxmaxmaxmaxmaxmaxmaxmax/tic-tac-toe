turn=0
winner=0
start=0
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
    global turn
    global start
    global winner
   

    if start == 1:
            fill(55);
            rect(0,0,600,600);
            fill(255);
            rect(200,0,20,600,20);
            rect(400,0,20,600,20);
            rect(0,200,600,20,20);
            rect(0,400,600,20,20);
        
    if keyPressed and start > 0:
        start += 1
        if key == 'q' and q == 0 and turn == 0:
            circle(100,100,100)
            q+=1
            turn+=1
        if key == 'w' and w == 0 and turn == 0:
            circle(300,100,100)
            w+=1
            turn+=1
        if key == 'e' and e == 0 and turn == 0 :
            circle(500,100,100)
            e+=1
            turn+=1
        if key == 'a' and a == 0 and turn == 0:
            circle(100,300,100)
            a+=1
            turn+=1
        if key == 's' and s == 0 and turn == 0:
            circle(300,300,100)
            s+=1
            turn+=1
        if key == 'd' and d == 0 and turn == 0:
            circle(500,300,100)
            d+=1
            turn+=1
        if key == 'z' and z == 0 and turn == 0 :
            circle(100,500,100)
            z+=1
            turn+=1
        if key == 'x' and x == 0 and turn == 0:
            circle(300,500,100)
            x+=1
            turn+=1
        if key == 'c' and c == 0 and turn == 0:
            circle(500,500,100)
            c+=1
            turn+=1
        if key == 't' and q == 0 and turn == 1:
            ellipse(100,100,100,50)
            q+=5
            turn-=1
        if key == 'y' and w == 0 and turn == 1:
            ellipse(300,100,100,50)
            w+=5
            turn-=1
        if key == 'u' and e == 0 and turn == 1:
            ellipse(500,100,100,50)
            e+=5
            turn-=1
        if key == 'g' and a == 0 and turn == 1:
            ellipse(100,300,100,50)
            a+=5
            turn-=1
        if key == 'h' and s == 0 and turn == 1:
            ellipse(300,300,100,50)
            s+=5
            turn-=1
        if key == 'j' and d == 0 and turn == 1:
            ellipse(500,300,100,50)
            d+=5
            turn-=1
        if key == 'b' and z == 0 and turn == 1:
            ellipse(100,500,100,50)
            z+=5
            turn-=1
        if key == 'n' and x == 0 and turn == 1:
            ellipse(300,500,100,50)
            x+=5
            turn-=1
        if key == 'm' and c == 0 and turn == 1:
            ellipse(500,500,100,50)
            c+=5
            turn-=1
            
    if keyPressed and start == 0:
        start+=1
        
    if start == 0 and winner > 0:
        fill(55)
        rect(0,0,600,600);
        fill(255);
        textSize(120);
        text("tic tac toe", 60, 300,)
        text("press enter",20, 400)
        text(" to start", 95, 500)
        textSize(20);
        text("p1 use q,w,e,a,s,d,z,x,c, for control",165, 525)
        text("p2 use t,y,u,g,h,j,v,b,n, for control",165, 550)
    
    if start == 0:
        textSize(120);
        text("tic tac toe", 60, 300,)
        text("press enter",20, 400)
        text(" to start", 95, 500)
        textSize(20);
        text("p1 use q,w,e,a,s,d,z,x,c, for control",165, 525)
        text("p2 use t,y,u,g,h,j,v,b,n, for control",165, 550)


    if int(q)+int(w)+int(e) == 3 or int(a)+int(s)+int(d) == 3 or int(z)+int(x)+int(c) == 3 or int(q)+int(a)+int(z) == 3 or int(w)+int(s)+int(x) == 3 or int(e)+int(d)+int(c) == 3 or int(e)+int(s)+int(z) == 3 or int(q)+int(s)+int(c) == 3:
        winner += 1
        start -= 1
        
    if int(q)+int(w)+int(e) == 15 or int(a)+int(s)+int(d) == 15 or int(z)+int(x)+int(c) == 15 or int(q)+int(a)+int(z) == 15 or int(w)+int(s)+int(x) == 15 or int(e)+int(d)+int(c) == 15 or int(e)+int(s)+int(z) == 15 or int(q)+int(s)+int(c) == 15:
        winner += 2
        start -= 1

    if int(winner) == 1:
        fill(255);
        textSize(80);
        text("PLAYER 1 WINS!!", 20, 150)
  
    if int(winner) == 2:
        fill(255);
        textSize(120);
        text("PLAYER 2 WINS!!", 10, 100)
        


        

        


    
   

   
                                               
                              
               


        
