import cv2
import numpy as np
import pyvirtualcam
from pyvirtualcam import PixelFormat

from face_detector import image_transform

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
                img = image_transform(img)
                cam.send(img)
                cam.sleep_until_next_frame()

    cap.release()


if __name__ == "__main__":
    main()
