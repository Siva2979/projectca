import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model('app/model/cnn_model.h5')

def predict_digit(image_array):
    image = image_array.reshape(1, 28, 28, 1).astype('float32') / 255.0
    prediction = model.predict(image)
    return np.argmax(prediction)
