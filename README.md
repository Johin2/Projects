# Projects
Welcome to my projects
These are the projects that I have made till date I will explain all of the projects here

**1)** **Brain Tumor Detection**:-  I used Deep Learning to train a model to detect if the MRI scans contained Brain Tumor.

Model Development: I employed Deep Learning techniques, including Convolutional Neural Networks (CNNs) and image segmentation, to create a robust model that demonstrates a high degree of accuracy in detecting brain tumors in MRI scans.

Data Preprocessing: I conducted thorough data preprocessing, including image augmentation and normalization, to enhance the model's ability to generalize across different MRI scans and imaging conditions.

Model Optimization: I fine-tuned the model's hyperparameters and architecture to ensure optimal performance, achieving a balance between accuracy and computational efficiency.

Validation and Testing: Rigorous validation and testing procedures were employed to assess the model's reliability and generalization capabilities. The model demonstrated consistent and reliable results across diverse MRI datasets.I have Completed my second project at Code Clause as a Data Science Intern. The task was to detect Brain tumor, I used Deep Learning to train a model to detect if the MRI scans contained Brain Tumor. Model Development: I employed Deep Learning techniques, including Convolutional Neural Networks (CNNs) and image segmentation, to create a robust model that demonstrates a high degree of accuracy in detecting brain tumors in MRI scans. Data Preprocessing: I conducted thorough data preprocessing, including image augmentation and normalization, to enhance the model's ability to generalize across different MRI scans and imaging conditions. Model Optimization: I fine-tuned the model's hyperparameters and architecture to ensure optimal performance, achieving a balance between accuracy and computational efficiency. Validation and Testing: Rigorous validation and testing procedures were employed to assess the model's reliability and generalization capabilities. The model demonstrated consistent and reliable results across diverse MRI datasets.
**Skills: Deep Learning · Machine Learning**

**2)** **Skin cancer Detection** :- This project involves building a skin cancer classification model using convolutional neural networks (CNNs) in Keras. The dataset used for training and testing the model is the Melanoma Skin Cancer Dataset, which consists of images of skin lesions labeled as either melanoma or non-melanoma.

The CNN model is trained on the dataset using image augmentation techniques, such as horizontal flipping, rotation, and zooming, to improve its performance. Once the model is trained, it is used to predict whether an input image contains melanoma or not.

To create a user interface for the skin cancer classification model, a GUI application is built using the Tkinter library in Python. The GUI allows users to select an image file from their local computer, and then displays the predicted result of the model. If the model predicts that the image contains melanoma, the GUI displays a message informing the user that the image is classified as melanoma, otherwise it displays a message that the image is classified as non-melanoma.This project involves building a skin cancer classification model using convolutional neural networks (CNNs) in Keras. The dataset used for training and testing the model is the Melanoma Skin Cancer Dataset, which consists of images of skin lesions labeled as either melanoma or non-melanoma. The CNN model is trained on the dataset using image augmentation techniques, such as horizontal flipping, rotation, and zooming, to improve its performance. Once the model is trained, it is used to predict whether an input image contains melanoma or not. To create a user interface for the skin cancer classification model, a GUI application is built using the Tkinter library in Python. The GUI allows users to select an image file from their local computer, and then displays the predicted result of the model. If the model predicts that the image contains melanoma, the GUI displays a message informing the user that the image is classified as melanoma, otherwise it displays a message that the image is classified as non-melanoma.
**Skills: Deep Learning · GitHub**

**3)** **Color Detection** :- This project lets you detect colors from an Image, I used K-mean Clustering a Unsupervised Machine Learning Technique to cluster the most dominant colors in an Image. Then I used Matplotlib to print out the most dominant colors as output. Overall this was a fun project and I got to learn alott from this projectI am Happy to announce that I have completed my first project as Data Science Intern at Code Clause,This project lets you detect colors from an Image, I used K-mean Clustering a Unsupervised Machine Learning Technique to cluster the most dominant colors in an Image. Then I used Matplotlib to print out the most dominant colors as output. Overall this was a fun project and I got to learn alott from this project
**Skills: Machine Learning**

**4)** **Document Data Extraction**:- The Program defines several functions to upload images, perform OCR (Optical Character Recognition) on them, and insert them into a MySQL database.
The upload_file() function reads an image file using OpenCV, resizes it, displays it, performs OCR on it using the Tesseract library, and prints the recognized text to the console.
The insert_to_database() function inserts an image file and its metadata into a MySQL database.
The upload_documents() function prompts the user to enter the document type and file paths for each image, calls the upload_file() function to process the images and collect their text, and stores the results in a dictionary.
The main() function connects to a MySQL server, calls upload_documents() to process the images and store them in the database, and prints a success or cancellation message to the console.
Overall, this code enables the user to upload images, extract text from them, and store the text and metadata in a MySQL database.The Program defines several functions to upload images, perform OCR (Optical Character Recognition) on them, and insert them into a MySQL database. The upload_file() function reads an image file using OpenCV, resizes it, displays it, performs OCR on it using the Tesseract library, and prints the recognized text to the console. The insert_to_database() function inserts an image file and its metadata into a MySQL database. The upload_documents() function prompts the user to enter the document type and file paths for each image, calls the upload_file() function to process the images and collect their text, and stores the results in a dictionary. The main() function connects to a MySQL server, calls upload_documents() to process the images and store them in the database, and prints a success or cancellation message to the console. Overall, this code enables the user to upload images, extract text from them, and store the text and metadata in a MySQL database.
**Skills: Python (Programming Language) · GitHub · MySQL**

**5)** **Sentiment Analysis**:-
__Data Acquisition and Preparation__:

You obtained Twitter datasets for training and validation purposes, which contained columns such as 'id', 'company', 'sentiment', and 'review'.
Data preprocessing involved:
Cleaning text data by removing punctuation and converting text to lowercase.
Tokenizing the text to separate words.
Removing English stop words to enhance the quality of text for analysis.
Filtering out irrelevant sentiments from the dataset for model training and testing.
__Text Vectorization__:

Utilized TF-IDF (Term Frequency-Inverse Document Frequency) vectorization to convert textual data into numerical form, which the machine learning model can interpret.
__Model Building and Evaluation__:

Employed a Support Vector Machine (SVM) with a linear kernel for classification.
Split the data into training and testing sets.
Trained the model using the training data transformed through TF-IDF vectorization.
Evaluated model performance using accuracy metrics and generated a classification report encompassing precision, recall, and F1-score for each sentiment class (Negative, Neutral, Positive).
Achieved an accuracy of approximately 96.01% on the validation dataset, demonstrating the model's effectiveness in sentiment classification.
__Prediction on New Data__:

Applied the trained model to predict sentiments on new, unseen data (a list of phrases), providing a breakdown of sentiments for each phrase.
**Skills :- Machine Learning**
