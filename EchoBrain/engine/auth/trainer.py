import cv2
import numpy as np
from PIL import Image #pillow package
import os
import tensorflow as tf

path = 'engine\\auth\\samples' # Path for samples already taken

recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
detector = cv2.CascadeClassifier("engine\\auth\\haarcascade_frontalface_default.xml")
#Haar Cascade classifier is an effective object detection approach

def tensorflow_image_recognition():
    
    model = tf.keras.applications.MobileNetV2(weights="imagenet")

    
    def load_image(image_path):
        img = Image.open(image_path).resize((224, 224))  # Resize image for MobileNetV2
        img = np.array(img) / 255.0  # Normalize the image
        img = np.expand_dims(img, axis=0)  # Add batch dimension
    

def Images_And_Labels(path): # function to fetch the images and labels

    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []

    for imagePath in imagePaths: # to iterate particular image path

        gray_img = Image.open(imagePath).convert('L') # convert it to grayscale
        img_arr = np.array(gray_img,'uint8') #creating an array

        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_arr)

        for (x,y,w,h) in faces:
            faceSamples.append(img_arr[y:y+h,x:x+w])
            ids.append(id)

    return faceSamples,ids

print ("Training faces. It will take a few seconds. Wait ...")

faces,ids = Images_And_Labels(path)
recognizer.train(faces, np.array(ids))

recognizer.write('engine\\auth\\trainer\\trainer.yml')  # Save the trained model as trainer.yml

print("Model trained, Now we can recognize your face.")