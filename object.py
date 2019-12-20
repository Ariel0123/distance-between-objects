import numpy as np
import cv2
import math

img = cv2.imread("test.jpg")

color_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

red_1 = np.array([155,25,0])
red_2 = np.array([179,255,255])

mask = cv2.inRange(color_hsv, red_1, red_2)

c, h = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

coord = []

for i in c:
    x1, y1, x2, y2 = cv2.boundingRect(i)
    cv2.rectangle(img, (x1, y1), (x1+x2, y1+y2), (255,0,0), 2)

    cc = x1, y1, x2, y2

    coord.append(cc)

    center_f = (int(x1 + x2/2), int(y1+y2/2))

    center = cv2.circle(img,  center_f, 3, (255, 0, 0), 2)

x_1, y_1 = (int(coord[0][0]+coord[0][2]/2), int(coord[0][1]+coord[0][3]/2))
x_2, y_2 = (int(coord[1][0]+coord[1][2]/2), int(coord[1][1]+coord[1][3]/2))

d  = cv2.line(img, (x_1, y_1), (x_2, y_2), (0,255,0), 2)


print(x_1, y_1)
print(x_2, y_2)


distance = math.sqrt(((x_1-x_2)**2)+((y_1-y_2)**2))


result = "Distance: {0:.2f}".format(distance)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, result, (15,28) , font, 1, (0, 255, 0), 2, cv2.LINE_AA)


cv2.imshow("image", img)


cv2.waitKey(0)
cv2.destroyAllWindows()