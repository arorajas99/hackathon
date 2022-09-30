from typing import Optional
from twilio.rest import Client
import serial
import struct
import time

arduino = serial.Serial('COM4', 9600)


def Measure():
    global distance
    distance = arduino.readline()
    # print(int(float(distance)))

    return float(distance)



def sus():
    account_sid = 'AC509864713fdb4303e4e311437429f752'
    auth_token = '0d25da60160d37f451e1d7141f067947'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='MOTION DETECTED!! Kindly Pay Attention ',
        from_='+17754028167',
        to='+918791147322'
    )

while True:
    output = Measure()
    b = int(float(arduino.readline()))
    print(b)
    if b <= 30:
        print("STRANGER THINGS")
        sus()

