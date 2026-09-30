"""GUI adapter fixing the original global-Turtle dependency.

Run with python3 turtle_reference.py on a system with Tk/Turtle installed.
The mathematical core and SVG export require neither Turtle nor Tk.
"""
from adler_fractal import Parameters, iter_segments


def draw_fractal(_turtle, start_pos=(0, 0), ang=20, lng=200,
                 iterations=2, scale=1.0):
    p = Parameters.from_angle(ang, length=lng, iterations=iterations,
                             scale=scale, origin=complex(*start_pos))
    for s in iter_segments(p):
        _turtle.penup()
        _turtle.goto(s.start.real, s.start.imag)
        _turtle.pendown()
        _turtle.goto(s.end.real, s.end.imag)


if __name__ == "__main__":
    import turtle
    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0)
    screen.tracer(0, 0)
    pen = turtle.Turtle()
    pen.speed(0)
    draw_fractal(pen, ang=5)
    pen.hideturtle()
    screen.update()
    turtle.done()
