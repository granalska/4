import turtle

def koch(t, length, level):
    """
    функція, яка малює фрактал Коха
    t - об'єкт turtle
    length - довжина фрактала
    level  - рівень рекурсії
    """
    if level == 0:
        t.forward(length)
    else:
        koch(t, length / 3, level - 1)
        t.left(60)
        koch(t, length / 3, level - 1)
        t.right(120)
        koch(t, length / 3, level - 1)
        t.left(60)
        koch(t, length / 3, level - 1)

def draw_snowflake(level):
    screen = turtle.Screen()
    screen.title(f"Сніжинка Коха — рівень {level}")
    screen.setup(width=800, height=700)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)        #максимальна швидкість мал
    t.pensize(2)

    #початкова довжина сторони
    base_length = 400
    

    #позиц 
    t.penup()
    t.goto(-length / 2, length / 3)
    t.pendown()
    t.showturtle()

    #малюємо три сторони 
    for _ in range(3):
        koch(t, length, level)
        t.right(120)

    t.hideturtle()
    turtle.done()

if __name__ == "__main__":
    try:
        level_input = input("Введіть рівень рекурсії (ціле число >= 0, рекомендовано 0..6): ").strip()
        level = int(level_input)
        if level < 0:
            raise ValueError
    except ValueError:
        print("Будь ласка, введіть коректне ціле число >= 0")
    else:
        draw_snowflake(level)
        