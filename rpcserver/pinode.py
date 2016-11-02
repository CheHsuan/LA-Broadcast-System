import SimpleXMLRPCServer
import os
import socket
import fcntl 
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    return socket.inet_ntoa(fcntl.ioctl( 
        s.fileno(), 0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15]))[20:24])

def echo(sMsg):
    return sMsg

def play(music):
    os.system("omx_api --play ~/Music/" + music)
    return "success"

def pause():
    os.system("omx_api --pause")
    return "success"

def stop():
    os.system("omx_api --stop")
    return "success"
 
def main():
    server = SimpleXMLRPCServer.SimpleXMLRPCServer((get_ip_address('eth0'), 8080),  allow_none=True)
    server.register_function(echo)
    server.register_function(play)
    server.register_function(pause)
    server.register_function(stop)
    server.serve_forever()
 
if __name__ == "__main__":
    main()
