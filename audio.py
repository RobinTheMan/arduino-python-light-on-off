#Robert Wierzal

#The python part that uses WhisperMic in order to send an "on" and "off" signal to the arduino

from whisper_mic import WhisperMic

import serial
import time


port = "COM3"
baud_rate = 9600
arduino = serial.Serial(port, baud_rate)

keywords = ["on", "off", "stop"]

while True:
    mic = WhisperMic()
    result = mic.listen()
    print(result)
    # Convert the transcribed text to lowercase for case-insensitive matching
    result = result.lower()

    # Check for the presence of keywords
    detected_keywords = [word for word in keywords if word.lower() in result]

    if detected_keywords:
        print("Detected Keywords: ", detected_keywords)
    else:
        print("No keywords detected.")

    try:
        # Send data
        try:
            message_to_send = detected_keywords.pop()
        except IndexError: #If there are no detected keywords, it prints out a statement and just ends it there
                print('Cannot use as input')
                break
        if message_to_send == 'stop': #Also a clear way to stop the program, even though as of now it can be stopped by just
            print ("Goodbye!")        #Using another word that isn't "on" or "off
            break
        else:
            arduino.write(message_to_send.encode('utf-8')) #Sends it to the arduino in utf-8
            print(f"Sent: {message_to_send.strip()}") 
                # Receive data
            if arduino.in_waiting > 0:
                received_data = arduino.readline().decode('utf-8').strip()
                print(f"Received: {received_data}")
            time.sleep(1)  # Wait for 1 second
    except serial.SerialException as e:
        print(f"Error: {e}")