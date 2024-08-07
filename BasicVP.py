import cv2
# Uncomment the commented lines(except this one) to write all frames in a directory
#  import os

#d='IndiFrame'
#os.makedirs(d,exist_ok=True)
#f_num=0

vid=cv2.VideoCapture('video0.mp4')
while vid.isOpened():
    boo, frame = vid.read()

    if not boo:
        break

    rgb=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow('frame',rgb)

#    fname=os.path.join(d, f'frame_{f_num:04d}.jpg')
#    cv2.imwrite(fname,rgb)

    if cv2.waitKey(1)== ord('w'):
        break

#   f_num+=1

vid.release()
cv2.destroyAllWindows