import cv2
import numpy as np

RED = (0, 20, 200)


def image_to_red(img, x, y, w, h):
    sub_img = img[y:y+h, x:x+w, :3]
    red_rect = np.ones(sub_img.shape, dtype=np.uint8)
    red_rect[:, :, :] = RED
    res = cv2.addWeighted(sub_img, 0.5, red_rect, 0.5, 1.0)
    img[y:y+h, x:x+w, :] = res


def image_to_blur(img, x, y, w, h, factor=21):
    sub_img = img[y:y+h, x:x+w, :3]
    blur = cv2.GaussianBlur(sub_img, (factor, factor), 75)
    img[y:y+h, x:x+w, :] = blur


def frame_to_image(img, x, y, w, h):
    cx, cy = x + w//2, y + w//2
    dx, dy = w//10, h//10
    cv2.rectangle(img, (x, y), (x+w, y+h), RED, 1)


def grid_to_image(img, x, y, w, h, number=5, color=RED):
    number = (2*number + 1)//2
    for i in range(number):
        cv2.line(img, (x + w*(i + 1)//number, y + 1),
                 (x + w*(i + 1)//number, y + h), color, 1)
        cv2.line(img, (x + 1, y + h*(i + 1)//number),
                 (x + w, y + h*(i + 1)//number), color, 1)
