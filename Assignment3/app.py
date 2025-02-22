import streamlit as st
from workflows.crew_workflow import run_workflow

st.title("📰 AI-Powered News Extractor with CrewAI")

query = st.text_input("Enter news topic (e.g., 'GPT-5')", "AI technology")

if st.button("Fetch News"):
    result = run_workflow(query, num_articles=5)

    st.subheader("🔹 Extracted News Headlines")
    for title, url in result["headlines"]:
        st.markdown(f"- [{title}]({url})")  # Clickable links

    st.subheader("📄 AI-Generated Summary")
    st.write(result["summary"])

    st.subheader("📊 Sentiment Analysis")
    st.write(f"**Overall Sentiment:** {result['sentiment']}")
