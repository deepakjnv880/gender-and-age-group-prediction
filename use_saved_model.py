import cv2
import numpy as np
from PIL import Image
import dlib
import os
#
# IMG_SIZE=227
#
# def distance(a, b):
# 	return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
#
# def shape_to_normal(shape):
# 	shape_normal = []
# 	for i in range(0, 5):
# 		shape_normal.append((shape.part(i).x, shape.part(i).y))
# 	return shape_normal
#
# def angle_opposite_to_line3(length_line1, length_line2, length_line3):
# 	cos_value = (length_line1**2 + length_line2**2 - length_line3**2) / (2*length_line2*length_line1)
# 	return np.arccos(cos_value)
#
# def align_and_resize_image(img):
# 	##### align image ############################
# 	predictor = dlib.shape_predictor('shape_predictor_5_face_landmarks.dat')
#
# 	gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# 	x = 0
# 	y = 0
# 	w = gray.shape[0]
# 	h = gray.shape[1]
# 	rect=dlib.rectangle(x,y,w,h)
# 	shape = predictor(gray, rect)
#
# 	shape = shape_to_normal(shape)
# 	# shape has 5 point 4 nose 2 3 left eye 0 1 right eye
# 	# https://www.pyimagesearch.com/2018/04/02/faster-facial-landmark-detector-with-dlib/
# 	nose = shape[4]
# 	left_eye = [int(shape[2][0]+shape[3][0])/2,int(shape[2][1]+shape[3][1])/2]
# 	right_eye = [int(shape[0][0]+shape[1][0])/2,int(shape[0][1]+shape[1][1])/2]
#
# 	center_of_forehead = ((left_eye[0] + right_eye[0])/2, (left_eye[1] + right_eye[1])/2)
#
# 	center_image_top = (int((x + w) / 2), int((y + y) / 2))
#
# 	length_line1 = distance(center_of_forehead, nose)
# 	length_line2 = distance(center_image_top, nose)
# 	length_line3 = distance(center_image_top, center_of_forehead)
#
# 	angle = angle_opposite_to_line3(length_line1, length_line2, length_line3)
#
# 	if center_of_forehead[0]<=center_image_top[0]:
# 		angle = np.degrees(angle)
# 	else:
# 		angle = np.degrees(-angle)
#
# 	# print("angle is ",angle)
# 	img = Image.fromarray(img)
# 	img = np.array(img.rotate(angle))
# 	# ########################### Cropping of aligned image ###################################
# 	cv2.resize(img, (IMG_SIZE, IMG_SIZE))
# 	return img
#
# def deepak(ImagePath):
#
# 	img = cv2.imread(ImagePath)
# 	# gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# 	image_copy = np.copy(img)
# 	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# 	faces = face_cascade.detectMultiScale(img, 1.15, 4)
# 	print("===>",len(faces))
# 	face_crop = []
# 	for f in faces:
# 		x, y, w, h = [ v for v in f ]
# 		cv2.rectangle(image_copy, (x,y), (x+w, y+h), (82,247,115), 2)
# 		cv2.putText(image_copy, 'Fedex', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,255), 1)
# 		# Define the region of interest in the image
# 		# face_crop.append(gray[y:y+h, x:x+w])
# 		mod_img=align_and_resize_image(img[y:y+h, x:x+w])
# 	cv2.imshow('face',image_copy)
# 	cv2.waitKey(0)
#
#
# deepak("p2.jpg")

import tensorflow as tf
print("tensorflow version ==> ",tf.__version__)
model = tf.keras.models.load_model('/home/deepakjnv880/deep learning projects/genderage detection github/saved model/gender_prediction.h5')
model.summary()

import numpy as np
import cv2
IMG_SIZE=100
l=["male","female","child"]
X=[]
for i in os.listdir("photo"):
  img = cv2.imread("photo/"+i,cv2.IMREAD_GRAYSCALE)
  img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
  X.append(np.array(img))
X = np.expand_dims(X, axis=3)
result = new_model.predict_classes(X)
print(result)
