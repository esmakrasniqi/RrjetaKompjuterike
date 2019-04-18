from socket import *

server = "localhost"
port = 12000

print("Per te zgjedhur sherbimin shkruani fjalet:")
print("IPADRESA, \nNUMRIIPORTIT, \nBASHKETINGELLORE, \nPRINTIMI, \nEMRIIKOMPJUTERIT,\nKOHA, \nLOJA, \nFIBONACCI, \nKONVERTIMI, \nMAX, \nMIN\n\n")
while True:
    try:
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((server,port))
    except :
        print("Lidhja nuk mund te realizohet!")
        break
    pass
    
    
    Operacioni = input("Operacioni: ").upper()
    
    while Operacioni == "":
       print("IPADRESA, NUMRIIPORTIT, BASHKETINGELLORE, PRINTIMI, EMRIIKOMPJUTERIT, KOHA, LOJA, FIBONACCI, KONVERTIMI, MAX, MIN")
       Operacioni = input("Operacioni: ").upper()
        
    try:
        clientSocket.send(Operacioni.encode("ASCII"))
    except:
        print("Operacioni nuk mund te dergohet!")
    pass
    

    pergjigjja = clientSocket.recv(2048)

    print("pergjigjja: " + pergjigjja.decode("ASCII"))
    
clientSocket.close()
input()

