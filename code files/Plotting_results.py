import cv2
import numpy as np

width = 1125
height = 615
data = 255 * np.ones(shape=[height, width, 3], dtype=np.uint8)

file = open(r"clusterred_data.txt","r")
lines = file.readlines()
original = cv2.imread("data_plot.jpg")
offset0 = 0
offset1 = 114
offset2 = 454

cents = open("centers.txt","r")
cents = cents.readlines()
Cents = []
for i in range(1,len(cents)):
    Cents.append( [ float(cents[i].split(",")[0]) , float(cents[i].split(",")[1].strip())])


lg = (128,200,148)
red = (89,81,218)
dg = (69,153,71)
for i in range(1,len(lines)):
    x = float(lines[i].split(",")[0])
    y = float(lines[i].split(",")[1])
    clr = lines[i].split(",")[2].strip()

    if (x <= 30):
        X = int (( x / 30 )*offset1)
    elif (x<=60):
        X = offset1 + int (( (x - 30)/30)*(offset2-offset1))
    else:
        X = offset2 + int (( (x-60)/24) * 657)
    y = int(y)

    y = int((y/100)*height)
    y = height - y

    line_type = 1
    type = lines[i].split(",")[3].strip()
    if (clr == "red"):

        if (type == "0"):
            cv2.circle(data,(X,y),6,red,-1)
            cv2.circle(data, (X, y), 6, (0,0,0), line_type)
        elif (type == "1"):
            cv2.rectangle(data,(X-3,y-3),(X+3,y+3),red,-1)  # 6x6 square..
            cv2.rectangle(data, (X - 3, y - 3), (X + 3, y + 3), (0,0,0), line_type)
        elif (type == "2"):
            cv2.rectangle(data,(X-7,y-2),(X+7,y+2),red,-1)  # 8x4 rectangle..
            cv2.rectangle(data, (X - 7, y - 2), (X + 7, y + 2), (0,0,0), line_type)  # 8x4 rectangle..
        elif (type == "3"):
            cv2.rectangle(data,(X-2,y-7),(X+2,y+7),red,-1)  # 4X8 rectangle..
            cv2.rectangle(data, (X - 2, y - 7), (X + 2, y + 7), (0,0,0), line_type)  # 4X8 rectangle..
        elif (type == "4"):
            cv2.ellipse(data,(X,y),(10,3),0,0,360,red,-1)    #elipse
            cv2.ellipse(data, (X, y), (10, 3), 0, 0, 360, (0,0,0), line_type)  # elipse




    if (clr == "light green"):
        if (type == "0"):
            cv2.circle(data, (X, y), 6, dg, -1)
            cv2.circle(data, (X, y), 6, (0, 0, 0), line_type)
        elif (type == "1"):
            cv2.rectangle(data, (X - 3, y - 3), (X + 3, y + 3), lg, -1)  # 6x6 square..
            cv2.rectangle(data, (X - 3, y - 3), (X + 3, y + 3), (0, 0, 0), line_type)
        elif (type == "2"):
            cv2.rectangle(data, (X - 7, y - 2), (X + 7, y + 2), lg, -1)  # 8x4 rectangle..
            cv2.rectangle(data, (X - 7, y - 2), (X + 7, y + 2), (0, 0, 0), line_type)  # 8x4 rectangle..
        elif (type == "3"):
            cv2.rectangle(data, (X - 2, y - 7), (X + 2, y + 7), lg, -1)  # 4X8 rectangle..
            cv2.rectangle(data, (X - 2, y - 7), (X + 2, y + 7), (0, 0, 0), line_type)  # 4X8 rectangle..
        elif (type == "4"):
            cv2.ellipse(data, (X, y), (10, 3), 0, 0, 360, lg, -1)  # elipse
            cv2.ellipse(data, (X, y), (10, 3), 0, 0, 360, (0, 0, 0), line_type)  # elipse

    if (clr == "dark green"):

        if (type == "0"):
            cv2.circle(data, (X, y), 6, dg, -1)
            cv2.circle(data, (X, y), 6, (0, 0, 0), line_type)
        elif (type == "1"):
            cv2.rectangle(data, (X - 3, y - 3), (X + 3, y + 3), dg, -1)  # 6x6 square..
            cv2.rectangle(data, (X - 3, y - 3), (X + 3, y + 3), (0, 0, 0), line_type)
        elif (type == "2"):
            cv2.rectangle(data, (X - 7, y - 2), (X + 7, y + 2), dg, -1)  # 8x4 rectangle..
            cv2.rectangle(data, (X - 7, y - 2), (X + 7, y + 2), (0, 0, 0), line_type)  # 8x4 rectangle..
        elif (type == "3"):
            cv2.rectangle(data, (X - 2, y - 7), (X + 2, y + 7), dg, -1)  # 4X8 rectangle..
            cv2.rectangle(data, (X - 2, y - 7), (X + 2, y + 7), (0, 0, 0), line_type)  # 4X8 rectangle..
        elif (type == "4"):
            cv2.ellipse(data, (X, y), (10, 3), 0, 0, 360, dg, -1)  # elipse
            cv2.ellipse(data, (X, y), (10, 3), 0, 0, 360, (0, 0, 0), line_type)  # elipse

    for z in range (len(Cents)):
        x = Cents[z][0]
        y = Cents[z][1]
        if (x <= 30):
            X = int((x / 30) * offset1)
        elif (x <= 60):
            X = offset1 + int(((x - 30) / 30) * (offset2 - offset1))
        else:
            X = offset2 + int(((x - 60) / 24) * 657)
        y = int(y)

        y = int((y / 100) * height)
        y = height - y

        cv2.circle(data, (X,y), 14, (0,0,0), -1)
        cv2.circle(data, (X,y), 14, (0, 0, 0), line_type)

    cv2.line(data,(offset1,0),(offset1,height),(0,0,0),1)
    cv2.line(data, (offset2, 0), (offset2, height), (0, 0, 0), 1)
cv2.imshow("Original:",original)
cv2.imshow("Results:",data)
cv2.waitKey(0)