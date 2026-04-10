# src/audio.py

from gtts import gTTS
import os
import base64
import streamlit as st
from config import WELCOME_MESSAGE

AUDIO_PATH = "welcome.mp3"

def generate_welcome_audio():
    if not os.path.exists(AUDIO_PATH):
        tts = gTTS(text=WELCOME_MESSAGE, lang='en', slow=False)
        tts.save(AUDIO_PATH)

def render_welcome_sound():
    if "welcomed" not in st.session_state:
        st.session_state.welcomed = True
        generate_welcome_audio()
        with open(AUDIO_PATH, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        st.markdown(f"""
        <audio autoplay style="display:none;">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """, unsafe_allow_html=True)
