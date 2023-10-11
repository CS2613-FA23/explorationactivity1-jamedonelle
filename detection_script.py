import cv2 # import openCV

face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


hat = cv2.imread("cowboy_hat.png", cv2.IMREAD_UNCHANGED)

cam = cv2.VideoCapture(0) # initialization camera

while True:
    
    result, video_frame = cam.read()  # get frame from cam

    gray_image = cv2.cvtColor(video_frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    for (x, y, w, h) in faces:
        try:
            x1, y1 = x - 20, y - 150
            x2, y2 = x1 + w + 20, y + 10 
            if y1 < 0:
                y1 = 0
            if x2 > video_frame.shape[1]:
                x2 = video_frame.shape[1]

            hat_width = x2 - x1
            hat_height = y2 - y1

            resized_hat = cv2.resize(hat, (hat_width, hat_height))

            # need to create mask to add trasnparency
            mask = resized_hat[:, :, 3] / 255.0
            mask_inv = 1.0 - mask

            # put hat on top of face
            for c in range(0, 3):
                video_frame[y1:y2, x1:x2, c] = (
                    video_frame[y1:y2, x1:x2, c] * mask_inv
                    + resized_hat[:, :, c] * mask
                )
        except:
            print("Failed to load frame")

    cv2.imshow("My Face Detection Project", video_frame) # show cam frame  

    key = cv2.waitKey(1)
    if key == 27 : # escape
        break
    if key == 49: # w
        print("file written")
        cv2.imwrite("written_frame.png", video_frame)

cam.release()
cv2.destroyAllWindows()