from pythonosc import udp_client
from time import sleep
import random

address = "127.0.0.1"
port = 9002
client = udp_client.SimpleUDPClient(address, port)

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

while True:
    for i in range(20):
        letter = random.choice(letters)
        print(letter)
        client.send_message(f"/note", letter)
        sleep(.5)
