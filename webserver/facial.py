from PIL import Image
import face_recognition
import os, csv
import numpy as np
from numpy import savetxt
import pickle
import json
import shutil

all_face_encodings = {}
current_face_encodings = {}

# Opens dataset_faces.dat" if it exists #
if os.path.exists('./webserver/dataset_faces.dat'):
    with open('./webserver/dataset_faces.dat', 'rb') as f:
        current_face_encodings = pickle.load(f)


i = 1
directory = './webserver/public/images/'

# Loops through all files and directories inside images folder #
for subdir, dirs, files in os.walk(directory):
    for file in files:
        # Checks if file is .txt - .txt file is used to keep images folder on git #
        if file.endswith('.txt'):
            print(file)
        else:
            print((os.path.join(subdir, file)))
            # Reads measurements from photo
            image = face_recognition.load_image_file(os.path.join(subdir, file))
            folderName = os.path.basename(subdir)
            # Creates a key (folder name) with the measurements from the photos
            current_face_encodings[folderName] = face_recognition.face_encodings(image)[0]

# Dumps encodings and measurements to the .dat file #     
with open('./webserver/dataset_faces.dat', 'wb') as f:
    pickle.dump(current_face_encodings, f)
 
# Deletes all photos # 
if os.path.basename(subdir) != "images":
    print (subdir)
    shutil.rmtree(subdir) 

