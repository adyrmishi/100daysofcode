import turtle as t
import random as r

colour_list = [(235, 242, 249), (237, 224, 80), (205, 4, 73), (236, 50, 130),
               (198, 164, 8), (111, 179, 218), (204, 75, 12), (219, 161, 103),
               (234, 224, 4), (11, 23, 63), (29, 189, 111), (22, 107, 174), (16, 28, 177),
               (216, 134, 179), (8, 186, 216), (229, 167, 200), (210, 25, 148), (122, 190, 160),
               (7, 49, 26), (34, 136, 72), (63, 20, 7), (126, 219, 234), (190, 14, 4), (109, 87, 215),
               (140, 217, 202), (238, 64, 34), (71, 10, 28)]


tim = t.Turtle()
screen = t.Screen()
start = -250
t.colormode(255)
tim.hideturtle()
tim.penup()
print(tim.goto(start, start))


def generate_random_colour():
    random_colour = r.choice(colour_list)
    return random_colour


def line_of_dots():
    for _ in range(10):
        tim.pendown()
        tim.dot(20, generate_random_colour())
        tim.penup()
        tim.forward(50)


for _ in range(start + 50, -start, 50):
    line_of_dots()
    tim.goto(start, _)


screen.exitonclick()
