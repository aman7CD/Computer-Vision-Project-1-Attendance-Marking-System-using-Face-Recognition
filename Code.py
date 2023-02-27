
import os
import cv2
import face_recognition
import numpy as np
from datetime import datetime


name1 = list()
names = []
list_of_known_face_encodings = list()

path = "images"
name_wth_ext = os.listdir(path)
#print(n_wth_ext)
for i in name_wth_ext:
    name = os.path.splitext(i)
    names.append(name[0].upper())
#print(names)


for i in name_wth_ext:
    img = cv2.imread(f"images/{i}")
    face_encoding = face_recognition.face_encodings(img)
    list_of_known_face_encodings.append(face_encoding[0])
#print(list_of_face_encoding)

def mark_attendence(name):
    with open("Attendence.txt", "r+") as f:
        af = f.readlines()
        for line in af:
            b = line.split(",")
            name1.append(b[0])
        if names[index] not in name1:
            now = datetime.now()
            entry_time = now.strftime("%H:%M:%S")
            f.writelines(f"{names[index]},{entry_time}")
            f.write("\n")




cap = cv2.VideoCapture(0)
cap.set(3,1080)
cap.set(4,1080)

while True:
    success,new_img = cap.read()
    face_loc = face_recognition.face_locations(new_img)
    # print(face_loc)
    if len(face_loc)!=0:
        new_face_encoding = face_recognition.face_encodings(new_img)
        distance = face_recognition.face_distance(list_of_known_face_encodings,
                                              new_face_encoding[0])
        # print(distance)
        index = np.argmin(distance)
        # print(index)

        if distance[index] < 0.5:
            y1, x2, y2, x1 = face_loc[0]
            cv2.rectangle(new_img, (x1, y1), (x2, y2), (0, 0, 210), 2)
            cv2.rectangle(new_img, (x1, y2 - 30), (x2, y2), (0, 0, 210), cv2.FILLED)
            cv2.putText(new_img, f"{names[index]}", (x1, y2 - 5),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
            new_name = names[index].upper()
            mark_attendence(new_name)

    cv2.imshow("Attendence Window",new_img)
    cv2.waitKey(1)
