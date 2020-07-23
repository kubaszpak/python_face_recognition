import cv2


cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

def main():
    while True:
        success, img = cap.read()
        cv2.imshow("Video", img)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows() 

if __name__ == "__main__":
    main()