import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

model_Apple = load_model('model_corn.h5')

def Disease_Predict_Apple(file_data):
    test_image = load_img(file_data, target_size = (256, 256)) # load image 
    print("@@ Got Image for prediction")
    test_image = img_to_array(test_image)/255

    res = model_Apple.predict(test_image)
    res1 = np.argmax(res)

    return res1


