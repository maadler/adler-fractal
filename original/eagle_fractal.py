import turtle
from enum import Enum


class SpeedEnum(Enum):
    HIGH = 0
    X_HIGH = 1
    SUPER_HIGH = 2


def draw_fractal(
        _turtle: turtle.Turtle,
        start_pos: tuple[int, int],
        ang: int = 20,
        lng: int = 200,
        iterations: int = 2
) -> None:
    if iterations <= 0:
        return
    circle_positions: list[tuple] = []
    turt.penup()
    turt.goto(*start_pos)
    turt.pendown()

    for angle in range(0, 360, ang):
        turt.setheading(angle)
        turt.forward(lng)
        circle_positions.append(tuple(turt.pos()))
        turt.penup()
        turt.goto(*start_pos)
        turt.pendown()

    for circle_position in circle_positions:
        draw_fractal(
            _turtle,
            circle_position,
            ang=ang,
            lng=lng,
            iterations=iterations - 1
        )

if __name__ == '__main__':
    speed: SpeedEnum = SpeedEnum.X_HIGH
    screen: turtle._Screen = turtle.Screen()

    # Fenster auf die verfügbare Bildschirmgröße bringen
    screen.setup(width=1.0, height=1.0)

    if speed == SpeedEnum.SUPER_HIGH:
        screen.tracer(0, 0)
    elif speed == SpeedEnum.X_HIGH:
        screen.tracer(5, 0)

    turt: turtle.Turtle = turtle.Turtle()
    turt.shape("turtle")
    turt.speed(0)

    # Fraktal zeichnen
    draw_fractal(turt, (0, 0), lng=200, ang=5, iterations=2)

    # Fenster offen halten
    turt.hideturtle()
    screen.update()
    turtle.done()