# Import socket module
import socket
from pynput.keyboard import Listener, Key
import sys

s = None

def on_press(key):
    if key == Key.left: 
        print('left key was pressed')
        s.send("left".encode('ascii'))
    elif key == Key.right: 
        print('right key was pressed')
        s.send("right".encode('ascii'))
    elif key == Key.enter: 
        print('closing connection')
        s.close()
        exit()
    else:
    	print("key pressed")



# local host IP '127.0.0.1'
host = sys.argv[1]

# Define the port on which you want to connect
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# connect to server on local computer
s.connect((host,port))

print("connected")

with Listener(on_press=on_press) as listener:  # Setup the listener
	listener.join()  # Join the thread to the main thread
