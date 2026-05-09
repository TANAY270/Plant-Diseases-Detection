import os 
import json
from zipfile import ZipFile
from PIL import Image 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg 
import tensorflow as tf
import streamlit as st
from tensorflow.keras.preprocessing.image import ImageDataGeneratorcl
from keras import layers, models
import streamlit as st
working_dir = os.path.dirname(os.path.abspath(__file__))
model_path =  f"{working_dir}/trained_model/plant_disease_prediction_model.h5"
#load the pretrained model

model= tf.keras.models.load_model(model_path)