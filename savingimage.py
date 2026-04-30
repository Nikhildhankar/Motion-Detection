import cv2
import time

video_capture = cv2.VideoCapture(0)
time.sleep(1)
first_frame = None
count =1
while True:
    check, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gaussian = cv2.GaussianBlur(gray, (11, 11), 0)

    if first_frame is None:
        first_frame = gray_frame_gaussian

    delta_frame = cv2.absdiff(first_frame, gray_frame_gaussian)
    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
    thresh_frame = cv2.erode(thresh_frame, None, iterations=2)

    countours,check =cv2.findContours(dil_frame,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in countours:
        if cv2.contourArea(contour) < 1000:
            continue
        x,y,w,h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        if rectangle.any():
            status = 1
            cv2.imwrite(f"images/{count}.png", frame)
            count += 1

    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()



