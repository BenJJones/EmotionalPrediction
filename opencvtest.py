import numpy as np
import cv2
import MSEmotionAPI
import testscore

cap = cv2.VideoCapture(0)
i = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(500) & 0xFF == ord('q'):
        break
    imageFile = "test" + str(i) + ".png"
    cv2.imwrite(imageFile,frame)
    i += 1
    testscore.score(MSEmotionAPI.processImage(imageFile))

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
