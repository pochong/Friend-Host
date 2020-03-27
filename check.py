import pyaudio 
import time

chunk = 4096
audio_format = pyaudio.paInt16
channels = 2
rate_of_transfer = 10000
devices = 2
data = []

p = pyaudio.PyAudio()
device = p.get_device_info_by_index(devices)
print(device)
device = p.get_device_info_by_index(1)
print(device)
for i in range(30):
    stream = p.open(format=audio_format, channels=channels, rate=rate_of_transfer, input=True, output=True, frames_per_buffer=chunk, input_device_index=devices)
    stream2 = p.open(format=audio_format, channels=channels, rate=rate_of_transfer, input=True, output=True, frames_per_buffer=chunk)
    data.append(stream.read(4096))
    data.append(stream2.read(4096))
    print(i)
print("done recording")

time.sleep(0.1)

for x in range(len(data)):
    stream.write(data[x])

# p = pyaudio.PyAudio()
# host_info = p.get_host_api_info_by_index(0)    
# device_count = host_info.get('deviceCount')
# devices1 = []

# # iterate between devices:
# for s in range(0, device_count):
#     device1 = p.get_device_info_by_index(s)
#     devices1.append(device1)

# for x in range(len(devices1)):
#     print(devices1[x])