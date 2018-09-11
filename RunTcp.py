import socket
import time
import threading


class RunTcp():

    def __init__(self):
        self.tcpClientSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.tcpClientSock.settimeout(30)
        self.data = bytearray([0, 0])

    def connect(self):
        addr =(self.host,self.port)
        self.tcpClientSock.connect(addr)


    def run(self):
        try:
            bufszie = 1024
            self.tmpdata = []
            strl = ''
            totalrecv = 0
            self.tcpClientSock.send(self.data)
            #print(data)
            time.sleep(0.2)
            self.tmpdata = self.tcpClientSock.recv(bufszie)
            print(self.tmpdata)
        except Exception as err:
            print(err)

    def stop(self):
        time.sleep(1)
        self.tcpClientSock.close()





