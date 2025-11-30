import zmq

# Establish socket and timeout settings
context = zmq.Context()
print("Connecting to server")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5557")
socket.setsockopt(zmq.RCVTIMEO, 1000)
socket.setsockopt(zmq.SNDTIMEO, 1000)

# Requesting tile info for a coordinate from the test map
request = {
   "service_key": "rpg",
   "data": {
      "map": 'test_map',
      "coords": [5, 5]
   }
}
print(f"Sending request: {request}")
socket.send_json(request)

# Receive the tile info and print the response
npc = socket.recv_json()
print(f"Received response: {npc}")
