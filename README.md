# Map Microservice

A Python-based microservice capable of receiving requests for the information contained at specific coordinates
of a specific map.

### How It Works

server.py runs as a server using a ZeroMQ REP socket.

   * It listens for incoming requests via a TCP server connection.
   * It sends back a JSON containing status and data
     * Data will contain a JSON with values corresponding to the coordinates sent or error information.
   * Requests musts be made in valid JSON format.

### Service keys

`rpg`: Will search for tile information for map objects in rpg_map.py

### Request formats
To use the NPC Microservice, a client must send a JSON-formatted request which includes the following:

1. `service_key` (string) - identifies which service to use.
2. `data` (dict) - Contains the parameters for the map request.
   * `map` (string) - The name of the map being referenced.
   * `coords` (list[int, int]) - x & y coordinates used to find tile information.

### Making a Request

1. Establish a ZeroMQ context object
2. Create a socket w/ the context & establish connection on the host and port with 'socket = context.socket(zmq.REQ)'
   * connection is currently set to target "tcp://localhost:5557"
3. Create a valid JSON in the format listed in the section above.
4. Send the JSON via 'socket.send_json()'

#### Example Request
```python
import zmq

context = zmq.Context()

print("Connecting to server")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:55555")

request = {
   "service_key": "rpg",
   "data": {
      "map": 'test_map', 
      "coords": [5, 5]
   }
}
socket.send_json(request)
```
### Receiving a Response

After having sent the data, assign a variable equal to 'socket.recv()'

### Response Format

```python
response = {
    'narration': "The land that surrounds you is scorched. No life could ever live here.",
    'inspection': "you feel as though you are being watched.",
    'biome': 'scorched',
    'encounter': 5
}
```

#### Example of Receiving
```python
response = socket.recv_json()
```

## Tech Stack

Python 3.13

ZeroMQ (pyzmq) — Microservice communication

JSON — Data serialization for requests and responses

### Author

Joshua Hutson

#### Author Note

Currently, there is only one viable service key. Service key format was implemented to allow for modularity and future
improvements/additions.