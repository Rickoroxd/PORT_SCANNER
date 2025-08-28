import socket

def port_scanner(host : str,port : int) -> bool:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        if(s.connect_ex((host,port)) == 0):
            print(f'HOST : {host} PORT : {port} is OPENED')
        else :
             print(f'HOST : {host} PORT : {port} is CLOSED')
        s.close() 
    except KeyboardInterrupt:
        print("Something Wrong with Input")


port = [22,23,80,443]
host = "scanme.nmap.org"

for i in port:
    port_scanner(host,i)


