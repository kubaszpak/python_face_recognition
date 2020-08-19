from facerecognitionpy.recognizer import Recognizer
import cv2
import eel
import base64
# import sys
# # from importlib import reload

# # reload(recog)

# print(sys.path)

eel.init('web')


def generate_image(camera):
    while True:
        frame = camera.rec()
        yield frame


@eel.expose
def video_feed():
    camera = Recognizer()
    generator = generate_image(camera)
    for image in generator:
        blob = base64.b64encode(image)
        blob = blob.decode('utf-8')
        eel.updateImageSrc(blob)()

def main():
    eel.start('index.html', block=False)

    video_feed()
        
    while True:
        eel.sleep(1.0)

if __name__ == "__main__":
    main()