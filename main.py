import socket



def port_scanner(host : str,pott : int) -> bool:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    try:

