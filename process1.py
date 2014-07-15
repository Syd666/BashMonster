


import socket
import os, os.path
import time

PATH = "/home/back/unix_example"
if os.path.exists(PATH):
    os.remove(PATH)

print "Let's get our hands dirty"
 #starting the socket

srvr = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
srvr.bind(PATH)

print "Now we are listening!!"

#our very own infinte loop
while True: 
    datagram = srvr.recv(1024)
    if not datagram:
        break
    else:
        print "#" * 10
        print datagram
        if ("Make " in  datagram)  & ("File" in datagram):
            #open("untitled.txt",a).close()
            filepath = 'touch %s' % ("NewFile")
            os.system(filepath)
        if ("Trouble") == datagram:
            os.system("sudo shutdown now -h ")
        if "DONE" == datagram:
            break

print "#" * 10
print "Shuting down ...now !!!"

# Bye-Bye
srvr.close()

os.remove(PATH)
