import io
import joblib
import streamlit as st

from PIL import Image
from transformers import ViTImageProcessor, ViTModel
from sklearn.preprocessing import StandardScaler


@st.cache_resource
def load_model():
    processor = ViTImageProcessor.from_pretrained('google/vit-large-patch16-224-in21k')
    model = ViTModel.from_pretrained('google/vit-large-patch16-224-in21k')
    return processor, model

def get_vector_image(image_bytes):
    processor, model = load_model()

    image = Image.open(io.BytesIO(image_bytes))
    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    last_hidden_state = outputs.last_hidden_state
    vector = list(outputs.last_hidden_state[:, 0][0].detach().numpy().tolist())
    return vector


def get_vector_gizi(calories, proteins, fat, carbohydrate):
    scaler = joblib.load('models/gizi_scaler.pkl')
    vector = scaler.transform([[calories, proteins, fat, carbohydrate], ])
    return vector[0]

