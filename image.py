# Clever Company Collage Creator
# Kelvin Bian, Edmond Niu, Max Brodsky
# 1/21/2021
# Main file to apply our effect to image

import PIL
import os.path
import PIL.ImageDraw
from PIL import Image, ImageFont, ImageDraw
import numpy as np
from colorpicker import changeColorPicture, getOneColor

# Main function that adds our effect to image


def main():
    # Gather three RGB values from user to pass as paramters; creates three different versions of original image
    print("Welcome to Clever Company Collage Creator! Check out the readme for instructions before beginning. Select your company logo image and place it in the appropriate place. You will now need to select the three colors for your finished, modified logo.")
    changeColorPicture()
    # Store filtered images as RGBA images in variables
    im1 = Image.open("images/modified1.png").convert("RGBA")
    im2 = Image.open("images/modified2.png").convert("RGBA")
    im3 = Image.open("images/modified3.png").convert("RGBA")
    # Store length and width of image into variables
    l, w = im1.size
    # Gather company name, desired font size, font style, and text color. Create an image with text with these parameters
    print("\nSuccess! Now you will need to input your company name and its specifications.")
    text = input('Enter company name: ')
    fontsize = int(input(
        '\nEnter fontsize (if your picture is small choose a smaller fontsize or text will be cut off): '))
    print("\nNow you can choose font style: 1-bold, 2-bold italic, 3-italic, and 4-regular.")
    fontFam = int(input('Enter font style (number from 1-4): '))
    print("\nNow you can choose the color of the company text with this color picker. NOTE: we do not support the color black.")
    textColor = getOneColor()
    print("\nPlease stand by as we finish step 2. This may take a while")
    createText(text, fontsize, fontFam, textColor, l, w)
    # Store text image as RGBA image in variable
    im4 = Image.open("images/company_text.png").convert("RGBA")
    # creating blank images to paste real images on
    red = PIL.Image.new("RGBA", (l, w), color=(255, 255, 255, 0))
    blue = red.copy()
    yellow = red.copy()
    # paste images on blank image at slightly different offsets
    red.paste(im2, (int(l/7), int(w/7)), im2)
    yellow.paste(im1, (0, 0), im1)
    blue.paste(im3, (int(-l/7), int(w/7)), im3)
    # combine images
    final = Image.blend(red, blue, 0.5)
    final.paste(yellow, (0, 0), yellow)
    # change alpha of entire image
    final = changeAlpha(final, 150)
    # paste company text on center of image
    l1, w1 = im4.size
    final.paste(im4, (int(l/2)-int(l1/2), int(w/2)-int(w1/2)), im4)
    # Display resulting image and save final image to images folder
    final.show()
    final.save("images/finalimg.png")
    print("\nHere is your product. Hope you enjoy!")

    # Creates an image with text and saves the image to images folder


def createText(text, fontsize, fontFam, colorText, l, w):
    # Choosing font style
    if fontFam == 1:
        font = ImageFont.truetype("fonts/AnonymousPro-Bold.ttf",
                                  fontsize, encoding="unic")
    elif fontFam == 2:
        font = ImageFont.truetype("fonts/AnonymousPro-BoldItalic.ttf",
                                  fontsize, encoding="unic")
    elif fontFam == 3:
        font = ImageFont.truetype("fonts/AnonymousPro-Italic.ttf",
                                  fontsize, encoding="unic")
    elif fontFam == 4:
        font = ImageFont.truetype("fonts/AnonymousPro-Regular.ttf",
                                  fontsize, encoding="unic")
    else:
        print("that was invalid. Try again")
        return

    # Creates blank image and draws text in center of image
    img = Image.new('RGBA', (l, w), color=(0, 0, 0, 0))
    d = ImageDraw.Draw(img, mode='RGBA')
    d.text((int(l/2), int(w/2)), text, fill=(
        colorText[0], colorText[1], colorText[2]), font=font, anchor="mm")
    # Save image
    img.save('images/company_text.png')

# Changes alpha value of all pixels to desired number except pixels with alpha 0 (completely transparent)


def changeAlpha(img, alpha):
    # Create list of editable pixel data from image
    data = list(img.getdata())
    l, w = img.size
    newdata = [0]*(l*w)
    for i in range(l*w):
        newdata[i] = list(data[i])
    # Change each pixel's alpha to desired amount if pixel doesn't have alpha of 0 beforehand
    for i in range(l*w):
        if(newdata[i][3] != 0):
            newdata[i][3] = alpha
        newdata[i] = tuple(newdata[i])
    # Use data to form the final image
    result = PIL.Image.new("RGBA", (l, w), color=(255, 255, 255, 0))
    result.putdata(newdata)
    # Return the image with modified alpha
    return result


# Run the main function
main()
