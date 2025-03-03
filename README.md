# arduino-python-light-on-off
This is a very simple Arduino project involing WhisperMic in order to turn the built in light on the Arduino Mega 2560 Controller Board
# Hardware Components
Arduino Mega 2560 Controller
Any microphone (It will default to whatever microphone is detected e.g.: Webcam microphone, USB microphone, Headset microphone)
# Software Components
**IMPORTANT**: This project does not work on any Python 3.13 version, I recommend going to version 3.12
Any version of the Arduino IDE will work so nothing specific for that
- [WhisperMic](https://github.com/mallorbc/whisper_mic)
- [Python 3.12](https://www.python.org/downloads/release/python-3129/)
- Arduino IDE
- [PySerial](https://pypi.org/project/pyserial/)

# Steps
1. Download both the Python file and the ino file
2. Create a virtual environment (.venv or conda) for Python 3.12
3. pip install both WhisperMic and PySerial into the venv
4. Run the program and speak into your microphone
