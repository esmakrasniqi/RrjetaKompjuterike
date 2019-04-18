from socket import *
import platform  
from time import gmtime, strftime
import math
import ipaddress
import random 
port = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)

try:
    serverSocket.bind(('',port))
    serverSocket.listen()
    vlera = True
except:
    print("Vetem nje instance e serverit eshte e lejuar!")
    vlera = False
    pass

if vlera:
    print("FIEK TCP Serveri eshte i gatshem...\n")
else:
    print("FIEK TCP Serveri nuk mund te starohet!")

while vlera:
    try:
        connectionSocket, adresa = serverSocket.accept()
        Operacioni = connectionSocket.recv(2048)

        kushti = Operacioni.decode("ASCII")

        socketName = socket.getsockname(connectionSocket)
        print( socketName[0] + ":" + str(socketName[1]) + " Operacioni " + kushti.split(" ")[0] + " eshte pranuar...")
    except:
        continue
        pass


    if kushti == "IPADRESA":
        pergjigjja =  "IP adresa e klientit eshte " + socketName[0]
    elif kushti == "NUMRIIPORTIT":
        pergjigjja = "Klienti eshte duke perdorur portin " + str(socketName[1])
    elif kushti[0:16] == "BASHKETINGELLORE":
        if kushti[0:17] == "BASHKETINGELLORE ":
            string = kushti[17:len(kushti)]
            string = string.replace(" ", "")
            numri_bashketingelloreve = 0
            for i in string:
             if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
              continue
             else:
                numri_bashketingelloreve=numri_bashketingelloreve + 1

            pergjigjja = " Teksti derguar permban " + str(numri_bashketingelloreve) + " bashketingellore.  "
        else:
            pergjigjja = "Formati: BASHKETINGELLORE [teksti]";


    elif kushti[0:8] == "PRINTIMI":
        if kushti[0:9] == "PRINTIMI ":
            pergjigjja = kushti[9:len(kushti)].lower().capitalize()
        else:
            pergjigjja = "Formati: PRINTIMI [teksti]";

    elif kushti[0:3] == "MAX":
        if kushti[3:4] == " ":
            kushti = kushti.split(" ")

            num1 = int(kushti[1])
            num2 = int(kushti[2])

            if (num1 > num2):
                pergjigjja = kushti[1]
            else:
                pergjigjja = kushti[2]
        else:
            pergjigjja = "MAX [numri] [numri]"

    elif kushti[0:3] == "MIN":
        if kushti[3:4] == " ":
            kushti = kushti.split(" ")

            num1 = int(kushti[1])
            num2 = int(kushti[2])

            if (num1 < num2):
                pergjigjja = kushti[1]
            else:
                pergjigjja = kushti[2]
        else:
            pergjigjja = "MIN [numri] [numri]"


    elif kushti == "EMRIIKOMPJUTERIT":
        try:
            h = platform.uname()[1]
            pergjigjja = "Emri i klientit eshte " + h
        except:
            pergjigjja = "Emri i klientit nuk dihet"
    elif kushti == "KOHA":
        pergjigjja = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    elif kushti == "LOJA": 
        array = []
        for i in range(0, 7):
            array.append(random.randint(1,49))
        array.sort()
        pergjigjja = str(array)[1:-1]
                
    elif kushti[0:10] == "KONVERTIMI":
        if kushti[10:11] == " ":
            string = kushti.split(" ")
            if string[1] == '1':
                pergjigjja = str(float(string[2]) *  1.341)
            elif string[1] == '2':
                pergjigjja = str(float(string[2]) /  1.341)
            elif string[1] == '3':
                pergjigjja = str(float(string[2]) * 3.14 / 180)
            elif string[1] == '4':
                 pergjigjja = str(float(string[2]) * 180/ 3.14)
            elif string[1] == '5':
                pergjigjja = str(float(string[2]) * 3.785)
            elif string[1] == '6':
                pergjigjja = str(float(string[2]) / 3.785)
     
            else:
                pergjigjja = "Shkruaj njerin nga opsionet [ 1 - 6 ]"
        else:
            pergjigjja = "Formati: KONVERTIMI [NUMRI I OPERACIONI] [VLERA PER KONVERTIM]"
            pergjigjja += "\nZgjedh njerin nga OPERACIONET:"
            pergjigjja += "\n1 - KilowattToHorsepower"
            pergjigjja += "\n2 - HorsepowerToKilowatt" 
            pergjigjja += "\n3 - DegreesToRadians" 
            pergjigjja += "\n4 - RadiansToDegrees"
            pergjigjja += "\n5 - GallonsToLiters"
            pergjigjja += "\n6 - LitersToGallons"


   
    elif kushti[0:9] =="FIBONACCI":
        numri_pare = 1 
        numri_dyte = 0
        if kushti[9:10] == " ":
            for i in range(1, int(kushti[10:len(kushti)])):
                shuma = numri_pare + numri_dyte
                numri_dyte = numri_pare
                numri_pare = shuma
            pergjigjja = str(shuma)
        else:
            pergjigjja = "Formati: FIBONACCI [numri]";

  
    try:
        connectionSocket.send(pergjigjja.encode("ASCII"))
        print( socketName[0] + ":" + str(socketName[1]) + " pergjigjja " + kushti.split(" ")[0] + " eshte derguar...")
    except:
        print(socketName[0] + ":" + str(socketName[1]) + " pergjigjja nuk mund te dergohet!")
        pass        

