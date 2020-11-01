import sys
import os
from time import sleep
import PIL
from PIL import Image

if(len(sys.argv)) < 2:
    print("Missing arguments! Use testimg.py [-f] <imgname.ext> ")
    exit()

def convertToNum(rgb):
    tot = 0
    for i in range(0, len(rgb)-1):
        tot = tot + rgb[i]
    tot = tot/(len(rgb)-1)
    return tot

def convertToAscii(imageName):    
    imagename = imageName
    im = Image.open(imagename, 'r')
    im.thumbnail((128,128),Image.ANTIALIAS)
    #im.convert('1')

    pix_val = list(im.getdata())
    width, height = im.size

    p = 1
    for x in range(0, height):
        p=0
        for y in range(0, width):
            if(x%2) == 0:
                #if(y%2) == 0:
                    if(convertToNum(im.getpixel((y,x)))) < 25.6:
                        print(" ", end='')
                    elif(convertToNum(im.getpixel((y,x)))) < 51.2:
                        print("'", end='')
                    elif(convertToNum(im.getpixel((y,x)))) < 76.8:
                        print('"', end='')
                    elif(convertToNum(im.getpixel((y,x)))) < 102.4:
                        print(":", end='')
                    elif(convertToNum(im.getpixel((y,x)))) < 128:
                        print("<", end='')
                    elif(convertToNum(im.getpixel((y,x)))) < 153.6:
                        print("]", end='')
                    elif(convertToNum(im.getpixel((y,x)))) < 179.2:
                        print("?", end='')
                    elif(convertToNum(im.getpixel((y,x)))) < 204.8:
                        print("#", end='')
                    elif(convertToNum(im.getpixel((y,x)))) < 230.4:
                        print("%", end='')
                    elif(convertToNum(im.getpixel((y,x)))) < 256:
                        print("@", end='')
                    p=1
        if p==1:
            print("")


def photoToMovie(srcDir):
    count = 0
    for image_path in os.listdir(srcDir):
        if(count%3) == 0:
            pathToImg = srcDir + '/' + image_path
            os.system('clear')
            convertToAscii(pathToImg)
            #sleep(.025)
        count += 1


if(len(sys.argv)) == 3:
    if(sys.argv[1]) == "-f":
        photoToMovie(sys.argv[2])
    else:
        print("Usage: testimg.py [-f] <folder to images or imagename.src> 2")
        exit()
elif(len(sys.argv)) == 2:
    if((sys.argv[1]) == '-f') or ((sys.argv[1]) == '-F') or ((sys.argv[1]) == '/f') or ((sys.argv[1]) == '/F'):
        print("Usage: testimg.py [-f] <folder to images or imagename.src> 1")
        exit()
    else:
        convertToAscii(sys.argv[1])

