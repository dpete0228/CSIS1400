# CS 1400
# Assigment 6
# Written by David Johnson and

# This brings in functions from the graphics.py file
from graphics import *
from random import *


# Make a new image that moves the red intensity value of a pixel in the original image
# to the green part of a pixel, moves the green value to blue,
# and the blue value to red. An image that had a bright red part will end up with
# that part being bright green in the new image.
#
# Study the pattern of the loop inside a loop (called nested loops). Each time the first loop
# does a single repeat, the entire inner loop does all its repetitions.
#
# Look how to get the color at a pixel, change the color, and set the pixel to the new color.
# The assignment problems below will use these steps.
# This function returns a new image with changed colors. The code in main calls
# this function and draws the returned new image.
def switch_image_colors(image):
    # copy the image into an image the code will modify
    switched_image = image.clone()
    # The for x loop goes through all its iterations and then the for y loop goes down a row.
    for y in range(0, image.getHeight()):
        for x in range(0, image.getWidth()):
            # Each pixel has a location like an index in x and an index in y
            color = image.getPixel(x, y)
            # color is assigned a list with [red, green, blue] values each from 0-255.
            # color[0] is the red intensity, color[1] is green, color[2] is blue.
            new_color = [color[2], color[0], color[1]]
            # Set the pixel in the changed image to the new color
            switched_image.setPixel(x, y, new_color)
    # return the finished changed image
    return switched_image

# This function returns a new image with the colors changed to grayscale The code in main calls
# this function and draws the returned grayscale image.
def color_image_to_gray_scale(image):
    # copy the image into an image the code will modify
    gray_image = image.clone()
    # The for x loop goes through all its iterations and then the for y loop goes down a row.
    for y in range(0, image.getHeight()):
        for x in range(0, image.getWidth()):
            # Each pixel has a location like an index in x and an index in y
            color = image.getPixel(x, y)
            # color is assigned a list with [red, green, blue] values each from 0-255.
            # color[0] is the red intensity, color[1] is green, color[2] is blue.
            # converts to the gray version of the pixel using given conversions
            to_gray = int(color[0] * 0.299 + color[1] * 0.587 + color[2] * 0.114)
            new_color = [to_gray, to_gray, to_gray]
            # Set the pixel in the changed image to the new color
            gray_image.setPixel(x, y, new_color)
    # return the finished changed image
    return gray_image

# This function returns a new image with the colors changed to pure black and white
# The code in main calls this function and draws the returned black and white image.
def color_image_to_black_and_white(image, threshold):
    # copy the image into an image the code will modify
    bw_image = image.clone()
    # The for x loop goes through all its iterations and then the for y loop goes down a row.
    for y in range(0, image.getHeight()):
        for x in range(0, image.getWidth()):
            # Each pixel has a location like an index in x and an index in y
            color = image.getPixel(x, y)
            # color is assigned a list with [red, green, blue] values each from 0-255.
            # color[0] is the red intensity, color[1] is green, color[2] is blue.
            # converts to the gray version of the pixel using given conversions
            to_gray = int(color[0] * 0.299 + color[1] * 0.587 + color[2] * 0.144)
            # checks if the gray value is greater than the threshold paramater and
            # sets the gray to 0 (black) or 255 (white)
            # depending if it is above or below the threshold
            if to_gray >= threshold:
                to_gray = 255 #white
            else:
                to_gray = 0 #black
            new_color = [to_gray, to_gray, to_gray]
            # Set the pixel in the changed image to the new color
            bw_image.setPixel(x, y, new_color)
    # return the finished changed image
    return bw_image

# This function returns a new image with the colors changed to their photonegative
# The code in main calls this function and draws the returned photonegative image.
def photonegative_of_an_image(image):
    # copy the image into an image the code will modify
    photonegative_image = image.clone()
    # The for x loop goes through all its iterations and then the for y loop goes down a row.
    for y in range(0, image.getHeight()):
        for x in range(0, image.getWidth()):
            # Each pixel has a location like an index in x and an index in y
            color = image.getPixel(x, y)
            # color is assigned a list with [red, green, blue] values each from 0-255.
            # color[0] is the red intensity, color[1] is green, color[2] is blue.
            # sets to it's photonegative color by doing 255 - the intensity
            new_color = [255 - color[0], 255 - color[1], 255 - color[2]]
            # Set the pixel in the changed image to the new color
            photonegative_image.setPixel(x, y, new_color)
    # return the finished changed image
    return photonegative_image

def sepia_image(image):
    # copy the image into an image the code will modify
    converted_sepia_image = image.clone()
    # The for x loop goes through all its iterations and then the for y loop goes down a row.
    for y in range(0, image.getHeight()):
        for x in range(0, image.getWidth()):
            # Each pixel has a location like an index in x and an index in y
            # color is assigned a list with [red, green, blue] values each from 0-255.
            # color[0] is the red intensity, color[1] is green, color[2] is blue.
            color = image.getPixel(x, y)
            # converts to the sepia of each rgb by using the given conversions
            new_red = int((color[0] * 0.393 + color[1] * 0.769 + color[2] * 0.189))
            new_green = int((color[0] * 0.349 + color[1] * 0.686 + color[2] * 0.168))
            new_blue = int((color[0] * 0.272 + color[1] * 0.534 + color[2] * 0.131))
            # sets new_color to the new sepia version of the colors
            new_color = [new_red, new_green, new_blue]
            # checks to make sure that none of the rgb's are above 255 and sets
            # them to 255 if they are
            for rgb in range(3):
                if new_color[rgb] > 255:
                    new_color[rgb] = 255
            # Set the pixel in the changed image to the new color
            converted_sepia_image.setPixel(x, y, new_color)
    # return the finished changed image
    return converted_sepia_image


# This function returns a new image with the green screen image put onto the regular image
# The code in main calls this function and draws the green screen image over the regular image.
def green_screen_image(green_screen_image, regular_image):
    # copy the image into an image the code will modify
    added_green_screen_image = green_screen_image.clone()
    # The for x loop goes through all its iterations and then the for y loop goes down a row.
    for y in range(0, green_screen_image.getHeight()):
        for x in range(0, green_screen_image.getWidth()):
            # Each pixel has a location like an index in x and an index in y
            # green_check and normal_pixel is assigned a list with [red, green, blue]
            # with values each from 0-255.
            # [0] is red intensity, [1] is green intensity, and [2] is blue intensity
            green_check = green_screen_image.getPixel(x, y)
            normal_pixel = regular_image.getPixel(x,y)
            new_color = [green_check[0],green_check[1],green_check[2]]
            # checks to see if the green_screen_image has a pure green value
            # if it does it sets all of the pixels in this position to the regular image rgb
            if green_check[1] == 255 and green_check[0] == 0 and green_check[2] == 0:
                for rgb in range(3):
                    new_color[rgb] = normal_pixel[rgb]
            # Set the pixel in the changed image to the new color
            added_green_screen_image.setPixel(x, y, new_color)
    # return the finished changed image
    return added_green_screen_image

# This function draws a new image colored with pointllist.
def color_image_to_pointillist(image, win):
    # runs the pointllist 25000 times
    for count in range (25001):
        # chooses a random x and y in the image
        pixel_x=randint(0,image.getWidth()-1)
        pixel_y=randint(0,image.getHeight()-1)
        # color is assigned a list with [red, green, blue] values each from 0-255.
        # color[0] is the red intensity, color[1] is green, color[2] is blue.
        color = image.getPixel(pixel_x, pixel_y)
        # sets a circle at the random point with a radius 5
        circle=Circle(Point(pixel_x,pixel_y),5)
        # sets the color of the circle to the rgb of the point
        circle.setFill(color[0],color[1],color[2])
        circle.setWidth(0)
        # draws the circle
        circle.draw(win)

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
    arches_image = load_image("../../../../Downloads/Arches.png")
    cat_image = load_image("../../../../Downloads/green-screen-cat.png")

    # Set up the window using the image size
    win = GraphWin('Image Art',
                   arches_image.getWidth(),
                   arches_image.getHeight(),
                   autoflush=False)

    # Draw the original image and wait for a mouse click to move to the next step
    arches_image.draw(win)
    win.getMouse()

    # Make a new image with green intensity put in red, blue put in green, and red in blue.
    switched_image = switch_image_colors(arches_image)
    switched_image.draw(win)
    win.getMouse()

    # Test the grayscale
    gray_image = color_image_to_gray_scale(arches_image)
    gray_image.draw(win)
    gray_image.save("gray.png")
    win.getMouse()

    # # Test the black and white
    bw_image = color_image_to_black_and_white(arches_image, 100)
    bw_image.draw(win)
    bw_image.save("bw.png")
    win.getMouse()

    # Test the photonegative
    photonegative_image = photonegative_of_an_image(arches_image)
    photonegative_image.draw(win)
    photonegative_image.save("photonegative.png")
    win.getMouse()

    # Test the sepia
    sepia = sepia_image(arches_image)
    sepia.draw(win)
    sepia.save("sepia.png")
    win.getMouse()

    # Make a merged image between a green screen image and a background
    merged_image = green_screen_image(cat_image, arches_image)
    merged_image.draw(win)
    merged_image.save("merged.png")
    win.getMouse()

    # Test the pointillist function. It is just drawn on the window. You will need to
    # screen capture the image to save it for submitting.
    color_image_to_pointillist(arches_image, win)
    win.getMouse()

    win.close()


# Execute main when this file is run.
if __name__ == "__main__":
    main()
