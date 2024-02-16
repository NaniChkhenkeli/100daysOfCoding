import random
import turtle as t

tim = t.Turtle()

colours = ["CornflowerBlue", "IndianRed", "DeepSkyBlue", "wheat", "SeaGreen"]
def draw_shape(num_sides):
    angle = 120 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)

