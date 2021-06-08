import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('./src/h_eyeglasses.xml')
cap = cv2.VideoCapture(0)

# img = cv2.imread('')

while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    detections = face_cascade.detectMultiScale(gray, 1.1, 4)

    if (len(detections) == 2):

        # for (x, y, w, h) in detections:
        detections = np.array(detections)
        x1, x2 = detections[:, 0]
        y1, y2 = detections[:, 1]
        x = min([x1, x2])
        y = max([y1, y2])

        w = max([x1, x2]) + np.max(detections[:, 2]) - x
        h = max([y1, y2]) + np.max(detections[:, 3]) - y

        padding = 30
        cv2.rectangle(img, (x - padding, y),
                      (x + w + padding, y + h), (0, 20, 150), cv2.FILLED)

    cv2.imshow("Eyes", img)

    if cv2.waitKey(100) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
