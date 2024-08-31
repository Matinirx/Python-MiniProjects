import turtle
import time
import random

WIDTH, HEIGHT = 600, 500
COLORS = ['Cyan', 'Black', 'Red', 'Green', 'Blue', 'Purple', 'Pink', 'Brown', 'Yellow', 'Gray']

def number_of_racers():
    racers = 0
    
    while True:
        racers = input("Enter the number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Invalid Input, write a numeric value!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Invalid Input, write a number between 2 - 10!")

def race(colors):
    turtles = create_turtle(colors)
    
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]
            
            
def create_turtle(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1) 

    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)   
        racer.pendown()
        turtles.append(racer)

    return turtles
 
def init_turtle():

    screen = turtle.Screen()
    screen.title("Turtle Race")
    screen.setup(WIDTH, HEIGHT)

racers = number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f"The winner is the turtle with the color {winner}")
time.sleep(5)