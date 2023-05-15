import os, sys
from PyP100 import PyP100
from dotenv import dotenv_values, load_dotenv

load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

# States
states = ["on","off","toggle"]

# Define the array
device_ips = {
    "micro": "192.168.68.100",
    "camera": "192.168.68.110",
}

arguments = sys.argv
device = sys.argv[1]
state = sys.argv[2]

p100 = PyP100.P100(device_ips[device], username, password)
res = p100.handshake()
res = p100.login()

if (state == "on"):
    p100.turnOn()

if (state == "off"):
    p100.turnOff()

if (state == "toggle"):
    p100.toggleState()
