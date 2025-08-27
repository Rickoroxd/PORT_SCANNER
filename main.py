import socket



def port_scanner(host : str,port : int) -> bool:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect_ex((host,port))
        print(f'{host} : OPENED')
        s.close()
    except:
        print('f{host} : CLOSED')


