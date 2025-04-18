from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from PIL import Image
import io

app = Flask(__name__)
model = tf.keras.models.load_model('app/model/cnn_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file found'}), 400

    file = request.files['file']
    image = Image.open(file).convert('L').resize((28,28))
    image_array = np.array(image)
    image_array = image_array.reshape(1,28,28,1).astype('float32') / 255.0

    prediction = model.predict(image_array)
    predicted_digit = int(np.argmax(prediction))
    confidence = float(np.max(prediction))

    return jsonify({
        'predicted_digit': predicted_digit,
        'confidence': confidence
    })
