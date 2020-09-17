import cv2

print(cv2.__version__)

img = cv2.imread('lena.jpg', 0)
cap = cv2.VideoCapture(0);
#cap = cv2.VideoCapture('megamind.avi');

while(cap.isOpened()):
    ret, frame = cap.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Frame', grey)

    if cv2.waitKey(1) == ord('q'):
        break;

cap.release()
cv2.destroyAllWindows()