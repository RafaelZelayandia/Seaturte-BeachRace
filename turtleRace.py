#!/bin/python3
from turtle import *
from random import randint
import turtle
import time
#from PIL import Image
#need to install Pillow onto VSC

screen = turtle.Screen()
screen.title("Turtle Race")

def fullScreen():
    screen.setup(width=1.0, height=1.0)

#img=Image.new('RGBA',(900,900))
#for i in range(900):
#    for j in range(900):
#        img.putpixel((i,j),(0,0,j/4))
#img.show()

fullScreen()
#sand background 
turtle.bgcolor ("#F7C573")
speed(0)
penup()
goto(-160,180)
pendown()
style = ('ms serif', 30, 'bold', 'italic')
turtle.write("Seaturtle Beach Race\n               by \n  Rafael Zelayandia", font=style)

#ocean background
penup()
turtle.goto(210,400)
turtle.color("#12EBD8")
turtle.begin_fill()
turtle.pendown()
turtle.forward(450)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(490)
turtle.right(100)
turtle.forward(200)
turtle.left(10)
turtle.forward(100)
turtle.left(20)
turtle.forward(40)
turtle.right(10)
turtle.forward(40)
turtle.right(10)
turtle.forward(50)
turtle.right(10)
turtle.forward(50)
turtle.left(45)
turtle.forward(30)
turtle.right(30)
turtle.forward(50)
turtle.left(10)
forward(50)
right(30)
forward(50)
right(20)
forward(30)
right(10)
forward(15)
left(20)
forward(15)
left(10)
forward(10)
left(10)
forward(20)
left(10)
forward(30)
right(5)
turtle.end_fill()

#Creating another turtle for the starting line.
start = turtle.Turtle()
start.up()
start.speed(0)
start.goto(-140, 140)
start.width(5)
start.right(90)
start.down()

#Drawing the starting line.
for i in range(37):
	start.color("green")
	start.forward(5)
	start.color("yellow")
	start.forward(5)

#Creating the finish line.
finish = turtle.Turtle()
finish.up()	#Allowing to move the finish line to a certain location.
finish.speed(0)
finish.goto(160, 140) #Moving the finish line to the correct position.
finish.down()
finish.right(90)
finish.width(5)

#Drawing the finish line.
for i in range(37):
	finish.color("blue")
	finish.forward(5)
	finish.color("red")
	finish.forward(5)

hideturtle()

first_text = turtle.Turtle()
first_text.speed(10)
first_text.up()
first_text.color("darkblue")
first_text.goto(-580, -20)
first_text.write("GET TO SAFETY!!!\nREACH THE BEACH!!!!!", font = ("ms serif", 20, "bold"))
first_text.down()

##483D8B	darkslateblue       kristina
##FFD700	gold                julie
##228B22	forestgreen         amanda
##008080	teal                natalie
##000000	black               katya
##C71585	mediumvioletred     imani
##DC6A20  burntorange         atiyana
##FF00BD  brightpink          shannon
##ADC304  yellowgreen         nina
#red      red                 kiri
#orange   orange              avery
##B8860B	darkgoldenrod       desiree

speed(0)
hideturtle()

kristina = Turtle()
kristina.color('#483D8B')
kristina.shape('turtle')
kristina.penup()
kristina.goto(-160,120)
kristina.pendown()
for turn in range(1):
   kristina.right(360)

julie = Turtle()
julie.color('#FFD700')
julie.shape('turtle')
julie.penup()
julie.goto(-160,90)
julie.pendown()
for turn in range(1):
   julie.left(360)

amanda = Turtle()
amanda.color('#228B22')
amanda.shape('turtle')
amanda.penup()
amanda.goto(-160,60)
amanda.pendown()
for turn in range(1):
   amanda.right(360)

natalie = Turtle()
natalie.color('#008080')
natalie.shape('turtle')
natalie.penup()
natalie.goto(-160,30)
natalie.pendown()
for turn in range(1):
   natalie.left(360)

katya = Turtle()
katya.color('#000000')
katya.shape('turtle')
katya.penup()
katya.goto(-160,0)
katya.pendown()
for turn in range(1):
   katya.right(360)

imani = Turtle()
imani.color('#C71585')
imani.shape('turtle')
imani.penup()
imani.goto(-160,-30)
imani.pendown()
for turn in range(1):
   imani.left(360)

atiyana = Turtle()
atiyana.color('#DC6A20')
atiyana.shape('turtle')
atiyana.penup()
atiyana.goto(-160,-60)
atiyana.pendown()
for turn in range(1):
   atiyana.right(360)

shannon = Turtle()
shannon.color('#FF00BD')
shannon.shape('turtle')
shannon.penup()
shannon.goto(-160,-90)
shannon.pendown()
for turn in range(1):
  shannon.left(360)

nina = Turtle()
nina.color('#ADC304')
nina.shape('turtle')
nina.penup()
nina.goto(-160,-120)
nina.pendown()
for turn in range(1):
  nina.right(360)

kiri = Turtle()
kiri.color('red')
kiri.shape('turtle')
kiri.penup()
kiri.goto(-160,-150)
kiri.pendown()
for turn in range(1):
  kiri.left(360)
  
avery = Turtle()
avery.color('#FF5500')
avery.shape('turtle')
avery.penup()
avery.goto(-160,-180)
avery.pendown()
for turn in range(1):
  avery.right(360)
  
desiree = Turtle()
desiree.color('#B8860B')
desiree.shape('turtle')
desiree.penup()
desiree.goto(-160,-210)
desiree.pendown()
for turn in range(1):
  desiree.left(360)
  
hideturtle()

#Racelight Countdown 
#Creating the first red circle as a turtle.
red_circle_1 = turtle.Turtle()
red_circle_1.speed(1)
red_circle_1.up()
red_circle_1.goto(0, 120)
red_circle_1.color("red")
red_circle_1.shape("circle")

#Creating the second red circle indicating starting is about to begin.
red_circle_2 = turtle.Turtle()
red_circle_2.speed(1)
red_circle_2.up()
red_circle_2.goto(0, 90)
red_circle_2.color("red")
red_circle_2.shape("circle")

#Creating the third red circle indicating starting is about to begin.
red_circle_3 = turtle.Turtle()
red_circle_3.speed(1)
red_circle_3.up()
red_circle_3.goto(0, 60)
red_circle_3.color("red")
red_circle_3.shape("circle")

#Creating the first green circle indicating starting is about to begin.
green_circle_1 = turtle.Turtle()
green_circle_1.speed(1)
green_circle_1.up()
green_circle_1.goto(0, 0)
green_circle_1.color("green")
green_circle_1.shape("circle")
green_circle_1.pensize(100)

red_circle_1.ht()
red_circle_2.ht()
red_circle_3.ht()
green_circle_1.ht()

for turn in range(100):
  speed(0)
 
  kristina.forward(randint(1,5))
  julie.forward(randint(1,5))
  amanda.forward(randint(1,5))
  natalie.forward(randint(1,5))
  katya.forward(randint(1,5))
  imani.forward(randint(1,5))
  atiyana.forward(randint(1,5))
  shannon.forward(randint(1,5))
  nina.forward(randint(1,5))
  kiri.forward(randint(1,5))
  avery.forward(randint(1,5))
  desiree.forward(randint(1,5))

#This will display the winner at the bottom of the race
  if kristina.xcor() >= 150:
			kristina.goto(-180, -280)
			kristina.write("   KRISTINA MADE IT TO THE SEA!!!!!", font = ("Times New Roman", 14, "normal"))
			#This tells white turtle to move to a position if they win (cross a certain x position that is equivalent to the x position of the finish line).
			break
			#This will stop the loop (and thus the turtles moving) regardless of if they have finished the range set earlier.
  if julie.xcor() >= 150:
			julie.goto(-180, -280)
			julie.write("   JULIE MADE IT TO THE SEA!!!!!", font = ("Times New Roman", 14, "normal"))
			break
  if amanda.xcor() >= 150:
			amanda.goto(-180, -280)
			amanda.write("   AMANDA MADE IT TO THE SEA!!!!!", font = ("Times New Roman", 14, "normal"))
			break
  if natalie.xcor() >= 150:
			natalie.goto(-180, -280)
			natalie.write("   NATALIE MADE IT TO THE SEA!!!!!", font = ("Times New Roman", 14, "normal"))
			break
  if katya.xcor() >= 150:
			katya.goto(-180, -280)
			katya.write("   KATYA MADE IT TO THE SEA!!!!!", font = ("Times New Roman", 14, "normal"))
			break
  if imani.xcor() >= 150:
			imani.goto(-180, -280)
			imani.write("   IMANI MADE IT TO THE SEA!!!!!", font = ("Times New Roman", 14, "normal"))
			break
  if atiyana.xcor() >= 150:
			atiyana.goto(-180, -280)
			atiyana.write("   ATIYANA MADE IT TO THE SEA!!!!!", font = ("Times New Roman", 14, "normal"))
			break
  if shannon.xcor() >= 150:
			shannon.goto(-180, -280)
			shannon.write("   SHANNON MADE IT TO THE SEA!!!!!", font = ("Times New Roman", 14, "normal"))
			break
  if nina.xcor() >= 150:
			nina.goto(-180, -280)
			nina.write("   NINA MADE IT TO THE SEA!!!!!", font = ("Times New Roman", 14, "normal"))
			break
  if kiri.xcor() >= 150:
			kiri.goto(-180, -280)
			kiri.write("   KIRI MADE IT TO THE SEA!!!!!", font = ("Times New Roman", 14, "normal"))
			break
  if avery.xcor() >= 150:
			avery.goto(-180, -280)
			avery.write("   AVERY MADE IT TO THE SEA!!!!!", font = ("Times New Roman", 14, "normal"))
			break
  if desiree.xcor() >= 150:
			desiree.goto(-180, -280)
			desiree.write("   DESIREE MADE IT TO THE SEA!!!!!", font = ("Times New Roman", 14, "normal"))
			break

time.sleep(4)

turtle.clearscreen()

fullScreen()
turtle.bgcolor ("black")
speed(0)
penup()
goto(-300,-100)
pendown()
pencolor("cyan")
style = ('ms serif', 30, 'bold', 'italic')
turtle.write("I hope you enjoyed the race\n                                             3\n                                        Rz^", font=style)
hideturtle()
time.sleep(4)
#Be Safe