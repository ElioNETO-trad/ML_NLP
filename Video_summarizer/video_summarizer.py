#Test to summarize some videos using LLM

#1st = Import youtube__transcript_api.
#2nd = Install the deepmultilingualpunctuation Library to restore the punctuation in the transcript.
#3rd = import module to run the task in the local LLM model.


from youtube_transcript_api import YouTubeTranscriptApi
from deepmultilingualpunctuation import PunctuationModel
from ollama_client_llama7b import get_ollama_response


def get_video_id(url_link):
    return url_link.split("watch?v=")[-1]

video_url = input("Enter the url of your video: ")

video_id = get_video_id(video_url)

transcript = YouTubeTranscriptApi.get_transcript(video_id)

transcript_joined = "".join(line['text'] for line in transcript)

model = PunctuationModel()

result = model.restore_punctuation(transcript_joined)

print(f"This is the transcription of your video {result}")

prompt = f'"Summarize this text: \ntext:= "{result}'

response = get_ollama_response(prompt)

print(response)
