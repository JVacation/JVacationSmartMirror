from tkinter import *
from PIL import ImageTk, Image
import cv2
import csv
import face_recognition
import numpy as np
import pickle
from numpy import savetxt
import datetime
import time
import os.path

# Capture frames from Camera #
cap = cv2.VideoCapture(0)
medText = 28


# Initialise Variables for locations and encodings #
face_locations = []
face_encodings = []
face_names = []

# Security Path and time Ranges # 
image_path = "./security/"
start = datetime.time(10, 15)
end = datetime.time(11)



# Some code used from https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam_faster.py # 

class Cam(Frame):
    def __init__(self, parent, event_name="", *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.title = "Unknown"

        # Shows name of user being detected #
        self.infoText = "Recognising Face: "
        self.info = Label(self, text=self.infoText, font=('Helvetica', medText), fg="blue", bg="black")
        self.userName = Label(self, text=self.title, font=('Helvetica', medText), fg="white", bg="black")
        if event_name != "enable":
            self.info.pack(side=LEFT, anchor=W)
        self.userName.pack(side=TOP, anchor=CENTER)
        self.lmain = Label(self)

        # Enable camera preview (enabled from Mirror.py) #
        if event_name == "enable":
            self.lmain.pack(side=TOP) 
        self.video()
    
    def readUserName(self):
        return self.userName.cget("text")

    def video(self):
        process_this_frame = True
        # Reads pickle data from file that stores facial data # 
        with open('./webserver/dataset_faces.dat', 'rb') as f:
            all_face_encodings = pickle.load(f)
        known_face_encodings = np.array(list(all_face_encodings.values()))
        known_face_names = list(all_face_encodings.keys())

        # Open CV resizing and changing the colour of the frame #
        ret, frame = cap.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        if process_this_frame:
            # Reading face locations and encodings #
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_names = []
            name = "No User Detected"
            self.userName.config(text = name)
            # Checking if Face measurements match to ones in dataset_faces.dat #
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                self.userName.config(text = name)
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    self.userName.config(text = name)
                else:
                    # Unknown user detected during time range #
                    timestamp = datetime.datetime.now().time()
                    check = start <= timestamp <= end
                    # If user is unknown and the time is in the time range - Save the frame #
                    if check == True:
                        timestamp2 = datetime.datetime.now()
                        timestampStr = timestamp2.strftime("%d_%b_%Y__%H_%M_%S")
                        timestampStrFilePath = timestamp2.strftime("%d_%b_%Y")
                        directory = image_path + timestampStrFilePath + "/"
                        if not os.path.isdir(directory):
                            os.mkdir(directory)
                        filename = timestampStr + ".jpg"
                        filepath = os.path.join(directory, filename)
                        cv2.imwrite(filepath, frame)
                face_names.append(name)
        process_this_frame = not process_this_frame
        # Used for Camera preview #
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)   
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        self.lmain.imgtk = imgtk
        self.lmain.configure(image=imgtk)
        self.lmain.after(1, self.video)
    
        
       

    
    