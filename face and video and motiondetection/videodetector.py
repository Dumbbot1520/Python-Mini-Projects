import cv2,time

video = cv2.VideoCapture(0)#0,1,2,3 integers ar given for multiple camera devices(if present). in this case only one camera is present
a=1 #to check number of frames in while loop
while True:
    a=a+1
    check,frame = video.read() #checks if camera is present and gives the array of video images it captured in the specified time
    print(check)
    print(frame)

    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # time.sleep(3)
    cv2.imshow("Video screen",grey)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break
print(a)
video.release()
cv2.destroyAllWindows()