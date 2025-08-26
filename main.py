import socket
import asyncio
import concurrent.futures

 

def port_scanner(host:str,port: int) -> bool:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(timeout = 0.5)
    return s.connect_ex((host,port)) == 0


port_num = [80,443,22]




