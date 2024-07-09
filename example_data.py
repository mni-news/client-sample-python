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


# Fetch Scheduled Instant Answers From REST API


response = requests.get("https://apis.marketnews.com/api/select/calendar/events?size=100", 
    headers={
        "Authorization": "Bearer " + token
    },
    timeout= 30
)

events = response.json()['content']

for e in events:
    for s in e['dataSeriesEntries']:
        print(e['date'] + " - " + s['display'])




# Connect to Websocket and wait for data

ws = websocket.WebSocket()
ws.connect("wss://apis.marketnews.com/wss")


ws.send(Frame.marshall("CONNECT",{ 'passcode':token, 'heart-beat':'0,30000'},""))
print()
print(ws.recv())

print("Subscribing to data events ----")
ws.send(Frame.marshall("SUBSCRIBE",{'destination':"/topic/observations"},""))

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
        


