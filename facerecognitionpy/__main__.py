import cv2
import os


cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

cascade_location = os.path.join(os.getcwd(),'cascades/haarcascade_frontalface_default.xml')
faceCascade = cv2.CascadeClassifier(cascade_location)

def main():
    counter = 0
    while True:
        success, img = cap.read()
        imGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(imGray,1.1,4)

        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h),(255,0,0),2)
            roi_color = img[y:y+h , x:x+w]
            img_location = os.path.join(os.getcwd(),'resources/')
            my_face = os.path.join(img_location,'my/')
            os.makedirs(my_face,exist_ok=True)
            if(counter % 50 == 0):
                my_face_file = os.path.join(my_face,f'my_pic{counter//50}.png')
                cv2.imwrite(my_face_file, roi_color)
            counter += 1
        cv2.imshow('Video', img)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows() 

if __name__ == "__main__":
    main()