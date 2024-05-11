import cv2

cap = cv2.VideoCapture(0)
cap.isOpened

while(True):
    ret, frame = cap.read() 
    cv2.imshow('Frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if cv2.waitKey(33) == ord('a'):
        cv2.imwrite('image.png', frame)

cap.release()
cv2.destroyAllWindows()