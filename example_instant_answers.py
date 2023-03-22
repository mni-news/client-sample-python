import sys
import requests
import websocket

from frame import Frame


username = sys.argv[1]
password = sys.argv[2]

print("Logging in with: ", username)


response = requests.post("https://apis.marketnews.com/api/auth/client/token", 
    json={
        "username":username,
        "password":password
    },
    timeout= 30
)

print()
print("Auth response: ", response.status_code)

token = response.json()['access_token']


ws = websocket.WebSocket()
ws.connect("ws://127.0.0.1:61612/wss")


ws.send(Frame.marshall("CONNECT",{ 'passcode':token, 'heart-beat':'0,30000'},""))
print()
print(ws.recv())

ws.send(Frame.marshall("SUBSCRIBE",{'destination':"/topic/instant-answers"},""))

print("Starting listener loop ----")

while True:
    frameSource = ws.recv()

    print()

    if Frame.is_heartbeat(frameSource):
        print("Received: HEARTBEAT")
    else:
        frame = Frame.unmarshall_single(frameSource)
        print("Received:",frame.command)
        print("Content:",frame.body)
        


