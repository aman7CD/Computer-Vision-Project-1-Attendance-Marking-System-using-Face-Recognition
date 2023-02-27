# Attendance-Marking-System-using-Face-Recognition
Used dlib, face_recognition , opencv-python, to detect and identify faces and then mark attendance in a text file.
## About the Project

### Understand the Working of Face Recognition
1. Firstly pass the person’s picture to the model and their name.
2. The model takes every picture, converts them into some numerical encoding, and stores them in a list and all the labels(names of persons) in another list.
3. In the Prediction Phase when a picture of an unknown person is passed to the model, recognition model converts the unfamiliar person’s Image into encoding.
4. After converting an unknown person’s Image into encoding, it tries to find the most similar encoding based on the distance parameter. From the stored encodings,  the encoding with the least  distance from the encoding of an unknown person will be the closest match.
After getting the closest match encoding, we take the index of that encoding from that list, use indexing and find the detected person’s name.
