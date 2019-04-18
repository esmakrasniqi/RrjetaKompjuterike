from socket import *

server = "localhost"
port = 12000

print("Per te zgjedhur sherbimin shkruani fjalet:")
print("IPADRESA, \nNUMRIIPORTIT, \nBASHKETINGELLORE, \nPRINTIMI, \nEMRIIKOMPJUTERIT,\nKOHA, \nLOJA, \nFIBONACCI, \nKONVERTIMI, \nMAX, \nMIN\n\n")
       
try:
    clientSocket = socket(AF_INET, SOCK_DGRAM)
except socket.error:
    print ('Problem ne krijimin e soketes')
pass

while True:
       
    Operacioni = input("Operacioni: ").upper()
    clientSocket.sendto(Operacioni.encode("ASCII"), (server, port))

    while Operacioni == "":
      
        print("IPADRESA, NUMRIIPORTIT, BASHKETINGELLORE, PRINTIMI, EMRIIKOMPJUTERIT, KOHA, LOJA, FIBONACCI,  KONVERTIMI,  MAX,  MIN")
        Operacioni = input("Operacioni: ").upper()
        
    try:
        pergjigjja, adresa = clientSocket.recvfrom(2048)
        print("pergjigjja: " + pergjigjja.decode("ASCII"))
    except:
            print("Operacioni nuk mund te dergohet!")

    pass

clientSocket.close()

