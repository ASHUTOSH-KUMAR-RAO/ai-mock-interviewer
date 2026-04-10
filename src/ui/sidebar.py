# src/ui/sidebar.py

import streamlit as st
import json
from src.chains import get_chain
from src.database import save_interview, get_all_interviews, get_interview_by_id
from config import DIFFICULTY_LEVELS

def render_sidebar():
    with st.sidebar:
        st.markdown('<div style="font-family: Orbitron, monospace; color: #00ffe7; font-size: 1rem; font-weight: 700; letter-spacing: 2px; text-shadow: 0 0 10px #00ffe7;">⚙ CONTROL PANEL</div>', unsafe_allow_html=True)
        st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)

        role = st.text_input(
            "📡 TOPIC",
            placeholder="e.g. LangChain, DSA, System Design..."
        )

        difficulty = st.selectbox("⚡ DIFFICULTY", DIFFICULTY_LEVELS)

        if st.button("🔄 NEW INTERVIEW"):
            if st.session_state.get("chat_history") and st.session_state.get("current_topic"):
                save_interview(
                    topic=st.session_state.get("current_topic", "Unknown"),
                    difficulty=st.session_state.get("current_difficulty", "Unknown"),
                    score="N/A",
                    conversation=st.session_state.chat_history
                )
            st.session_state.chat_history = []
            st.session_state.store = {}
            st.session_state.chain = get_chain()
            st.session_state.current_topic = role
            st.session_state.current_difficulty = difficulty
            st.rerun()

        st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)

        # ── Past Interviews ──
        st.markdown('<div style="font-family: Orbitron, monospace; color: #ff00cc; font-size: 0.8rem; letter-spacing: 2px; text-shadow: 0 0 8px #ff00cc;">📂 PAST INTERVIEWS</div>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        past = get_all_interviews()
        if past:
            for interview in past[:8]:
                id_, topic, diff, score, date = interview
                if st.button(f"🗂 {topic} [{diff}]\n{date}", key=f"hist_{id_}"):
                    st.session_state.viewing_history = id_
                    st.rerun()
        else:
            st.markdown('<div style="color: rgba(0,255,231,0.4); font-size: 0.75rem;">No past interviews yet...</div>', unsafe_allow_html=True)

    return role, difficulty

def render_history_view():
    if st.session_state.get("viewing_history"):
        row = get_interview_by_id(st.session_state.viewing_history)
        if row:
            id_, topic, diff, score, date, convo = row
            st.markdown(f'<div style="font-family: Orbitron, monospace; color: #ff00cc; font-size: 0.9rem; margin-bottom: 10px;">📂 {topic} [{diff}] — {date}</div>', unsafe_allow_html=True)
            messages = json.loads(convo)
            for msg in messages:
                with st.chat_message(msg["role"]):
                    st.markdown(msg["content"])
            if st.button("❌ CLOSE HISTORY"):
                st.session_state.viewing_history = None
                st.rerun()
            return True
    return False
