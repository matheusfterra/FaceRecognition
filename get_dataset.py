import cv2
import os
from READ_JSON import get_users,save_users

ids,users=get_users()

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

face_detector = cv2.CascadeClassifier('Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id
face_user = input('\n Digite um nome para Usuário: ')
if face_user in users:
    index = users.index(face_user)
    face_id=ids[index]
    print("O Usuário {} já foi cadastrado com ID {}".format(face_user,face_id))
    change_input=input("Deseja Alterá-lo? (y/n)")
    if change_input=="y":
        make_dataset=True
    else:
        make_dataset=False
else:
    face_id=max(ids)+1
    save_users(face_id,face_user)
    make_dataset=True

if make_dataset==True:

    print("\n [INFO] Initializing face capture. Look the camera and wait ...")
    # Initialize individual sampling face count
    count = 0

    while(True):
        ret, img = cam.read()
        #img = cv2.flip(img, -1) # flip video image vertically
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
            count += 1

            # Save the captured image into the datasets folder
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

            cv2.imshow('image', img)

        k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 30: # Take 30 face sample and stop video
             break

    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()
    import trainer
else:
    print("Captura Cancelada")