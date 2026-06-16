from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(url: str) -> str:
    if "youtu.be" in url:
        return url.split("/")[-1].split("?")[0]

    parsed = urlparse(url)
    return parse_qs(parsed.query).get("v", [""])[0]

def get_transcript(url: str):
    video_id = extract_video_id(url)

    api = YouTubeTranscriptApi()
    transcript = api.fetch(video_id)  # Automatically picks available transcript

    text = " ".join(snippet.text for snippet in transcript)

    return {
        "video_id": video_id,
        "text": text,
        "segments": transcript,
    }