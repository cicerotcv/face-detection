from sys import argv

import cv2

from face_detector import image_transform

if __name__ == "__main__":
    src = argv[1]
    img = cv2.imread(src)
    img = image_transform(img)
    cv2.imwrite("output.png", img)
    img = cv2.resize(img, (img.shape[1]//8, img.shape[0]//8))
    cv2.imshow("img", img)
    cv2.waitKey(0)
