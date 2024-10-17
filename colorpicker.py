# Clever Company Collage Creator
# Kelvin Bian, Edmond Niu, Max Brodsky
# 1/21/2021
# Code for RGB color picker

import cv2
import numpy as np
from PIL import Image


def getOneColor(): #this function creates the color picker GUI and returns the RGB value in a list format

    def nothing(x):
        pass

    # Create a black image, a window
    img = np.zeros((300, 512, 3), np.uint8)
    cv2.namedWindow('Press C to confirm color (3 times)') #User Instruction


    # create trackbars for color change
    cv2.createTrackbar(
        'R', 'Press C to confirm color (3 times)', 0, 255, nothing)
    cv2.createTrackbar(
        'G', 'Press C to confirm color (3 times)', 0, 255, nothing)
    cv2.createTrackbar(
        'B', 'Press C to confirm color (3 times)', 0, 255, nothing)

    # continuous loop until the "c" key is pressed upon which the location of the track bars is located and returned in a list format
    while(1):
        cv2.imshow('Press C to confirm color (3 times)', img)
        k = cv2.waitKey(1) & 0xFF == ord('c')
        # print(k)
        if k == True:
            break

        # get current positions of four trackbars
        r = cv2.getTrackbarPos('R', 'Press C to confirm color (3 times)')
        g = cv2.getTrackbarPos('G', 'Press C to confirm color (3 times)')
        b = cv2.getTrackbarPos('B', 'Press C to confirm color (3 times)')

    
        img[:] = [b, g, r]

    cv2.destroyAllWindows() #destroy windows
    rgb = [r, g, b]
    return rgb #returns a list


def getThreeColors(): #this function calls the colorpicker three times, returning a list of lists (3 colors)
    threeColors = []
    for i in range(0, 3):
        oneCol = getOneColor()
        threeColors.append(oneCol)
    return threeColors


def changeColorPicture():  # source: https://stackoverflow.com/questions/36468530/changing-pixel-color-value-in-pil/36468996
    #this function will create three copies of the template image and change the colors of them according to user decision

    colors = getThreeColors() #gets the colors (rgb)
    print("\nPlease stand by as we finish step 1 (might take a while). Do not close the program.")
    img = Image.open("images/originalPicture.png")  # path to image here
    img1 = img.copy() #makes image copy
    img2 = img.copy()
    img3 = img.copy()


    #loops through every pixel and changes the non white pixels to the user decided color
    for i in range(img.size[0]):  # for every pixel:
        for j in range(img.size[1]):
            if img.getpixel((i, j)) != (0, 0, 0, 0):  # white
                img1.putpixel(
                    (i, j), (colors[0][0], colors[0][1], colors[0][2], 255))

    for i in range(img.size[0]):  # for every pixel:
        for j in range(img.size[1]):
            if img.getpixel((i, j)) != (0, 0, 0, 0):  # white
                img2.putpixel(
                    (i, j), (colors[1][0], colors[1][1], colors[1][2], 255))

    for i in range(img.size[0]):  # for every pixel:
        for j in range(img.size[1]):
            if img.getpixel((i, j)) != (0, 0, 0, 0):  # white
                img3.putpixel(
                    (i, j), (colors[2][0], colors[2][1], colors[2][2], 255))

    img1.save('images/modified1.png') #saves the images
    img2.save('images/modified2.png')
    img3.save('images/modified3.png')


''' 
sources
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_trackbar/py_trackbar.html
https://hackprojects.wordpress.com/tutorials/opencv-python-tutorials/write-a-text-on-image-using-opencv-python/
'''
