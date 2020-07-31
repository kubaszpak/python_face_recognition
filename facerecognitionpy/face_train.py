import os
from PIL import Image
import numpy as np
import cv2

def train():
    base_dir = os.getcwd()
    image_dir = os.path.join(base_dir,'resources')

    cascade_location = os.path.join(base_dir,'cascades/haarcascade_frontalface_default.xml')
    faceCascade = cv2.CascadeClassifier(cascade_location)
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    current_id = 0
    label_ids = {}
    x_train = []
    y_train = []

    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith('.png') or file.endswith('.jpg'):
                path = os.path.join(root,file)
                label = os.path.basename(root).replace(" ","-").lower()
                if not label in label_ids.values():
                    label_ids[current_id] = label
                    current_id+=1
                pil_image = Image.open(path).convert('L')
                size = (550,550)
                final_image = pil_image.resize(size, Image.ANTIALIAS)
                image_array = np.array(final_image,'uint8')
                faces = faceCascade.detectMultiScale(image_array,1.1,4)

                for (x,y,w,h) in faces:
                    roi = image_array[y:y+h,x:x+w]
                    x_train.append(roi)
                    y_train.append(current_id-1)

    recognizer.train(x_train, np.array(y_train))
    recognizer.save('trainner.yml')

    return label_ids, y_train