# Email/SMS Spam Classifier

A machine learning-based application that classifies emails and SMS messages as **Spam** or **Not Spam** using Natural Language Processing (NLP) and Multinomial Naive Bayes.

## Features

* Classifies email/SMS messages as Spam or Not Spam
* Text preprocessing using NLTK
* Feature extraction using CountVectorizer
* Multinomial Naive Bayes for classification
* Hyperparameter tuning using Optuna
* Saved model and vectorizer for prediction
* Interactive Streamlit web application

## Technologies Used

* Python
* NLTK
* Scikit-learn
* Pandas
* Joblib
* Optuna
* Streamlit

## Machine Learning Workflow

**Input Text → Text Preprocessing → CountVectorizer → Multinomial Naive Bayes → Prediction**

### Text Preprocessing

The input text is processed using:

* Lowercasing
* Tokenization
* Stop-word removal
* Punctuation removal
* Stemming using Porter Stemmer

### Model Selection & Hyperparameter Tuning

Different machine learning models were evaluated during the development of the project. **Optuna** was used for automated hyperparameter tuning and model optimization.

The final model used in the application is **Multinomial Naive Bayes (MNB)**, selected based on its classification performance.

The trained model and CountVectorizer are saved using **Joblib** and loaded during application execution.

## Streamlit Application

The project includes a Streamlit interface where users can enter an email or SMS message and receive an immediate prediction.

### Prediction

* 🚨 **SPAM** — The message is classified as spam.
* ✅ **NOT SPAM** — The message is classified as legitimate.

This project demonstrates the application of **Machine Learning, Natural Language Processing, hyperparameter optimization, and Streamlit** to build an end-to-end spam classification system.
