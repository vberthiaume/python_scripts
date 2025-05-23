from pythonosc import udp_client
from math import sin, pi
from time import sleep

address = "127.0.0.1"
port = 9002
client = udp_client.SimpleUDPClient(address, port)

while True:
    for i in range(20):
        x = (i / 19) * 2 * pi
        value = sin(x)
        print(value)
        client.send_message(f"/juce/rotaryknob", value)
        sleep(1)