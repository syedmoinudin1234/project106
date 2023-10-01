# import the opencv library
import cv2

# Define a video capture object
vid = cv2.VideoCapture(0)

while(True):
   
    # Capture the video frame by frame
    ret, frame = vid.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    face=face_cascade.detectMultiScale(gray)
    for (x,y,w,h)in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(40,30,20),4)
    # Display the resulting frame
    cv2.imshow("Web cam", frame)
      
    # Quit Window by Spacebar Key
    if cv2.waitKey(25) == 32:
        break
  
# After the loop release the cap object
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()