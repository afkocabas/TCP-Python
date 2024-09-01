from socket import *

class TCPServer:
    
    def __init__(self, serverPort=1200) -> None:

        # Initiliaze the socket in IPv4 and as TCP Socket
        self.port = serverPort
        # Bind socket ot 
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind(("", self.port))

        
    def run(self):

        print(f"The server is listening port {self.port}.")

        while True:
            # Start socket to listen to the its ports for the connections
            self.socket.listen()
            connectionSocket, address = self.socket.accept()
            while True:
            # Recieve data through the socket
                try:
                    data = connectionSocket.recv(1024)
                    if data == b'close': 
                        print(f"TCP connection between {address} is terminated.")
                        break

                    print(f"Data received over TCP: {data}")
                    # Send back the data itself
                    connectionSocket.send(data)
                except ConnectionResetError:
                    print(f"Exception: {address} left the connection unexpectedly.")
                    break

if __name__ == "__main__":
    
    server = TCPServer()
    server.run()