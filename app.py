import streamlit as st

from transcript import get_transcript
from summarizer import summarize

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI YouTube Video Summarizer",
    page_icon="🎥",
    layout="centered",
)

# -----------------------------
# UI
# -----------------------------
st.title("🎥 AI YouTube Video Summarizer")
st.caption("Paste a YouTube URL to generate an AI-powered summary.")

url = st.text_input(
    "YouTube URL",
    placeholder="https://www.youtube.com/watch?v=...",
)

# -----------------------------
# Generate Summary
# -----------------------------
if st.button("🚀 Generate Summary"):

    if not url.strip():
        st.warning("Please enter a YouTube URL.")
        st.stop()

    if "youtube.com" not in url and "youtu.be" not in url:
        st.error("Please enter a valid YouTube URL.")
        st.stop()

    try:
        # Fetch transcript
        with st.spinner("📥 Fetching transcript..."):
            data = get_transcript(url)

        st.success("✅ Transcript fetched successfully!")

        # Optional debug preview
        with st.expander("🔍 Transcript Preview (first 500 characters)"):
            st.code(data["text"][:500])

        # Generate summary
        with st.spinner("🤖 Generating AI summary..."):
            summary = summarize(data["text"])

        st.markdown("---")
        st.subheader("📝 AI Summary")
        st.markdown(summary)

    except Exception as e:
        st.error(
            "❌ Failed to process this video.\n\n"
            "Possible reasons:\n"
            "- The video has no available transcript.\n"
            "- Captions are disabled.\n"
            "- The transcript is not publicly accessible.\n"
            "- The AI service is temporarily unavailable.\n\n"
            f"Technical details:\n{str(e)}"
        )

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption(
    "⚠️ Version 1 uses YouTube transcripts. Videos without accessible captions may not be supported."
)