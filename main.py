import streamlit as st

st.header("Text Analyzer")
inputfromuser = st.text_area("Enter the paragraph")
inputfromuser2 = st.text_input("Enter the word to search for:")
inputfromuser3 = st.text_input("Enter the word to replace with:")

if inputfromuser.strip() == "":
    st.error("Please enter a paragraph.")
elif inputfromuser2.strip() == "":
    st.error("Please enter a word to search for.")
elif inputfromuser3.strip() == "":
    st.error("Please enter a word to replace with.")
else:
    if inputfromuser2 not in inputfromuser:
        st.error("The word to search for does not exist in the paragraph.")
    else:
        vowels = "aeiouAEIOU"
        words = inputfromuser.split()
        wordcount = len(words)
        characters = len(inputfromuser)
        st.success(f"Word Count: {wordcount}")
        st.success(f"Character Count: {characters}")
        count = sum(1 for char in inputfromuser if char in vowels)
        st.success(f"Vowels: {count}")
        modified = inputfromuser.replace(inputfromuser2, inputfromuser3)
        st.success(f"Modified Sentence: {modified}")
        lowercase = inputfromuser.lower()
        uppercase = inputfromuser.upper()
        st.success(f"Lowercase: {lowercase}")
        st.success(f"UPPERCASE: {uppercase}")
        average = characters / wordcount if wordcount > 0 else 0
        st.success(f"Average Word Length: {average}")