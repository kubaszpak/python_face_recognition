import cv2

def main():
    cv2.namedWindow("output", cv2.WINDOW_NORMAL)        # Create window with freedom of dimensions
    im = cv2.imread("resources/face1.jpg")              # Read image
    imS = cv2.resize(im, (200, 200))                    # Resize image
    cv2.imshow("output", imS)                           # Show image
    cv2.waitKey(0)                                      # Display the image infinitely until any keypress

if __name__ == "__main__":
    main()