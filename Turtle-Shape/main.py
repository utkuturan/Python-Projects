import turtle as t
import random


tim = t.Turtle()

colours = ["aquamarine", "crimson","medium blue","chartreuse","purple","deep pink","light coral","yellow","light sky blue","dark green","dark slate blue"]


def draw_shape(num_sides):
    angle = 360/ num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 13):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)