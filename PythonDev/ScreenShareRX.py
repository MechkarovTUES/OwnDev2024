from vidstream import StreamingServer
import threading
import cv2
import numpy as np
from matplotlib import pyplot as plt

reciever = StreamingServer('192.168.1.5', 9999)

def display_frame(address, frame):
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.title(str(address))
    plt.show(block=False)
    plt.pause(0.001)
    plt.close()

def client_connection_wrapper(address, frame):
    try:
        display_frame(address, frame)
    except Exception as e:
        print(f"Error displaying frame from {address}: {e}")

def custom_client_connection(self):
    while self._running:
        conn, address = self.server.accept()
        conn.settimeout(self.timeout)
        while self._running:
            try:
                length = conn.recv(self.header_length)
                if not length:
                    break
                length = int(length.decode())
                frame_data = b""
                while len(frame_data) < length:
                    packet = conn.recv(self.buffer_size)
                    if not packet:
                        break
                    frame_data += packet
                frame = np.frombuffer(frame_data, dtype=np.uint8).reshape(self.frame_height, self.frame_width, self.frame_channels)
                threading.Thread(target=client_connection_wrapper, args=(address, frame)).start()
            except Exception as e:
                print(f"Error in client connection: {e}")
                break
        conn.close()

# Monkey patch the original __client_connection method
StreamingServer.__client_connection = custom_client_connection

t = threading.Thread(target=reciever.start_server)
t.start()

while input("") != 'STOP':
    continue

reciever.stop_server()