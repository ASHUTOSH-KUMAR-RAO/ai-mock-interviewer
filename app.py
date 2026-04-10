# app.py

import streamlit as st
from config import APP_NAME, APP_ICON, AUTO_SAVE_INTERVAL
from src.chains import get_chain
from src.database import init_db, save_interview
from src.ui.styles import load_styles
from src.ui.components import render_header, render_welcome_placeholder
from src.audio import render_welcome_sound
from src.ui.sidebar import render_sidebar, render_history_view

# ── Init ──
st.set_page_config(page_title=APP_NAME, page_icon=APP_ICON, layout="wide")
init_db()

# ── Load Styles ──
st.markdown(load_styles(), unsafe_allow_html=True)

# ── Welcome Sound ──
render_welcome_sound()

# ── Header + Robot ──
render_header()

# ── Sidebar ──
role, difficulty = render_sidebar()

# ── History View ──
if render_history_view():
    st.stop()

# ── Session Init ──
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "chain" not in st.session_state:
    st.session_state.chain = get_chain()
if "current_topic" not in st.session_state:
    st.session_state.current_topic = ""
if "current_difficulty" not in st.session_state:
    st.session_state.current_difficulty = ""

# ── Chat Display ──
if not st.session_state.chat_history:
    render_welcome_placeholder()

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ── Chat Input ──
if user_input := st.chat_input("// Type your answer here..."):
    if not role:
        st.warning("⚠ ENTER A TOPIC IN THE CONTROL PANEL FIRST")
    else:
        st.session_state.current_topic = role
        st.session_state.current_difficulty = difficulty
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner("// PROCESSING..."):
                response = st.session_state.chain.invoke(
                    {"input": user_input, "role": f"{role} at {difficulty} level"},
                    config={"configurable": {"session_id": "interview_session"}}
                )
                answer = response.content
                st.markdown(answer)
                st.session_state.chat_history.append({"role": "assistant", "content": answer})

        # ── Auto Save ──
        if len(st.session_state.chat_history) % AUTO_SAVE_INTERVAL == 0:
            save_interview(
                topic=role,
                difficulty=difficulty,
                score="In Progress",
                conversation=st.session_state.chat_history
            )
