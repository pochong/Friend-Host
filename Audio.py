import pyaudio
import time

#variables
chunk = 4096
audio_format = pyaudio.paInt16
channels = 1
rate_of_transfer = 10000
#setting up the microphone
while 1 :
    p = pyaudio.PyAudio()
    record = p.open(format = audio_format, 
                    channels = channels, 
                    rate = rate_of_transfer,
                    input = True,
                    frames_per_buffer = chunk)
    playing = p.open(format = audio_format, 
                    channels = channels, 
                    rate = rate_of_transfer,
                    output = True,
                    frames_per_buffer = chunk)

    #print("microphone working")

    data = record.read(4096)

    time.sleep(0.1)

    playing.write(data)
    


