import cv2


def takeSnapshot():
    videoCapture = cv2.VideoCapture(0)
    result = True
    while(result == True):
        ret, frame = videoCapture.read()
        cv2.imwrite("new picture 1.jpg", frame)
        result = False
    videoCapture.release()
    cv2.destroyAllWindows()


takeSnapshot()
