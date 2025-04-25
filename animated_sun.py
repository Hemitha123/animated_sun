import turtle
import math
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("Animated Sun")

# Create the sun
sun = turtle.Turtle()
sun.shape("turtle")
sun.color("yellow")
sun.penup()
sun.speed(0)

# Draw the sun's body
sun.goto(0, -100)
sun.begin_fill()
sun.circle(100)
sun.end_fill()

# Create the sun rays
rays = turtle.Turtle()
rays.color("yellow")
rays.penup()
rays.speed(0)

# Function to draw rays
def draw_rays():
    rays.clear()
    for angle in range(0, 360, 15):
        rays.goto(0, 0)
        rays.setheading(angle)
        rays.forward(120)
        rays.pendown()
        rays.forward(30)
        rays.penup()

# Animate the sun rays
def animate_sun():
    for i in range(20):  # Number of animation cycles
        draw_rays()
        rays.hideturtle()
        time.sleep(0.1)
        rays.clear()

# Run the animation
animate_sun()

# Close the window on click
screen.mainloop()