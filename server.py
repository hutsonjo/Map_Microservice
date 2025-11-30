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
        response = {"error": "Missing service_key"}

    # RPG map service routing
    elif service_key == 'rpg':
        map_name = data['map']
        x, y = data['coords']

        # Error handling for missing or invalid map_name
        if map_name not in rpg_map_list:
            response = {'status': 'error', 'data': RPG_ERROR}

        # If new position within bounds of map, add tile info to response, error otherwise
        if 0 <= x < len(test_map) and 0 <= y < len(test_map[0]):
            position = test_map[x][y]
            response = {'status': 'success', 'data': position}
        else:
            response = {'status': 'out_of_bounds', 'data': RPG_OUTOFBOUNDS}

    socket.send_json(response)
