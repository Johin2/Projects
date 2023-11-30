import streamlit as st

import tensorflow as tf

from tensorflow.keras.preprocessing import image

import numpy as np

from tensorflow.keras.models import load_model

model = load_model('Brain_tumor.h5')

def main():

    st.title('Brain Tumor Detection App')

    st.write('Upload an MRI scan image to detect if it contains a brain tumor.')


    uploaded_file = st.file_uploader("Choose an MRI scan image...", type=["jpg", "jpeg", "png"])


    if uploaded_file is not None:

        img = image.load_img(uploaded_file, target_size=(200, 200), color_mode = 'grayscale')

        img_array = image.img_to_array(img)

        img_array = np.expand_dims(img_array, axis=0)

        img_array /= 255.0  # Normalization


        prediction = model.predict(img_array)

        if prediction[0][0] > 0.5:

            st.write("Prediction: This MRI scan contains a brain tumor.")

        else:

            st.write("Prediction: This MRI scan is tumor-free.")


        st.image(img, caption='Uploaded MRI scan', use_column_width=True)



if __name__ == "__main__":

    main()

