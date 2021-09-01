from captureImage import takeSnapshot
import time
import random
import cv2
import dropbox

startTime = time.time()


def takeSnapShot():
    number = random.randint(0, 100)
    takePhoto = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = takePhoto.read()
        imageName = "img"+str(number)+".png"
        cv2.imwrite(imageName, frame)
        startTime = time.time
        result = False
    return imageName
    print("snapshotTaken")
    takePhoto.release()
    cv2.destroyAllWindows()


def uploadFile(imageName):
    accestoken = "Rczxwob4U_IAAAAAAAAAARJURiUdqZSRtyaLaXIWmMlxL0-b0To-EqWNm129VmXO"
    file = imageName
    fileFrom = file
    fileTo = "/testFolder/"+(imageName)
    dbx = dropbox.Dropbox(accestoken)
    with open(fileFrom, "rb") as f:
        dbx.files_upload(f.read(), fileTo,
                         mode=dropbox.files.WriteMode.oveerwrite)
        print("file uploaded")


def main():
    while(True):
        if((time.time()-startTime) >= 10):
            name = takeSnapshot()
            uploadFile(name)


main()
