
import cv2

video = cv2.VideoCapture('video.mp4')
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
mog = cv2.createBackgroundSubtractorMOG2(history=30, varThreshold=100, detectShadows=False)
knn = cv2.createBackgroundSubtractorKNN(history=50, detectShadows=False)


while True:

    ret, frame = video.read()
    
    if frame is None:
        break

    #Getting img size    
    #height, width, _ = frame.shape
    #print(height, width)

    cap_area = frame[230:720, 200:1280]


    mask = mog.apply(cap_area)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contourns, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for i in contourns:
        # calc area 
        area = cv2.contourArea(i)
        if area > 150:
            #cv2.drawContours(cap_area, [i], -1, (0,0,255), 2)
            x,y,w,h = cv2.boundingRect(i)
            cv2.rectangle(cap_area, (x,y), (x+w, y+h), (0,0,255) )


    cv2.imshow('Frame', frame)
    cv2.imshow('Foreground MASK Frame', mask)

    keyboard = cv2.waitKey(30)
    if keyboard == 27:
        break


video.release()
cv2.destroyAllWindows()
