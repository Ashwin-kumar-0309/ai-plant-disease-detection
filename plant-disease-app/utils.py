import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from class_names import class_names

# Load the trained model
model = tf.keras.models.load_model('models/fine_tuned_model.h5')

def predict_disease(img_path):
    try:
        # Preprocess image
        img = image.load_img(img_path, target_size=(128, 128))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        
        # Predict
        pred = model.predict(img_array)
        class_idx = np.argmax(pred)
        return class_names[class_idx], np.max(pred)
        
    except Exception as e:
        raise RuntimeError(f"Prediction error: {str(e)}")