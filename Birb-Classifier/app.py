import gradio as gr
import tensorflow as tf
import cv2
import numpy as np

model = tf.keras.models.load_model('birb-classifier.h5')
classes = np.load('classes.npy')

def pred_fn(image):
    img = cv2.resize(image, (224, 224))
    result = model.predict(np.expand_dims(img, axis=0))
    return classes[result.argmax()]

# Create a Gradio interface
inputs = gr.inputs.Image(shape=(224, 224))
outputs = gr.outputs.Textbox()
interface = gr.Interface(fn=pred_fn, inputs=inputs, outputs=outputs, title='Bird Classifier')

# Launch the interface
interface.launch()
