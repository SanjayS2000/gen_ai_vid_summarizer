from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(url: str) -> str:
    """Extract YouTube video ID from different URL formats."""

    if "youtu.be" in url:
        return url.split("/")[-1].split("?")[0]

    parsed = urlparse(url)

    if "youtube.com" in parsed.netloc:
        return parse_qs(parsed.query).get("v", [""])[0]

    return url


def get_transcript(url: str):
    video_id = extract_video_id(url)

    print(f"Video ID: {video_id}")

    api = YouTubeTranscriptApi()

    transcript = api.fetch(video_id)

    text = " ".join(
        snippet.text if hasattr(snippet, "text") else snippet["text"]
        for snippet in transcript
    )

    return {
        "video_id": video_id,
        "text": text,
        "segments": transcript,
    }