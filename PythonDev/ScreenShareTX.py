from vidstream import CameraClient
import threading
import cv2

# Replace the CameraClient's send_frame method to use matplotlib for displaying frames
def custom_send_frame(self, frame):
    try:
        cv2.imshow('Transmitter', frame)
        cv2.waitKey(1)
    except Exception as e:
        print(f"Error displaying frame: {e}")

CameraClient.send_frame = custom_send_frame

# Function to start the camera client
def start_camera_client(address, port):
    client = CameraClient(address, port)
    t = threading.Thread(target=client.start_stream)
    t.start()
    return client, t

# Start the camera client
client, t = start_camera_client('192.168.1.5', 9999)

while input("") != 'STOP':
    continue

client.stop_stream()
t.join()
cv2.destroyAllWindows()