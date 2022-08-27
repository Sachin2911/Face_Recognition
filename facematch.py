from traceback import print_tb
from unittest import result
import face_recognition

image = face_recognition.load_image_file("./img/known/Bill Gates.jpg")
bill_face_encoding = face_recognition.face_encodings(image)[0]

unkown_image = face_recognition.load_image_file("./img/unknown/bill-gates-4.jpg")
unknown_face_encoding = face_recognition.face_encodings(unkown_image)[0]

#Compare faces
results = face_recognition.compare_faces([bill_face_encoding], unknown_face_encoding)

if results[0]:
    print("This is Bill gates")
    
else:
    print("This is no bill gates")