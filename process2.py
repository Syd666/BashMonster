import socket
import os, os.path


print "I will be ready for communication"
PATH = "/home/back/unix_example"
if os.path.exists(PATH):
    client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    client.connect(PATH)
    print "[*]Read?"
    print "[*] Ctrl-C to quite."
    print "Sending 'DONE'  will shut down the server"
    while True:
        try:
            x = raw_input(">")
            if "" != x:
                print "SEND: ", x
                client.send(x)
                if "DONE" == x:
                    print "Bye-Bye"
                    break
        except KeyboardInterrupt, k :
            print "Shutting Down."
    client.close()

else: 
    print "Sorry can't get it up and running. :("
 
