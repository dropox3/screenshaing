from vidstream import ScreenShareClient
import threading


sender = ScreenShareClient('YOUR-IP', 9999)

t = threading.Thread(target=sender.start_stream)

t.start()

while input("") != 'STOP':
    continue

sender.stop_stream
