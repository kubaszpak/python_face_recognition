import cv2


cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

faceCascade = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")

def main():
    while True:
        success, img = cap.read()
        imGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(imGray,1.1,4)

        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h),(255,0,0),2)
            
        cv2.imshow("Video", img)
        # print(cv2.waitKey(1))
        key = cv2.waitKey(1) & 0xFF
        # print(key)
        # print(ord('q'))
        # print(ord('s'))
        if key == ord("s"):
            break
    cap.release()
    cv2.destroyAllWindows() 

if __name__ == "__main__":
    main()