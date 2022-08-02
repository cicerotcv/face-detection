from time import time

import cv2
import numpy as np

from utils import frame_to_image, grid_to_image, image_to_blur, image_to_red

face_cascade = cv2.CascadeClassifier('./src/h_cascade_frontalface.xml')


def image_transform(img):
    image_copy = img.copy()
    gray = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)
    detections = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in detections:
        image_to_red(image_copy, x, y, w, h)
        image_to_blur(image_copy, x, y, w, h, factor=35)
        frame_to_image(image_copy, x, y, w, h)
        grid_to_image(image_copy, x, y, w, h, number=5)

    return image_copy


def main():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 15)

    while True:
        _, img = cap.read()

        img = image_transform(img)

        cv2.imshow("Face", img)

        if cv2.waitKey(100) == ord('p'):
            cv2.imwrite(f"./src/screenshots/{int(time())}.png", img, )
        if cv2.waitKey(30) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
