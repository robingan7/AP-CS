import turtle
import os
import math
import random


wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invader")
#wn.bgpic("space")

turtle.register_shape("spaceship2.gif")
turtle.register_shape("alexblue.gif")


border_pen=turtle.Turtle()
border_pen.speed(0)

border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

score=0

score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.color("blue")
score_pen.penup()
score_pen.setposition(-290,280)
scoreString="Score: %s"%score
score_pen.write(scoreString,False,align="left",font=("Arial",14,"normal"))
score_pen.hideturtle()

superNum=0

super_pen=turtle.Turtle()
super_pen.speed(0)
super_pen.color("blue")
super_pen.penup()
super_pen.setposition(-110,280)
superString="numbers of super bullet: %s"%superNum
super_pen.write(superString,False,align="left",font=("Arial",14,"normal"))           
super_pen.hideturtle()

level=1

level_pen=turtle.Turtle()
level_pen.speed(0)
level_pen.color("blue")
level_pen.penup()
level_pen.setposition(-190,280)
levelString="level: %s"%level
level_pen.write(levelString,False,align="left",font=("Arial",14,"normal"))
level_pen.hideturtle()



box=turtle.Turtle()
box.speed(0)
box.shape("triangle")
box.penup()
box.color("green")
box.shapesize(1,1)
box.hideturtle()


player=turtle.Turtle()
player.color("blue")
player.shape("spaceship2.gif")
player.speed(0)
player.penup()
player.setposition(0,-250)
player.setheading(90)



superBullet=turtle.Turtle()
superBullet.speed(0)
superBullet.shape("circle")
superBullet.color("blue")
superBullet.setheading(90)
superBullet.penup()
superBullet.shapesize(2,2)
superBullet.hideturtle()
superBulletspeed=20

superNum=0

superstate="notready"



def fire_super():
    global superstate
    if superstate=="ready":
        superstate="fire"
        x=player.xcor()
        y=player.ycor()+20
        superBullet.setposition(x,y)
        superBullet.showturtle()

def superCollision(t1,t2):
    distant=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distant<85:
        return True
    else:
        
        return False


playerspeed=15
playerspeed2=15

def move_left():
    x=player.xcor()
    x-=playerspeed
    if player.xcor()<-280:
        x=-280
    player.setx(x)
    
def move_right():
    x=player.xcor()
    x+=playerspeed
    if player.xcor()>280:
        x=280
    player.setx(x)
    
def move_left2():
    x2=player2.xcor()
    x2-=playerspeed2
    if player2.xcor()<-280:
        x=-280
    player2.setx(x2)
    
def move_right2():
    x2=player2.xcor()
    x2+=playerspeed2
    if player2.xcor()>280:
        x=280
    player2.setx(x2)    
    
def fire_bullet():
    global bulletstate
    if bulletstate=="ready":
        bulletstate="fire"
        x=player.xcor()
        y=player.ycor()+10
        bullet.setposition(x,y)
        bullet.showturtle()
        
def fire_bullet2():
    global bulletstate2
    if bulletstate2=="ready":
        bulletstate2="fire"
        x2=player2.xcor()
        y2=player2.ycor()-10
        bullet2.setposition(x2,y2)
        bullet2.showturtle()        
        
        
def isCollision(t1,t2):
    distant=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distant<35:
        return True
    else:
        return False
    
def cross_boarder(t1):
    if t1.ycor()<-250:
        return True
    else:
        return False
    
    
    
def setFinish(): 
    score3_pen=turtle.Turtle()
    score3_pen.speed(0)
    score3_pen.color("green")
    score3_pen.penup()
    score3_pen.setposition(-250,40)
    score3String="Game over\n Your score is: %s"%score
    score3_pen.write(score3String,False,align="left",font=("Elephant",44,"normal"))
    score3_pen.hideturtle()
    
    
turtle.listen()
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"space")
turtle.onkey(move_left,"Left")
turtle.onkey(setFinish,"q")
turtle.onkey(fire_super,"a")
turtle.onkey(move_right2,"d")
turtle.onkey(move_left2,"m")
turtle.onkey(fire_bullet2,"f")


number_of_ene=5

enemies=[]
for index in range(number_of_ene):
    enemies.append(turtle.Turtle())
    

    
for enemy in enemies:
    enemy.color("red")
    enemy.shape("alexblue.gif")
    enemy.penup()

    enemy.speed(0)
    x=random.randint(-200,200)
    y=random.randint(100,180)
    enemy.setposition(x,y)

enemyspeed=2




bullet=turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()
bulletspeed=20

bulletstate="ready"


count=0
count2=0
count3=0

while True:
    for enemy in enemies:
        x=enemy.xcor()
        x+=enemyspeed
        enemy.setx(x)
                  
        if enemy.xcor()>280:
            for e in enemies:
                y=e.ycor()
                y-=40
                e.sety(y)
            enemyspeed*=-1    
        
        if enemy.xcor()<-280:
            for e in enemies:
                y=e.ycor()
                y-=40
                e.sety(y)
                
            enemyspeed*=-1
            
      
        
        
        if bulletstate=="fire" :   
            y=bullet.ycor()
            y+=bulletspeed
            bullet.sety(y)  


        if bullet.ycor()>275:
            bullet.hideturtle()
            bulletstate="ready"
        
        
        if score%30==0 and score!=0 and count2<1:
            count=1
            superstate="ready"
            count2+=1
            
                        
            
            
        if count==1:
            superNum+=1
            super_pen.speed(0)
            super_pen.color("blue")
            super_pen.penup()
            super_pen.setposition(-110,280)
            superString="numbers of super bullet: %s"%superNum
            super_pen.hideturtle()
            super_pen.clear()
            super_pen.write(superString,False,align="left",font=("Arial",14,"normal"))
            count=2
            count3=0
            

            
        if superstate=="fire"and count==2: 
            bulletstate="ready"
            y2=superBullet.ycor()
            y2+=superBulletspeed
            superBullet.sety(y2)
            superstate=="notready"
            
            

        if superBullet.ycor()>275 and count3<1:
            superBullet.hideturtle()
            super_pen.speed(0)
            super_pen.color("blue")
            super_pen.penup()
            super_pen.setposition(-110,280)
            superString="numbers of super bullet: %s"%superNum
            super_pen.hideturtle()
            super_pen.clear()
            super_pen.write(superString,False,align="left",font=("Arial",14,"normal"))
            count3+=1
            
        if count3==1:    
            superstate="notready"
            
      
        
        if isCollision(bullet,enemy):
            bullet.hideturtle()
            bulletstate="ready"
            bullet.setposition(0,-400)
            x=random.randint(-200,200)
            y=random.randint(100,180)
            enemy.setposition(x,y)
            score+=10
            scoreString="Score: %s" %score
            score_pen.clear()
            score_pen.write(scoreString,False,align="left",font=("Arial",14,"normal"))
            for index in range(1,9):
                if int(score)/20==index:
                    enemyspeed=1*index
                    level+=1
                    levelString="level: %s"%level
                    level_pen.clear()
                    level_pen.write(levelString,False,align="left",font=("Arial",14,"normal"))
                    level_pen.hideturtle()
     
        if isCollision(player,enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            score2_pen=turtle.Turtle()
            score2_pen.speed(0)
            score2_pen.color("green")
            score2_pen.penup()
            score2_pen.setposition(-250,70)
            score2String="Game over\n Your score is: %s"%score
            score2_pen.write(score2String,False,align="left",font=("Elephant",44,"normal"))
            score2_pen.hideturtle()
            break
            
        if superCollision(superBullet,enemy):
            count2=0
            superNum-=1
            super_pen.speed(0)
            super_pen.color("blue")
            super_pen.penup()
            super_pen.setposition(-110,280)
            superString="numbers of super bullet: %s"%superNum
            super_pen.hideturtle()
            super_pen.clear()
            super_pen.write(superString,False,align="left",font=("Arial",14,"normal"))
            superstate="notready"
            superBullet.setposition(0,-400)
            x=random.randint(-200,200)
            y=random.randint(100,180)
            enemy.setposition(x,y)
            score+=10
            scoreString="Score: %s" %score
            score_pen.clear()
            score_pen.write(scoreString,False,align="left",font=("Arial",14,"normal"))
            bulletstate="ready"
            for index in range(1,10):
                if int(score)/20==index:
                    enemyspeed=1*index
                    level+=1
                    levelString="level: %s"%level
                    level_pen.clear()
                    level_pen.write(levelString,False,align="left",font=("Arial",14,"normal"))
                    level_pen.hideturtle()
            
            
        if cross_boarder(enemy):
            enemy.hideturtle()
            print("Game Over")

            score2_pen=turtle.Turtle()
            score2_pen.speed(0)

            score2_pen.color("green")
            score2_pen.penup()
            score2_pen.setposition(-250,70)
            score2String="Game over\n Your score is: %s"%score

            score2_pen.write(score2String,False,align="left",font=("Elephant",44,"normal"))
            score2_pen.hideturtle()
            
            break


delay=input("Press enter to finsh")#if don't use this the sreen will show for only a second
        
