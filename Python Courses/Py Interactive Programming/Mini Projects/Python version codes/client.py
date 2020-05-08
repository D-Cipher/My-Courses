import sys
import socket
import select

def client():
        if(len(sys.argv) < 3):
            print('Usage : python chat_client.py hostname port')
            sys.exit()

        #Get users input
        host = sys.argv[1]
        port = int(sys.argv[2])


        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Set socket timeout
        s.settimeout(2)

        #connect to host
        try:
            s.connect((host, port))
        except:
            print('Unable to connect')
            sys.exit()

        print("Connected to remote host. You can start sending messages")
        sys.stdout.write('[Me] '); sys.stdout.flush()

        while 1:
            socket_list = [sys.stdin, s]

            #Get the list of readable sockets
            ready_to_read,ready_to_write, in_error = select.select(socket_list, [], [], 0)

            for sock in ready_to_read:
                if sock == s:
                    #Message from server
                    data = sock.recv(4096)
                    if not data:
                        print('\nDisconnected from chat server')
                        sys.exit()
                    else:
                        sys.stdout.write(data)
                        sys.stdout.write('[Me] '); sys.stdout.flush()

                else:
                    #User has entered a message
                    mes = sys.stdin.readline()
                    s.send(mes)
                    sys.stdout.write('[Me] '); sys.stdout.flush()

if __name__ == "__main__":
    sys.exit(client())
