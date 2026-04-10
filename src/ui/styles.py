# src/ui/styles.py

CYBERPUNK_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Share+Tech+Mono&display=swap');

html, body, [class*="css"] {
    font-family: 'Share Tech Mono', monospace;
    background-color: #0a0a0f;
    color: #e0e0ff;
}

.stApp { background: #0a0a0f; }

.stApp::before {
    content: "";
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: repeating-linear-gradient(
        0deg,
        transparent,
        transparent 2px,
        rgba(0, 255, 200, 0.015) 2px,
        rgba(0, 255, 200, 0.015) 4px
    );
    pointer-events: none;
    z-index: 9999;
}

.cyber-title {
    font-family: 'Orbitron', monospace;
    font-size: 2.4rem;
    font-weight: 900;
    text-align: center;
    color: #00ffe7;
    text-shadow: 0 0 10px #00ffe7, 0 0 30px #00ffe7, 0 0 60px #00ffe7;
    letter-spacing: 4px;
    animation: flicker 3s infinite;
}

.cyber-subtitle {
    font-family: 'Share Tech Mono', monospace;
    text-align: center;
    color: #ff00cc;
    font-size: 0.85rem;
    letter-spacing: 3px;
    text-shadow: 0 0 8px #ff00cc;
}

@keyframes flicker {
    0%, 95%, 100% { opacity: 1; }
    96% { opacity: 0.4; }
    97% { opacity: 1; }
    98% { opacity: 0.2; }
    99% { opacity: 1; }
}

.neon-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, #00ffe7, #ff00cc, transparent);
    margin: 15px 0;
    box-shadow: 0 0 8px #00ffe7;
}

/* Chat Messages */
[data-testid="stChatMessageContent"] {
    background: rgba(0, 255, 231, 0.05) !important;
    border: 1px solid rgba(0, 255, 231, 0.2) !important;
    border-radius: 12px !important;
    box-shadow: 0 0 10px rgba(0, 255, 231, 0.1) !important;
    font-family: 'Share Tech Mono', monospace !important;
}

[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) [data-testid="stChatMessageContent"] {
    background: rgba(255, 0, 204, 0.05) !important;
    border-color: rgba(255, 0, 204, 0.3) !important;
    box-shadow: 0 0 10px rgba(255, 0, 204, 0.1) !important;
}

/* Chat Width Fix */
[data-testid="stChatMessageContainer"] {
    max-width: 750px !important;
    margin: 0 auto !important;
}

[data-testid="stChatMessage"] {
    max-width: 750px !important;
    margin: 0 auto 10px auto !important;
}

/* Input Fix */
[data-testid="stChatInput"] {
    max-width: 750px !important;
    margin: 0 auto !important;
}

.stChatInput textarea {
    background: rgba(0, 255, 231, 0.05) !important;
    border: 1px solid #00ffe7 !important;
    color: #e0e0ff !important;
    font-family: 'Share Tech Mono', monospace !important;
    box-shadow: 0 0 15px rgba(0, 255, 231, 0.2) !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #0d0d1a !important;
    border-right: 1px solid rgba(0, 255, 231, 0.2) !important;
}

/* Buttons */
.stButton button {
    background: transparent !important;
    border: 1px solid #00ffe7 !important;
    color: #00ffe7 !important;
    font-family: 'Orbitron', monospace !important;
    letter-spacing: 2px !important;
    font-size: 0.75rem !important;
    border-radius: 4px !important;
    transition: all 0.3s !important;
    text-transform: uppercase !important;
}

.stButton button:hover {
    background: rgba(0, 255, 231, 0.1) !important;
    box-shadow: 0 0 20px rgba(0, 255, 231, 0.4) !important;
    transform: translateY(-1px) !important;
}

/* Inputs */
.stSelectbox > div > div,
.stTextInput > div > div > input {
    background: rgba(0, 255, 231, 0.05) !important;
    border: 1px solid rgba(0, 255, 231, 0.3) !important;
    color: #e0e0ff !important;
    font-family: 'Share Tech Mono', monospace !important;
}

/* Welcome Text */
.welcome-text {
    font-family: 'Orbitron', monospace;
    color: #00ffe7;
    text-align: center;
    font-size: 1rem;
    text-shadow: 0 0 10px #00ffe7;
    animation: fadeInUp 1s ease forwards;
    opacity: 0;
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Scrollbar */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #0a0a0f; }
::-webkit-scrollbar-thumb { background: #00ffe7; border-radius: 2px; }
</style>
"""

def load_styles():
    return CYBERPUNK_CSS    
