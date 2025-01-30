from pyannote.audio.pipelines.speaker_diarization import SpeakerDiarization
from pyannote.core import Segment
import whisper
import torch
import os
from dotenv import load_dotenv

load_dotenv()

# Load models
diarization_model = SpeakerDiarization.from_pretrained("pyannote/speaker-diarization", use_auth_token=os.getenv("HF_KEY"))
whisper_model = whisper.load_model("base")

def transcribe_and_diarize(audio_path):
    # Step 1: Diarization
    diarization_result = diarization_model({"uri": "audio", "audio": audio_path})

    # Step 2: Transcription
    whisper_result = whisper_model.transcribe(audio_path)
    
    # Step 3: Match text with speakers
    segments = []
    for segment in diarization_result.itertracks(yield_label=True):
        start, end = segment[0].start, segment[0].end
        speaker = segment[2]
        text = extract_text(whisper_result, start, end)
        segments.append({"speaker": speaker, "text": text, "start": start, "end": end})

    return segments

def extract_text(whisper_result, start, end):
    """ Match Whisper transcriptions to diarization segments """
    return " ".join([seg["text"] for seg in whisper_result["segments"] if seg["start"] >= start and seg["end"] <= end])
