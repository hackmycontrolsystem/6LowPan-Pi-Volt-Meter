#!/usr/bin/python3

import socket
import time


ADDR = 'fd28:e5e1:86:0:e40c:932d:df85:4be9' # the other RPi
PORT = 2016

def main():
    # scope_id = socket.if_nametoindex('lowpan0')
    while True:
        s6 = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
        s6.connect((ADDR, PORT, 0, 0))
        data = s6.recv(1024)
        print(data.decode('utf-8'), end='')

        # get it again after 10 seconds
        time.sleep(10)

if __name__ == '__main__':
    main()
