import cv2
import os
import sys

if(len(sys.argv)) != 2:
    print("Missing arguments! Use testimg.py <imgname.ext>")
    exit()



vidname = sys.argv[1]
vid = cv2.VideoCapture(vidname)

try:
    if not os.path.exists('data'):
        os.makedirs('data')

except OSError:
    print('Error: creating directory.')

currentframe = 0

while(True):

    ret,frame = vid.read()

    if ret:
        name = './data/frame' + str(currentframe).zfill(5)+ '.jpg'
        print('Creating...' + name)

        cv2.imwrite(name, frame)

        currentframe += 1
    else:
        break

vid.release()
cv2.destroyAllWindows()