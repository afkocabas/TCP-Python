from socket import *

class TCPClient:
    
    def __init__(self, serverPort=1200, serverName="localhost") -> None:
        
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.serverPort = serverPort 
        self.serverName = serverName

    def run(self):

        self.socket.connect((self.serverName, self.serverPort))

        while True:
            try:
                message = input("Data to be sent over TCP: ")

                self.socket.send(message.encode("utf-8"))
                if message == "close":
                    self.socket.close()
                    break
                data = self.socket.recv(1024)
            except ConnectionResetError:
                print("TCP connection is shut down unexpectedly.")
                self.socket.close()

            print("The message recieved", data)


if __name__ == "__main__":
    
    client = TCPClient()
    client.run()



        