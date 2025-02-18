# CS 1400
# Lab 7

# This brings in functions from the graphics.py file
from graphics import *
from random import *


# Make a new image that keeps a color at a pixel if it is mostly red and otherwise sets it
# to black.
def keep_red_part_of_image(image):
    # copy the image into an image the code will modify
    red_image = image.clone()
    # The for x loop goes through all its iterations and then the for y loop goes down a row.
    for y in range(0, image.getHeight()):
        for x in range(0, image.getWidth()):
            # Each pixel has a location like an index in x and an index in y
            color = image.getPixel(x, y)


            # color is assigned a list with [red, green, blue] values each from 0-255.
            # color[0] is the red intensity, color[1] is green, color[2] is blue.
            # Add an if statement to set new_color to color when color has a
            # reasonable intensity of red and also the intensity of red is greater
            # than the intensity of green and also the intensity of blue.
            if color[0] > 150 and color[0] > color[1] and color[0] > color [2]:
                new_color = color
            else:
                new_color = [0,0,0]


            # Set the pixel in the changed image to the new color
            red_image.setPixel(x, y, new_color)
    # return the finished changed image
    return red_image


# This function loads the image file called filename and centers it in the window.
# The image is returned so it can be drawn.
def load_image(filename):
    # Load the image
    image = Image(Point(0, 0), filename)
    # Center it
    image.move(int(image.getWidth() / 2), int(image.getHeight() / 2))
    return image


def main():
    # Load the image first, so we know how big to make the window.
    arches_image = load_image("Arches.png")

    # Set up the window using the image size
    win = GraphWin('Image Art',
                   arches_image.getWidth(),
                   arches_image.getHeight(),
                   autoflush=False)

    # Draw the original image and wait for a mouse click to move to the next step
    arches_image.draw(win)
    win.getMouse()

    # Call the function to keep red parts of an image and draw it
    red_image = keep_red_part_of_image(arches_image)
    red_image.draw(win)
    win.getMouse()

    win.close()


# Execute main when this file is run.
if __name__ == "__main__":
    main()
