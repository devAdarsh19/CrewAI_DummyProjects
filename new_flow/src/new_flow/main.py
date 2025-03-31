#!/usr/bin/env python
from pydantic import BaseModel
from crewai.flow import Flow, listen, start
from pathlib import Path
from pydub import AudioSegment
from pydub.utils import make_chunks
from dotenv import load_dotenv
from openai import OpenAI
client = OpenAI()

load_dotenv()

class MeetingMinutesState(BaseModel):
    transcript: str = ""
    meeitng_minutes: str = ""


class MeetingMeetingFlow(Flow[MeetingMinutesState]):

    @start()
    def transcribe_meeting(self):
        print("Generating transcription")
        
        SCRIPT_DIR = Path(__file__).parent
        audio_path = str(SCRIPT_DIR / "EarningsCall.wav")
        
        audio = AudioSegment.from_file(audio_path, format="wav")
        
        chunk_len_ms = 60000
        chunks = make_chunks(audio, chunk_len_ms)
        
        full_transcription = ""
        for i, chunk in enumerate(chunks):
            print(f"Transcribing chunk {i+1}/{len(chunks)}")
            chunk_path = f"chunk_{i}.wav"
            chunk.export(chunk_path, format="wav")
            
            with open(chunk_path, "rb") as audio_file:
                transcription = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file
                )
                full_transcription += transcription.text + " "
                
        self.state.transcript = full_transcription

    
def kickoff():
    meeting_minutes_flow = MeetingMeetingFlow()
    meeting_minutes_flow.kickoff()

if __name__ == "__main__":
    kickoff()
