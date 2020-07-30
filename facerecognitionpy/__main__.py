import cv2
import os
import facerecognitionpy.face_train as face_train


cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

cascade_location = os.path.join(os.getcwd(),'cascades/haarcascade_frontalface_default.xml')
faceCascade = cv2.CascadeClassifier(cascade_location)

def main():
    delay_value = 100
    conf_counter = {}
    label_ids, picture_list = face_train.train()
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("trainner.yml")
    for key in label_ids:
        conf_counter[key] = 1
        conf_counter[key] += delay_value * picture_list.count(key)
    conf_counter[-1] = 1 # -1 stands for unknown person
    while True:
        success, img = cap.read()
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(imgGray,1.1,5)

        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h),(255,0,0),2)
            roi_color = img[y:y+h , x:x+w]
            roi_gray = imgGray[y:y+h , x:x+w]

            id_, conf = recognizer.predict(roi_gray)
            if(conf >= 60 and conf < 90):
                print(label_ids[id_],conf)
                for key in conf_counter:
                    if key != id_:
                        conf_counter[key] = 1
                if(conf_counter[id_] % delay_value == 0):
                    img_location = os.path.join(os.getcwd(),'resources/')
                    my_face = os.path.join(img_location,label_ids[id_])
                    my_face_file = os.path.join(my_face,f'{label_ids[id_]}{conf_counter[id_]//delay_value}.png')
                    cv2.imwrite(my_face_file, roi_color)
                conf_counter[id_] += 1
                conf_counter[-1] = 1
            else:
                print('unknown')

                if(conf_counter[-1] % delay_value == 0):
                    decision = input('Did a new person just show up? (y/n)')
                    img_location = os.path.join(os.getcwd(),'resources/')
                    name = input('Then what is your name?')
                    my_face = os.path.join(img_location,name)
                    if decision == 'y':
                        try:
                            os.makedirs(my_face)
                        except:
                            print('Try different name this one is probably taken')
                            my_face = os.path.join(img_location,name)
                            os.makedirs(my_face)
                    my_face_file = os.path.join(my_face,f'{name}0.png')
                    cv2.imwrite(my_face_file, roi_color)
                    label_ids, picture_list = face_train.train()
                    recognizer.read("trainner.yml")
                    for key in label_ids:
                        conf_counter[key] = 1
                        conf_counter[key] += delay_value * picture_list.count(key)
                    conf_counter[-1] = 1 # -1 stands for unknown person 
                conf_counter[-1] += 1
        cv2.imshow('Video', img)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows() 

if __name__ == "__main__":
    main()