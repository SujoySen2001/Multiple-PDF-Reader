import streamlit as st
from textblob import TextBlob
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import random

# Function to generate similar questions
def generate_similar_questions(query):
    # Tokenize the query
    query_tokens = word_tokenize(query.lower())
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    query_tokens = [word for word in query_tokens if word not in stop_words]
    
    # Get synonyms for each word in the query
    similar_questions = []
    for token in query_tokens:
        synonyms = set()
        for syn in TextBlob(token).synsets:
            for lemma in syn.lemmas():
                synonyms.add(lemma.name())
        if synonyms:
            similar_questions.append(synonyms)
    
    # Generate new questions by replacing words with synonyms
    generated_questions = []
    for synonyms in similar_questions:
        for synonym in synonyms:
            new_question = ' '.join([synonym if word == synonym else word for word in query_tokens])
            generated_questions.append(new_question)
    
    # Shuffle and return a subset of generated questions
    random.shuffle(generated_questions)
    return generated_questions[:5]  # Return 5 similar questions

# Streamlit UI
st.title("Similar Question Generator")

query = st.text_input("Enter your query:")
if st.button("Generate Similar Questions"):
    if query:
        similar_questions = generate_similar_questions(query)
        st.subheader("Similar Questions:")
        for q in similar_questions:
            st.write(q)
    else:
        st.write("Please enter a query.")