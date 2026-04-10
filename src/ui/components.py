# src/ui/components.py

import streamlit as st

ROBOT_HTML = """
<div style="display:flex; justify-content:center; margin: 10px 0 20px 0;">
<svg width="80" height="110" viewBox="0 0 80 110" xmlns="http://www.w3.org/2000/svg">
  <style>
    @keyframes float { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-8px)} }
    @keyframes blink { 0%,89%,100%{ry:6px} 90%,95%{ry:1px} }
    @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.3} }
    @keyframes talk { 0%{height:3px} 100%{height:8px} }
    .robot { animation: float 3s ease-in-out infinite; }
    .eye { animation: blink 4s infinite; }
    .chest { animation: pulse 1s infinite; }
    .mouth { animation: talk 0.4s infinite alternate; }
  </style>
  <g class="robot">
    <rect x="10" y="0" width="60" height="50" rx="10" fill="#16213e" stroke="#00ffe7" stroke-width="2" filter="url(#glow)"/>
    <ellipse class="eye" cx="28" cy="20" rx="7" ry="6" fill="#00ffe7"/>
    <ellipse class="eye" cx="52" cy="20" rx="7" ry="6" fill="#00ffe7"/>
    <rect class="mouth" x="27" y="36" width="26" height="3" rx="2" fill="#ff00cc"/>
    <rect x="5" y="55" width="70" height="45" rx="8" fill="#16213e" stroke="#00ffe7" stroke-width="2"/>
    <rect x="25" y="67" width="30" height="22" rx="4" fill="rgba(0,255,231,0.1)" stroke="#00ffe7" stroke-width="1"/>
    <ellipse class="chest" cx="40" cy="78" rx="6" ry="6" fill="#ff00cc"/>
  </g>
  <defs>
    <filter id="glow">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
</svg>
</div>
"""

def render_header():
    st.markdown('<div class="cyber-title">⬡ NEXUS ⬡</div>', unsafe_allow_html=True)
    st.markdown('<div class="cyber-subtitle">"[ NEXUS v1.0 — WHERE PREPARATION MEETS INTELLIGENCE ]"</div>', unsafe_allow_html=True)
    st.markdown(ROBOT_HTML, unsafe_allow_html=True)
    st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)

def render_welcome_placeholder():
    st.markdown('<div class="welcome-text">[ SELECT A TOPIC AND START TYPING TO BEGIN YOUR INTERVIEW ]</div>', unsafe_allow_html=True)

def render_neon_divider():
    st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)
