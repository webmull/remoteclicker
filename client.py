# Import socket module
import socket
from pynput.keyboard import Listener, Key
import sys

s = None

def on_press(key):
    if key == Key.left:  # If space was pressed, write a space
        print('left key was pressed')
        s.send("left".encode('ascii'))
    elif key == Key.right:  # If enter was pressed, write a new line
        print('right key was pressed')
        s.send("right".encode('ascii'))
    elif key == Key.enter:  # If enter was pressed, write a new line
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



	# while True:

	# 	# message sent to server
	# 	s.send(message.encode('ascii'))

	# 	# messaga received from server
	# 	data = s.recv(1024)

	# 	# print the received message
	# 	# here it would be a reverse of sent message
	# 	print('Received from the server :',str(data.decode('ascii')))

	# 	# ask the client whether he wants to continue
	# 	ans = input('\nDo you want to continue(y/n) :')
	# 	if ans == 'y':
	# 		continue
	# 	else:
	# 		break
	# # close the connection
	# s.close()
