import streamlit as st
import pickle
import string

# Load model
model = pickle.load(open("spam_model.pkl","rb"))
vectorizer = pickle.load(open("vectorizer.pkl","rb"))

# Simple stopwords list (NO NLTK needed)
stop_words = set([
    "the","is","in","and","to","a","of","for","on","with","this","that",
    "you","it","are","was","i","have","has","at","be","as","by","an"
])

def clean_text(text):
    text = text.lower()
    text = ''.join(char for char in text if char not in string.punctuation)

    words = text.split()
    words = [word for word in words if word not in stop_words]

    return " ".join(words)

# UI
st.title("📧 Spam Email Classifier")

message = st.text_area("Enter Email or Message")

if st.button("Check Spam"):
    cleaned = clean_text(message)

    vector = vectorizer.transform([cleaned])

    prediction = model.predict(vector)[0]

    if prediction == "spam":
        st.error("🚨 SPAM EMAIL")
    else:
        st.success("✅ NOT SPAM")
