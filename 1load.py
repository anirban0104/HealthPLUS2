import cv2
import time

cap= cv2.VideoCapture('videos/load.mp4')


fps= int(cap.get(cv2.CAP_PROP_FPS))

if cap.isOpened() == False:
    print("Error File Not Found")

while cap.isOpened():
    ret,frame= cap.read()

    if ret == True:

        time.sleep(1/fps)

        cv2.imshow('Loading, Please wait...', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break


cap.release()
cv2.destroyAllWindows()

# FINEEE