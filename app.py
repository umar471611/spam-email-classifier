
import streamlit as st
import pickle
import string
from nltk.corpus import stopwords

model = pickle.load(open("spam_model.pkl","rb"))
vectorizer = pickle.load(open("vectorizer.pkl","rb"))

def clean_text(text):
    text = text.lower()
    text = ''.join(char for char in text if char not in string.punctuation)

    words = text.split()

    words = [word for word in words
             if word not in stopwords.words('english')]

    return " ".join(words)

st.title("Spam Email Classifier")

message = st.text_area("Enter Email")

if st.button("Check"):

    cleaned = clean_text(message)

    vector = vectorizer.transform([cleaned])

    prediction = model.predict(vector)[0]

    if prediction == "spam":
        st.error("SPAM EMAIL")
    else:
        st.success("NOT SPAM")
