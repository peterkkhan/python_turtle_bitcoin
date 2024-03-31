import turtle
from turtle import *


def bitcoin():
    t=turtle.Turtle()
    wn=Screen()

    t.pensize(15)
    t.hideturtle()
    t.penup()

    #outer circle
    
    t.setposition(0,-270)
    t.pendown()
    t.begin_fill()
    t.color("white")
    t.pencolor("orange")
    t.circle(270)
    t.end_fill()
    t.penup()

    #inner circle
    t.setposition(0,-220)
    t.pendown()
    t.begin_fill()
    t.color("orange")
    t.pencolor("orange")
    t.circle(220)
    t.end_fill()
    t.penup()

    #draw 'B'
    t.setposition(30,120)
    t.pendown()
    t.begin_fill()
    t.color("white")
    t.pensize(2)
    t.pencolor("white")
    t.right(-90)
    t.forward(60)
    t.right(270)
    t.forward(40)
    t.right(-90)
    t.forward(60)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(60)
    t.right(-90)
    t.forward(40)
    t.right(-90)
    t.forward(60)
    t.right(90)
    t.forward(70)
    t.right(-90)
    t.forward(40)
    t.right(-90)
    t.forward(30)
    t.circle(-10,90)
    t.forward(160)
    t.circle(-10,90)
    t.forward(30)
    t.right(-90)
    t.forward(40)
    t.right(-90)
    t.forward(70)
    t.right(90)
    t.forward(60)
    t.right(-90)
    t.forward(40)
    t.right(-90)
    t.forward(60)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(60)
    t.right(-90)
    t.forward(40)
    t.right(-90)
    t.forward(60)
    t.right(90)
    t.forward(15)
    t.circle(80,160)
    t.right(-30)
    t.circle(-54,-180)
    t.right(194)
    t.forward(24)
    t.end_fill()
    t.penup()

    #outer side 'B'
    t.setposition(-40,80)
    t.pendown()
    t.begin_fill()
    t.color("orange")
    t.pencolor("orange")
    t.right(-93)
    t.forward(60)
    t.right(-90)
    t.forward(45)
    t.circle(31,170)
    t.right(-10)
    t.end_fill()
    t.penup()

    t.setposition(-40,-15)
    t.pendown()
    t.begin_fill()
    t.color("orange")
    t.pencolor("orange")
    t.right(-92)
    t.forward(75)
    t.right(-90)
    t.forward(50)
    t.circle(37,190)
    t.right(12)
    t.forward(44)
    t.end_fill()

    turtle.done()

a = int(input("비트코인을 좋아하나요? 좋아한다면 숫자 0을 누르고 싫어한다면 아무숫자나 누르세요."))
if a == 0:
    bitcoin()
else:
    youarepoor = ["You should visit:https://bitcoin.org/bitcoin.pdf",
                  "You should visit:https://bitcoin.org/bitcoin.pdf",
                  "You should visit:https://bitcoin.org/bitcoin.pdf",
                  "You should visit:https://bitcoin.org/bitcoin.pdf",
                  "You should visit:https://bitcoin.org/bitcoin.pdf",
                  "You should visit:https://bitcoin.org/bitcoin.pdf",
                  "You should visit:https://bitcoin.org/bitcoin.pdf",
                  "You should visit:https://bitcoin.org/bitcoin.pdf"
                  "You should visit:https://bitcoin.org/bitcoin.pdf",
                  "You should visit:https://bitcoin.org/bitcoin.pdf",
                  "You should visit:https://bitcoin.org/bitcoin.pdf",
                  "You should visit:https://bitcoin.org/bitcoin.pdf",
                  "You should visit:https://bitcoin.org/bitcoin.pdf",
                  "You should visit:https://bitcoin.org/bitcoin.pdf",
                  "You should visit:https://bitcoin.org/bitcoin.pdf",
                  "You should visit:https://bitcoin.org/bitcoin.pdf"
                  "You should visit:https://bitcoin.org/bitcoin.pdf",
                  "You should visit:https://bitcoin.org/bitcoin.pdf",
                  "You should visit:https://bitcoin.org/bitcoin.pdf",
                  "You should visit:https://bitcoin.org/bitcoin.pdf",
                  "You should visit:https://bitcoin.org/bitcoin.pdf",
                  "You should visit:https://bitcoin.org/bitcoin.pdf",
                  "You should visit:https://bitcoin.org/bitcoin.pdf",
                  "You should visit:https://bitcoin.org/bitcoin.pdf"
                  "You should visit:https://bitcoin.org/bitcoin.pdf",
                  "You should visit:https://bitcoin.org/bitcoin.pdf",
                  "You should visit:https://bitcoin.org/bitcoin.pdf",
                  "You should visit:https://bitcoin.org/bitcoin.pdf",
                  "You should visit:https://bitcoin.org/bitcoin.pdf",
                  "You should visit:https://bitcoin.org/bitcoin.pdf",
                  "You should visit:https://bitcoin.org/bitcoin.pdf",
                  "You should visit:https://bitcoin.org/bitcoin.pdf"
                  ]
    for i in youarepoor:
        print(i)
    
