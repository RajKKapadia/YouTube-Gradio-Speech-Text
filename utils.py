import os
import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_transcription(file_path_upload: str, file_path_microphone: str) -> str:
    print(file_path_upload, file_path_microphone)
    audio_file = open(file_path_microphone, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript['text']
