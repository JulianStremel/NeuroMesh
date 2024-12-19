import enum
import socket
import struct
import threading

class ServiceType(enum.Enum):
    Sensor = 1
    Logic = 2
    Actuator = 3
    Storage = 4

class Data(struct.Struct):
    data:list[float] = None
    
    def __init__(self, data:list[float]):
        self.data = data
    
    def encode(self) -> bytes:
        tmp = struct.pack("!I",len(self.data))
        for i in self.data:
            tmp += struct.pack("!f",i)
        return tmp
    
    def decode(data:bytes) -> list[float]:
        tmp = []
        size = struct.unpack("!I",data[:4])[0]
        for i in range(size):
            tmp.append(struct.unpack("!f",data[4+i*4:8+i*4])[0])
        return tmp
    
class ServiceBase:

    def __init__(self,type:ServiceType):
        self.type = type
    
class Sensor(ServiceBase):
    
    def __init__(self):
        super().__init__(ServiceType.Sensor)
        self.output:tuple[str,int] = None
        self.sockOut =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def setOutput(self,output:tuple[str,int]):
        self.output = output
     
    def send(self,data:Data):
        try:
            self.sockOut.connect(self.output)
            self.sockOut.sendall(data.encode())
        except Exception as e:
            print(f"Failed to send data -> {e}")
    

class Logic(ServiceBase):
    
    def __handle_client__(self, callback,client_socket):
        try:
            while True:
                # Receive data from the client
                data = client_socket.recv(1024)
                if not data:
                    break

                # Call the provided callback with the received data
                callback(data)

        except ConnectionResetError:
            print("Connection reset by client.")
        finally:
            client_socket.close()
    
    def __init__(self):
        super().__init__(ServiceType.Logic)
        self.input:tuple[str,int] = None    
        self.sockIn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def setInput(self,input:tuple[str,int]):
        self.input = input    
    
    def start(self,callback):
        self.sockIn.bind((self.input[0], self.input[1]))
        self.sockIn.listen(5)
        print(f"Server listening on {self.input[0]}:{self.input[1]}")

        try:
            while True:
                client_socket, client_address = self.sockIn.accept()
                print(f"Accepted connection from {client_address}")
                client_thread = threading.Thread(target=self.__handle_client__, args=(callback,client_socket))
                client_thread.start()
        except Exception as e:
            print("error -> ",e)
        finally:
            self.sockIn.close()

class Actuator(ServiceBase):
    def __init__(self):
        super().__init__(ServiceType.Actuator)