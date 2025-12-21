import turtle

def tree(length, level):
    if level == 0:
        return

    turtle.forward(length)

    turtle.left(30)
    tree(length * 0.7, level - 1)

    turtle.right(60)
    tree(length * 0.7, level - 1)

    turtle.left(30)
    turtle.backward(length)


#налаштування черепашек нінзя
turtle.speed(0)
turtle.left(90)
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()

#рівень рекурсії
level = int(input("Введіть рівень рекурсії:"))

tree(100, level)

turtle.done()