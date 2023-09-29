# TechdomeSentiment
 Sentiment Analysis using DistilBERT
This repository contains the code and resources used for sentiment analysis using the DistilBERT model.

Table of Contents
Introduction
Installation
Dataset
Training
Evaluation
Deployment
Acknowledgements
Introduction
This project aims to classify text data into positive, negative, or neutral sentiments using the power of transformer models, specifically DistilBERT.

Installation
Clone this repository.
Install the required packages:
bash
Copy code
pip install -r requirements.txt
Dataset
The dataset consists of various text sources such as product reviews, social media comments, and news articles, labeled as positive or negative.

Training
Due to time and hardware limitations, the model has been trained with certain constraints. As such, for optimal performance, further training is recommended on more robust systems.

Evaluation
The model's performance is evaluated based on various metrics such as accuracy, precision, recall, and F1-score. The evaluation script can be found in the repository.

Deployment
The model is deployed using Flask as a simple web application. To use:

Run python app.py.
Navigate to http://127.0.0.1:5000/ in your browser.
Acknowledgements
Hugging Face's Transformers library for the model and tokenizers.
The open-source community for the invaluable tools and libraries.
Note
Checkpoints and the trained model are not uploaded to this repository as they exceed the file size limit of 250 MBs.

