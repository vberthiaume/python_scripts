from pythonosc import udp_client
from math import sin
from time import sleep

address = "127.0.0.1"
port = 9001
client = udp_client.SimpleUDPClient(address, port)
counter = 0

while True:
      counter+=0.1
      for i in range(20):
            client.send_message(f"/{i}/size", sin(i+counter)+2)
      sleep(2)
