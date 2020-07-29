import os
from PIL import Image
import numpy as np
import cv2

base_dir = os.getcwd()
image_dir = os.path.join(base_dir,'resources')

cascade_location = os.path.join(base_dir,'cascades/haarcascade_frontalface_default.xml')
faceCascade = cv2.CascadeClassifier(cascade_location)
recognizer = cv2.face.LBPHFaceRecognizer_create()

# current_id = 0
labels_ids = {}
y_train = []
x_train = []

def train():
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith('.png') or file.endswith('.jpg'):
                path = os.path.join(root,file)
                label = os.path.basename(root)
                # print(label, path)
                pil_image = Image.open(path).convert('L')
                image_array = np.array(pil_image,'uint8')
                faces = faceCascade.detectMultiScale(image_array,1.1,5)

                for (x,y,w,h) in faces:
                    roi = image_array[y:y+h,x:x+w]
                    x_train.append(roi)
                    y_train.append(label)

    recognizer.train(x_train, y_train)
    recognizer.save('trainner.yml')