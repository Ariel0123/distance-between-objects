import numpy as np
import cv2
import math

video = cv2.VideoCapture('animation2.mov')

width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("output.mp4", fourcc, 30,(int(width), int(height)))

while True:
    ret, frame = video.read()


    color_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    red_1 = np.array([155,25,0])
    red_2 = np.array([179,255,255])

    mask = cv2.inRange(color_hsv, red_1, red_2)

    c, h = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    coord = []

    for i in c:
        x1, y1, x2, y2 = cv2.boundingRect(i)
        cv2.rectangle(frame, (x1, y1), (x1+x2, y1+y2), (255,0,0), 2)

        cc = x1, y1, x2, y2

        coord.append(cc)

        center_f = (int(x1 + x2/2), int(y1+y2/2))

        center = cv2.circle(frame,  center_f, 3, (255, 0, 0), 2)

    x_1, y_1 = (int(coord[0][0]+coord[0][2]/2), int(coord[0][1]+coord[0][3]/2))
    x_2, y_2 = (int(coord[1][0]+coord[1][2]/2), int(coord[1][1]+coord[1][3]/2))

    d  = cv2.line(frame, (x_1, y_1), (x_2, y_2), (0,255,0), 2)

    
    print(x_1, y_1)
    print(x_2, y_2)


    distance_pixel = math.sqrt(((x_1-x_2)**2)+((y_1-y_2)**2))

    result_pixel = "Pixel Distance: {0:.2f} pixels".format(distance_pixel)


    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, result_pixel, (15,28) , font, 1, (0, 255, 0), 2, cv2.LINE_AA)

    pixel = 2.54 / 110.5
    cm = distance_pixel * pixel

    result_cm = "Cm Distance: {0:.2f} cm".format(cm)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, result_cm, (15,58) , font, 1, (0, 255, 0), 2, cv2.LINE_AA)

    out.write(frame)
    cv2.imshow('Frame',frame)
 
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

 
video.release()
 
cv2.destroyAllWindows()
