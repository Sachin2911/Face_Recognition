import face_recognition

image = face_recognition.load_image_file("./img/groups/team2.jpg")
face_locations = face_recognition.face_locations(image)

#Array of coordinaes of each face
print(face_locations)
print("There are {} people in this image".format(len(face_locations)))