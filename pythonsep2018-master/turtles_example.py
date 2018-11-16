
import turtle

def square():
    t = turtle.Turtle()
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    turtle.mainloop()

def polygon(sides = 4, length = 50):
    t = turtle.Turtle()
    for i in range(sides):
        t.forward(length)
        t.left(360/sides)

    turtle.mainloop()


def pattern():
    t = turtle.Turtle()
    t.pendown()
    t.pencolor("red")
    for i in range(100):
        t.forward(i)
        t.right(85)

    turtle.mainloop()

def main():
    # polygon(1, 200)
    pattern()

if __name__ == '__main__':
    main()