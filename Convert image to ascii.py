import os
import cv2

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
    


def asciiConverter(file1,Framerate):
    img= cv2.imread(file1, cv2.IMREAD_GRAYSCALE)
    n_img=cv2.resize(img,(tSize[0], tSize[1]))
    print(convertion(n_img))

    
asciiConverter('Trialimgage.jpeg')