import os
import cv2
import time

x=input('enter video file name: ')

ascii = ['@', '$', '#', '*', '!', '=', ';', ':', '~', '-', '.', ' ']
tSize=os.get_terminal_size()

def pixel_type(p):
    return ascii[p//22]
    
def convertion(img):
    ascii_img=[]
    for i in img:
        asChar=[pixel_type(pix) for pix in i]
        asRow=''.join(asChar)
        ascii_img.append(asRow)

    return '\n'.join(ascii_img)


def vid_to_ascii(file0, framerate=0):
    vid=cv2.VideoCapture(file0)
    while vid.isOpened():
        boo, frame = vid.read()
        if not boo:
            break

        n_frame=cv2.resize(frame,(tSize[0], tSize[1]))
        grey=cv2.cvtColor(n_frame, cv2.COLOR_BGR2GRAY)
        print("\033[H\033[J", end="")
        print(convertion(grey))

        if framerate>0:
            time.sleep(1/framerate)

        if cv2.waitKey(1)== ord('w'):
            break

    vid.release()
    cv2.destroyAllWindows


vid_to_ascii(x,60)