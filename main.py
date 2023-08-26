import numpy as np
import cv2

captureDevice = cv2.VideoCapture(0)

while True:
    ret, frame = captureDevice.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the captured frame
    cv2.imshow('Video', frame)
    cv2.imshow('Video2', gray)


    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture device and close any open windows
captureDevice.release()
cv2.destroyAllWindows()
