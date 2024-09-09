import streamlit as st
import spacy
from spacy import displacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Streamlit app
st.title(":rainbow[POS Tagging Application]")
st.write("Enter text below to see the Part-of-Speech tags.")

# Text input
text = st.text_area("Enter your text here:")

if text:
    # Process the text with spaCy
    doc = nlp(text)

    # Extract POS tags
    pos_tags = [(token.text, token.pos_, token.tag_) for token in doc]

    # Display the POS tags
    st.write("### POS Tags")
    for word, pos, tag in pos_tags:
        st.write(f"**{word}**: {pos} ({tag})")

    # Highlight words based on POS tags
    st.write("### Highlighted Text")
    options = {"ents": ["VERB", "ADJ", "ADV"], "colors": {"VERB": "yellow", "ADJ": "lightblue", "ADV": "lightgreen"}}
    html = displacy.render(doc, style="ent", options=options)
    st.write(html, unsafe_allow_html=True)
