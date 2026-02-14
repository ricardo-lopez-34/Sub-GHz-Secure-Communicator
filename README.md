# Sub-GHz Secure Communicator 📻

A long-range, off-grid messaging system utilizing LoRa technology and AES encryption to provide secure communication in network-deprived environments.

## Description
A long-range, off-grid messaging system utilizing LoRa technology and AES encryption to provide secure communication in network-deprived environments.

## Key Features
- **LoRa Telemetry:** Transmission range of up to 5km in open-field environments using 433MHz.
- **AES-128 Encryption:** Ensures end-to-end data privacy against packet sniffing and MITM attacks.
- **Frequency Hopping:** Minimizes interference and prevents signal jamming in contested spectrums.

## Tech Stack
- **Language:** Python, C++
- **Libraries:** Streamlit, LoRa-Lib, AES-Lib, PySerial
- **Model:** Symmetric-key cryptography for packet encapsulation.

## Engineering Logic
- **Hardware:** The Arduino Uno interfaces with the SX1278 LoRa module via SPI to modulate data into Chirp Spread Spectrum (CSS) signals.
- **Software:** Python acts as the "Command Terminal," encrypting the string before sending it to the hardware and decrypting incoming radio packets for display.
