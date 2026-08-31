import joblib
import streamlit as st 
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import PorterStemmer
# Download NLTK resources
nltk.download("stopwords")
nltk.download("punkt")
nltk.download("punkt_tab")
import re
import string

#import the model and count vectorizer
model = joblib.load("spam_mnb_model.pkl")
vector = joblib.load("count_vectorizer.pkl")
st.header('EMAIL/SMS SPAM CLASSIFIER')
#using the nltk library 
porter=PorterStemmer()
stop_word=set(stopwords.words('english'))
user_input=st.text_area('enter you email')
def tranform_text(text):
  text=re.sub(r'[%#@]','',text)
  text = re.sub(r'_+', ' ', text)
  text=text.lower()
  text=word_tokenize(text)
  new_text=[]
  for i in text:
    if i not in stop_word and i not in string.punctuation:
      i=porter.stem(i)
      new_text.append(i)


  return  ' '.join(new_text)

if st.button('predict'):
 tranform_input=tranform_text(user_input)
 input_vector=vector.transform([tranform_input])  # Convert text into numerical features
 prediction=model.predict(input_vector)

 if prediction[0]==1:
   st.write('🚨ITS A SPAM')
 else:
   st.write('✅ NOT SPAM') 
