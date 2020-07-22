import cv2

def main():
    
    cap = cv2.videoCapture(0)
    while True:
        success, img = cap.read()
        


if __name__ == "__main__":
    main()