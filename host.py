import select
import socket
import pyautogui


def main() -> None:
    host = ""
    port = 12345

    # create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setblocking(0)
        # bind the socket to the port
        sock.bind((host, port))
        # listen for incoming connections
        sock.listen(5)
        print("Server started...")

        # sockets from which we expect to read
        inputs = [sock]
        outputs = []

        while inputs:
            # wait for at least one of the sockets to be ready for processing
            readable, writable, exceptional = select.select(inputs, outputs, inputs)

            for s in readable:
                if s is sock:
                    conn, addr = s.accept()
                    inputs.append(conn)
                else:
                    data = s.recv(1024)
                    if data:
                        decoded = data.decode()
                        if decoded == 'right':
                            print("right pressed")
                            pyautogui.press('down') 
                        elif decoded == 'left':
                            print("left pressed")
                            pyautogui.press('up') 

                        # if()
                        # pyautogui.press('f1') 

                    else:
                        inputs.remove(s)
                        s.close()

if __name__ == "__main__":
    main()