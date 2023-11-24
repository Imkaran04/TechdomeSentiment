# TechDome Sentiment Analysis 

### Sentiment Analysis using DistilBERT
 
This repository contains the code and resources used for sentiment analysis using the DistilBERT model.

Table of Contents

1.Introduction

2.Installation

3.Dataset

4.Training

5.Evaluation

6.Deployment

7.Acknowledgements


# 1. Introduction

This project aims to classify text data into positive, negative, or neutral sentiments using the power of transformer models, specifically DistilBERT.


# 2. Installation

Clone this repository.

Install the required packages:

bash

Copy code

pip install -r requirements.txt

# 3. Dataset

The dataset consists of various text sources such as product reviews, social media comments, and news articles, labeled as positive, neutral or negative.

# 4. Training

Due to time and hardware limitations, the model has been trained with certain constraints. As such, for optimal performance, further training is recommended on more robust systems.

# 5. Evaluation and Analysis 

The model's performance is evaluated based on various metrics such as accuracy, precision, recall, and F1-score. The evaluation script can be found in the repository.

Evaluation Results and Analysis:

##### Loss:

Achieved a final loss of approximately 0.5177.

##### Accuracy:

The model achieved an accuracy of around 78.02%.

##### Precision:

The precision achieved was approximately 77.88%.

##### Recall:

The recall achieved was approximately 78.02%.

##### F1-Score:

The model achieved an F1-score of around 77.95%.

## Analysis:

The model shows a good balance between precision and recall, indicating a balanced performance for both positive and negative classes. However, for more concrete results, further fine-tuning and hyperparameter optimization can be explored.

# 6.Deployment
The model is deployed using Flask as a simple web application. To use:

Run python app.py.

Navigate to http://127.0.0.1:5000/ in your browser.

# 7.Acknowledgements

Hugging Face's Transformers library for the model and tokenizers.

The open-source community for the invaluable tools and libraries.

# Note

Checkpoints and the trained model are not uploaded to this repository as they exceed the file size limit of 250 MBs.

