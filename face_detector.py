import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('./src/h_cascade_frontalface.xml')
cap = cv2.VideoCapture(0)

# img = cv2.imread('')

while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    detections = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in detections:
        padding = 30
        sub_img = img[y:y+h, x:x+w, :3]

        red_rect = np.ones(sub_img.shape, dtype=np.uint8)*255
        red_rect[:, :, :] = [0, 20, 150]

        res = cv2.addWeighted(sub_img, 0.5, red_rect, 0.5, 1.0)

        img[y:y+h, x:x+w, :] = res

        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 20, 200), 1)

    cv2.imshow("Face", img)

    if cv2.waitKey(100) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
