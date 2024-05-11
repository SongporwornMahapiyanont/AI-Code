import openai

openai.api_key = "xxx"

audio_file = open("t1_video.mp4", "rb")

transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript.text)
