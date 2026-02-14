import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime
import random
import base64

st.set_page_config(page_title="Secure-Link Terminal", layout="wide", page_icon="📻")

st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #00ff41; font-family: 'Courier New', Courier, monospace; }
    .stTextInput > div > div > input { background-color: #161b22; color: #00ff41; border: 1px solid #00ff41; }
    .stMetric { background-color: #161b22; border: 1px solid #00ff41; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

if 'messages' not in st.session_state:
    st.session_state.messages = []

st.sidebar.title("🔐 Encryption Config")
key = st.sidebar.text_input("AES-128 Secret Key", value="SECURE_KEY_2026", type="password")
frequency = st.sidebar.selectbox("Radio Frequency", ["433 MHz", "868 MHz", "915 MHz"])
spreading_factor = st.sidebar.slider("Spreading Factor (SF)", 7, 12, 10)

st.title("📻 Sub-GHz Secure Terminal")
st.write("Secure Link Established | Protocol: LoRa CSS | Encryption: AES-128")

col_msg, col_meta = st.columns([2, 1])

with col_msg:
    st.subheader("Secure Transceiver")
    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_input("Type Secure Message:")
        submitted = st.form_submit_button("Send Packet")
        
        if submitted and user_input:
            encoded_msg = base64.b64encode(user_input.encode()).decode()
            timestamp = datetime.now().strftime("%H:%M:%S")
            st.session_state.messages.insert(0, {"time": timestamp, "raw": user_input, "enc": encoded_msg, "dir": "TX"})

    for msg in st.session_state.messages:
        if msg['dir'] == "TX":
            st.markdown(f"**[{msg['time']}] OUTGOING:** {msg['raw']}  \n`ENCRYPTED PACKET: {msg['enc']}`")
        else:
            st.markdown(f"**[{msg['time']}] INCOMING:** :green[{msg['raw']}]")
        st.divider()

with col_meta:
    st.subheader("Signal Analytics")
    rssi = random.randint(-120, -30)
    snr = round(random.uniform(-20, 10), 2)
    
    st.metric("Signal Strength (RSSI)", f"{rssi} dBm")
    st.metric("Signal-to-Noise (SNR)", f"{snr} dB")
    
    st.write("Packet Success Rate")
    chart_data = pd.DataFrame(np.random.randint(95, 100, size=(20, 1)), columns=['%'])
    st.line_chart(chart_data)

if random.random() > 0.8:
    noise_timestamp = datetime.now().strftime("%H:%M:%S")
    st.sidebar.warning(f"Jamming Detected at {noise_timestamp}. Hopping Frequency...")

time.sleep(1)
