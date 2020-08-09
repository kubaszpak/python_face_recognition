#making visual interface
import cv2
import os
import facerecognitionpy.face_train as face_train
import numpy as np

def get_next_photo_number(dir):
    number_list = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            path = os.path.join(root, file)
            base = os.path.basename(path)
            number_list.append(int(os.path.splitext(base)[0][-1]))
    if not number_list:
        return 0
    else:
        return max(number_list) + 1
                
def add_image_to_dir(image,dir):
    img_location = os.path.join(os.getcwd(),'resources/')
    direct_location = os.path.join(img_location,dir)
    next = get_next_photo_number(direct_location)
    new_file_location = os.path.join(direct_location,f'{dir}{next}.png')
    cv2.imwrite(new_file_location, image)

def reset_labels(label_ids, conf_counter):
    for key in label_ids:
        # conf_counter[key] = delay_value * (picture_list.count(key)-1) + 1
        conf_counter[key] = 1
    conf_counter[-1] = 1 # -1 stands for unknown person
    # print(label_ids, picture_list, conf_counter)

def rec():

    
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    cap.set(10,100)

    cascade_location = os.path.join(os.getcwd(),'cascades/haarcascade_frontalface_default.xml')
    faceCascade = cv2.CascadeClassifier(cascade_location)

    delay_value = 200
    conf_counter = {}
    label_ids, picture_list = face_train.train()
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainner.yml')
    reset_labels(label_ids, conf_counter)

    while cap.isOpened():
        success, img = cap.read()
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(imgGray,1.1,4)

        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h),(255,0,0),2)
            roi_color = img[y:y+h, x:x+w]
            roi_gray = imgGray[y:y+h , x:x+w]

            id_, conf = recognizer.predict(roi_gray)

            if(conf >= 70 and conf <= 95):
                # print(label_ids, picture_list, conf_counter, 'why')
                # print(id_)
                cv2.putText(img,label_ids[id_],(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)

                for key in label_ids:
                    if key != id_:
                        conf_counter[key] = 1

                if(conf_counter[id_] % delay_value == 0):
                    add_image_to_dir(roi_color, label_ids[id_])

                conf_counter[id_] += 1
                conf_counter[-1] = 1

            else:
                # print('unknown')

                if(conf_counter[-1] % delay_value == 0):
                    decision = input('Did a new person just show up? (y/n) ')
                    name = input('Then what is your name? ')
                    images_location = os.path.join(os.getcwd(),'resources/')
                    label_dir_location = os.path.join(images_location,name)
                    if decision == 'y':
                        if(not os.path.isdir(label_dir_location)):
                            os.makedirs(label_dir_location)
                        else:
                            print('Try different name, this one is probably taken ')
                            name = input('Enter different name: ')
                            label_dir_location = os.path.join(images_location,name)
                            os.makedirs(label_dir_location)

                    add_image_to_dir(roi_color, name)

                    # print(label_ids, picture_list, conf_counter, 'clear')
                    label_ids.clear()
                    picture_list.clear()
                    label_ids, picture_list = face_train.train()
                    new_roi = []
                    new_roi.append(roi_gray)
                    new_label = []
                    new_label.append(max(picture_list))
                    recognizer.update(new_roi, np.array(new_label))
                    # recognizer.read("trainner.yml")
                
                    reset_labels(label_ids, conf_counter)

                conf_counter[-1] += 1
                # print(label_ids, picture_list, conf_counter)
        cv2.imshow('Video', img)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows() 

if __name__ == "__main__":
    rec()