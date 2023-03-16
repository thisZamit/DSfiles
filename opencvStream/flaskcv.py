from flask import Flask,render_template,url_for,redirect,Response
import cv2

app = Flask(__name__)
camera = cv2.VideoCapture(0)

def getVideo():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            detector = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_alt.xml')
            eye_cascade = cv2.CascadeClassifier('Haarcascades/haarcascade_eye.xml')
            smile_cascade = cv2.CascadeClassifier('Haarcascades/haarcascade_smile.xml')
            faces=detector.detectMultiScale(frame,1.1,7)
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #Draw the rectangle around each face
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0 ,0), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255, 0), 2)

                # smile = smile_cascade.detectMultiScale(roi_gray, 1.1, 3)
                # for (ex, ey, ew, eh) in smile:
                #     cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255, 0), 2)


            # The below code is a general code for video stream without any bounding box, showing just the webcam
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/webcam')
def webcam():
    return Response(getVideo(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__=='__main__':
    app.run(debug=True)
