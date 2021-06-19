import cv2
import numpy as np
import pyvirtualcam
from pyvirtualcam import PixelFormat

from utils import aim_to_image, image_to_blur, image_to_red

face_cascade = cv2.CascadeClassifier('./src/h_cascade_frontalface.xml')


def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise RuntimeError('Could not open video source')

    pref_width = 1280
    pref_height = 720
    pref_fps = 30

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, pref_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, pref_height)
    cap.set(cv2.CAP_PROP_FPS, pref_fps)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    with pyvirtualcam.Camera(width, height, fps, fmt=PixelFormat.BGR) as cam:
        print('Virtual camera device: ' + cam.device)

        while True:
            ret, img = cap.read()

            if ret:
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                detections = face_cascade.detectMultiScale(gray, 1.1, 4)

                for (x, y, w, h) in detections:
                    image_to_red(img, x, y, w, h)
                    image_to_blur(img, x, y, w, h, factor=55)
                    aim_to_image(img, x, y, w, h)

                cam.send(img)
                cam.sleep_until_next_frame()

    cap.release()


if __name__ == "__main__":
    main()
