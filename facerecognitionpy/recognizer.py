import cv2
import os
import facerecognitionpy.face_train as face_train
import numpy as np
from facerecognitionpy.rec_functions import *
import eel
from facerecognitionpy.files import *

cascade_location = 'cascades/haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascade_location)

# def check(value):
#     print("It is working " + value)


def get_value():
    eel.dealWithButtons()(helper)


def helper(value):
    print(value)


class Recognizer(object):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(10, 100)
        self.delay_value = 300
        self.conf_counter = {}
        self.label_ids = {}
        self.label_ids, self.picture_list = face_train.train()
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read('trainner.yml')
        reset_labels(self.label_ids, self.conf_counter)

    def __del__(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def rec(self):
        success, img = self.cap.read()
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_color = img[y:y+h, x:x+w]
            roi_gray = imgGray[y:y+h, x:x+w]

            id_, conf = self.recognizer.predict(roi_gray)
            print(id_, conf)

            if(conf >= 70 and conf <= 95):
                print(self.label_ids, self.picture_list,
                      self.conf_counter, 'why')
                # print(id_)
                cv2.putText(
                    img, self.label_ids[id_], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

                for key in self.label_ids:
                    if key != id_:
                        self.conf_counter[key] = 1

                if(self.conf_counter[id_] % self.delay_value == 0):
                    add_image_to_dir(roi_color, self.label_ids[id_])
                    self.conf_counter[id_] = 0
                    self.picture_list.append(id_)
                    self.picture_list.sort()

                self.conf_counter[id_] += 1
                self.conf_counter[-1] = 1

            else:
                # print('unknown')

                if(self.conf_counter[-1] % self.delay_value == 0):
                    eel.changeDisplay('wave-one')()
                    decision = None
                    while(decision is None):
                        decision = eel.dealWithButtons()()
                    print(decision)
                    eel.changeDisplay('wave-two')()
                    # eel.dealWithInput()()
                    name = None
                    while(name is None):
                        name = eel.getInput()()
                    print(name)
                    images_location = get_full_path('resources')
                    label_dir_location = os.path.join(images_location, name)
                    print(label_dir_location)
                    self.conf_counter.clear()
                    new_roi = []
                    new_roi.append(roi_gray)
                    new_label = []
                    if decision == False:
                        try:
                            os.makedirs(label_dir_location)
                        except:
                            raise Exception(
                                'There already exists a directory with this name')
                        new_label.append(max(self.picture_list) + 1)
                        self.picture_list.append(new_label[0])
                        self.label_ids[new_label[0]] = name.replace(
                            " ", "-").lower()
                    else:
                        newId = idOfName(name, self.label_ids)
                        if newId == None:
                            raise Exception(
                                'There is not a name like the one you have passed')
                        else:
                            new_label.append(newId)
                        self.picture_list.append(newId)
                        self.picture_list.sort()

                    # else:
                    #     os.makedirs(label_dir_location, exist_ok=True)
                    # else:
                    #     eel.changeDisplay('wave-two')()
                    #     eel.changePlaceHolderName('Enter different name: ')()
                    #     name = None
                    #     while(name is None):
                    #         name = eel.getInput()()
                    #     eel.changePlaceHolderName('Enter your name: ')()
                    #     label_dir_location = os.path.join(images_location,name)
                    #     os.makedirs(label_dir_location)
                    # print(label_ids, picture_list, conf_counter, 'clear')
                    # self.label_ids.clear()
                    # self.picture_list.clear()

                    self.recognizer.update(new_roi, np.array(new_label))
                    # self.recognizer.read("trainner.yml")

                    reset_labels(self.label_ids, self.conf_counter)

                    add_image_to_dir(roi_color, name)

                self.conf_counter[-1] += 1
                # print(label_ids, picture_list, conf_counter)
            break
        # cv2.imshow('Video', img)
        # key = cv2.waitKey(1) & 0xFF
        # if key == ord('q'):
        #     break
        ret, jpeg = cv2.imencode('.jpg', img)
        frame = jpeg.tobytes()
        return frame
