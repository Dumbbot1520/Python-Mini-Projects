import cv2

#the cascade filecontains all the information on how to recognize or detect a face in any image so this file is a seperate xml file 
face_cascade = cv2.CascadeClassifier("C:/Users/Om/OneDrive/Documents/GitHub/pythonudemy/IMAGE PROCESSING/FACEDETECTION/haarcascade_frontalface_default.xml")

image = cv2.imread("C:/Users/Om/OneDrive/Documents/GitHub/pythonudemy/IMAGE PROCESSING/FACEDETECTION/face.png")
grey_img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#identifying the  face
face = face_cascade.detectMultiScale(grey_img,
scaleFactor= 1.05,
minNeighbors= 5)

#creating the rectangle to show the face dimensions
for x,y,w,h in face:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),thickness=5)


resized= cv2.resize(image,(int(image.shape[1]/3),int(image.shape[0]/3)))
cv2.imshow(" image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()