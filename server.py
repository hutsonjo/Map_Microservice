import zmq
from rpg_map import *

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5557")

while True:
    message = socket.recv_json()
    print(message)
    map_name = message['map']
    x, y = message['coords']
    if map_name != NAME:
        socket.send_json({'status': 'error', 'data': ERROR})
    if 0 <= x < len(test_map) and 0 <= y < len(test_map[0]):
        position = test_map[x][y]
        socket.send_json({'status': 'success', 'data': position})
    else:
        socket.send_json({'status': 'out_of_bounds', 'data': OUTOFBOUNDS})