import turtle
"""
Initial code written by David Johnson, University of Utah.
This, and all derived works may not be publicly shared.

Assignment completed by David Peters
"""

def draw_spiral(start_length, end_length, turtle):
    """
    Draws a square spiral with a starting side length of start_length
    centered at the current turtle location.
    The side length grows by 5 each turn.
    The spiral stops when the side length is greater than end_length.

    :param start_length: The starting length of the spiral
    :param end_length: The length of the last side of the square spiral
    :param turtle: A python turtle
    :return: None
    """
    side = start_length
    # Note that the end_length is included as a part of the square spiral.
    while side <= end_length:
        turtle.forward(side)
        turtle.left(90)
        side = side + 5



def draw_centered_circle(circle_radius, turtle):
    """
    A helper function to make the circle fractal easier to
    draw with turtle. It draws a circle of size circle_radius
    centered at the current turtle location.
    :param circle_radius: The radius of the circle
    :param turtle: The Python turtle to draw the circle.
    :return: None
    """

    turtle.penup()
    turtle.forward(circle_radius)
    turtle.left(90)
    turtle.pendown()
    turtle.circle(circle_radius)
    turtle.penup()
    turtle.right(90)
    turtle.backward(circle_radius)
    turtle.penup()

def draw_circles(circle_radius, turtle):
    """
    Draw a big circle with three half-sized circles up, left,
    and right of the big circle. Return the turtle to its
    original location and heading.

    :param circle_radius: The radius of the center circle
    :param turtle: The Python turtle to draw.
    :return: None.
    """
    draw_centered_circle(circle_radius, turtle)
    turtle.left(90)
    turtle.forward(circle_radius * 1.5)
    draw_centered_circle(circle_radius * 0.5, turtle)
    turtle.backward(circle_radius * 1.5)
    turtle.right(180)
    draw_centered_circle(circle_radius * 0.5, turtle)
    turtle.backward(circle_radius * 1.5)
    turtle.left(90)
    turtle.forward(circle_radius * 1.5)
    draw_centered_circle(circle_radius * 0.5, turtle)
    turtle.backward(circle_radius * 1.5)


def draw_spiral_recursive(start_length, end_length, turtle):
    """
    Draws a square spiral with a starting side length of start_length
    centered at the current turtle location.
    Runs recursively till the start_length is greater then the end_length
    and increases by 5 each time that it runs.

    :param start_length: The starting length of the spiral
    :param end_length: The length of the last side of the square spiral
    :param turtle: A python turtle
    :return: None
    """
    if start_length > end_length:  # Base case
        return
    turtle.forward(start_length)
    turtle.left(90)
    draw_spiral_recursive(start_length + 5, end_length, turtle)  # Adds 5 to the size of the wall each run through


def draw_fractal_circles(circle_radius, turtle):
    """
    Draws a Circle with 3 circles half it's length to the left, forward, and right of the circle
    Runs recursively till the radius of the circle is less than 2
    :param circle_radius: The radius of the center of the circle
    :param turtle: A python turtle
    :return: None
    """
    if circle_radius < 2:  # Base Case
        return

    draw_centered_circle(circle_radius, turtle)  # Main Circle
    turtle.left(90)
    turtle.forward(circle_radius * 1.5)
    draw_fractal_circles(circle_radius*.5, turtle)  # Draws a fractal circles of .5 radius to the left
    turtle.backward(circle_radius * 1.5)
    turtle.right(180)
    turtle.forward(circle_radius * 1.5)
    draw_fractal_circles(circle_radius * .5, turtle)  # Draws a fractal circles of .5 radius to the right
    turtle.backward(circle_radius * 1.5)
    turtle.left(90)
    turtle.forward(circle_radius* 1.5)
    draw_fractal_circles(circle_radius * .5, turtle)  # Draws a fractal circles of .5 radius straight ahead
    turtle.backward(circle_radius * 1.5)



def main():
    """
    Provide code to setup and test the spiral and circle
    fractal code.
    :return: None.
    """
    # Set up the turtle and window
    recursive_turtle = turtle.Turtle()
    recursive_turtle.speed(0)
    myWin = turtle.Screen()
    recursive_turtle.penup()
    recursive_turtle.left(90)
    recursive_turtle.backward(100)

    # Draw the spiral
    recursive_turtle.pendown()
    # draw_spiral(5, 200, recursive_turtle)
    draw_spiral_recursive(5, 200, recursive_turtle)

    # Draw the circles
    recursive_turtle.penup()
    recursive_turtle.goto(0, 100)
    recursive_turtle.setheading(90)
    # draw_circles(40, recursive_turtle)
    draw_fractal_circles(40, recursive_turtle)

    myWin.exitonclick()

if __name__ == "__main__":
    main()
