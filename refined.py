import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "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"

# Function to refine the user's query using OpenAI GPT-3
def query_refiner(query):
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"Given the following user query, formulate a question that would be the most relevant to provide the user with an answer from a knowledge base and also make the correct spelling of the words given in the query and it should be gramatically correct\n\nQuery: {query}\n\nRefined Query:",
        temperature=0.7,
        max_tokens=50,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    refined_query = response.choices[0].text.strip()
    return refined_query

# Main Streamlit app
def main():
    st.title("Query Refiner")

    # Text box for user input
    user_query = st.text_input("Enter your query:")

    # Button to refine the query
    if st.button("Refine Query"):
        if user_query:
            # Refine the user's query using OpenAI GPT-3
            refined_query = query_refiner(user_query)
            # Display the refined query
            st.success("Refined Query: {}".format(refined_query))
        else:
            st.warning("Please enter a query.")

if __name__ == "__main__":
    main()
