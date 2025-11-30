import zmq
from rpg_map import *

# Initialize context and socket
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5557")

while True:
    # Receive and extract data from requesting client
    request = socket.recv_json()
    print(f"Received request: {request}")
    service_key = request.get("service_key")
    data = request.get("data", {})
    response = {}

    # Error handling for missing service key
    if not service_key:
        response = {'status': 'error', 'data': "Missing service_key"}

    # RPG map service routing
    elif service_key == 'rpg':
        map_name = data['map']
        x, y = data['coords']

        # Error handling for missing or invalid map_name
        if map_name not in rpg_maps:
            response = {'status': 'error', 'data': RPG_ERROR}

        # If position within bounds of map, add tile info to response, error otherwise
        else:
            target_map = rpg_maps[map_name]
            response = target_map.get_tile(x, y)

    print(f"Sending response: {response}")
    socket.send_json(response)
