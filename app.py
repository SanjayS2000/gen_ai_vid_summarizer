import streamlit as st

from transcript import get_transcript
from summarizer import summarize

st.set_page_config(page_title="AI YouTube Summarizer")

st.title("🎥 AI YouTube Summarizer")

url = st.text_input("Enter YouTube URL")

if st.button("Generate Summary"):

    if not url.strip():
        st.error("Please enter a YouTube URL.")
        st.stop()

    try:

        with st.spinner("Fetching transcript..."):

            data = get_transcript(url)

        st.success("Transcript fetched successfully!")

        st.subheader("Debug")

        st.code(data["text"][:500])

        with st.spinner("Generating summary..."):

            summary = summarize(data["text"])

        st.subheader("Summary")

        st.write(summary)

    except Exception as e:

        st.error(str(e))