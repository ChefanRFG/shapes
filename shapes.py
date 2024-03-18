import turtle
# Create a turtle object
t = turtle.Turtle()

# Set turtle speed (slow down for better visualization)
t.speed(1)
# Move the turtle to the starting position (adjust values for different positions)
t.penup()
t.goto(-50, 0)
t.pendown()

# Draw a square with side length 100
for _ in range(4):
    t.forward(100)
    t.right(90)

import turtle

window = turtle.Screen()
window.title("Dibujando un triángulo")
t = turtle.Turtle()

for _ in range(3):
    t.forward(100)  # Avanzar 100 píxeles
    t.left(120)     # Girar 120 grados hacia la izquierda


import turtle

window = turtle.Screen()
window.title("Dibujando un rectángulo")
t = turtle.Turtle()

for _ in range(2):
    t.forward(200)  # Avanzar 200 píxeles (largo del rectángulo)
    t.left(90)      # Girar 90 grados hacia la izquierda (esquina del rectángulo)
    t.forward(100)  # Avanzar 100 píxeles (ancho del rectángulo)
    t.left(90)      # Girar 90 grados hacia la izquierda (esquina del rectángulo)

window.mainloop()
