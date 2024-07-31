from youtube_transcript_api import YouTubeTranscriptApi

# TODO: add whisper API instead of youtube caption

def get_transcript_from_id(video_id):
    """
    Get the transcript of a YouTube video from the video id.
    Args:
        video_id (str): The video id of the video
    Returns: 
        video_transcript (str): The transcript of the video
    """
    transcipts = YouTubeTranscriptApi.get_transcript(video_id)
    combined_texts = []

    for transcipt in transcipts:
        combined_texts.append(transcipt['text'])

    combined_texts = ' '.join(combined_texts)
    assert isinstance(combined_texts, str), "The transcript is not a string"

    print(combined_texts)
    return combined_texts

get_transcript_from_id('LdeVtvKFDNU')
