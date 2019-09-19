import turtle
import os

# desenhar tela

screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer()

while True:
    screen.update()