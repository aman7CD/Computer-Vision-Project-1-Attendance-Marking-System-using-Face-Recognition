# Attendance-Marking-System-using-Face-Recognition
Used dlib, face_recognition , opencv-python, to detect and identify faces and then mark attendance in a text file.
## About the Project

### Working of the Project
1. Firstly I passed the person’s picture to the model and their name.
2. The model takes every picture, converts them into some numerical encoding, and stores them in a list and all the labels(names of persons) in another list.
3. In the Prediction Phase when a picture of an unknown person is passed to the model, recognition model converts the unfamiliar person’s Image into encoding.
4. After converting an unknown person’s Image into encoding, it tries to find the most similar encoding based on the distance parameter. From the stored encodings,  the encoding with the least distance from the encoding of an unknown person will be the closest match.
5. After getting the closest match encoding, I took the index of that encoding from that list, used indexing and find the detected person’s name.
6. Then I used file handling to store the name of the detected person and the time of his entry in the class.

### Libraries used in the Project
#### dlib
Dlib is one of the most powerful and easy-to-go open-source library consisting of machine learning library/algorithms and various tools for creating software. It was initially released in 2002.
Dlib is mostly used for face recognition purposes.It recognizes faces by estimating the location of 68 coordinates (x, y) that map the facial points on a person’s face . It analyzes the object/face using the functions called HOG (Histogram of oriented gradients) and CNN (Convolutional Neural Networks.

#### face_recognition
The face_recognition is a Python library and deep within, it employs dlib – a modern C++ toolkit that contains several machine learning algorithms.

#### openCV
OpenCV is a Python library that allows you to perform image processing and computer vision tasks. It provides a wide range of features, including object detection, face recognition, and tracking
