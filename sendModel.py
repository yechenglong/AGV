# -*- coding:utf-8 -*-
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
class sendModel():
    def __init__(self):
        self.vern = ''
        self.mslg = ''
        self.errc = ''
        self.timp = ''
        self.msid = ''
        self.hcs = ''
        self.dvtp = ''
        self.dvlg = ''
        self.dvid = ''
        self.msgtp = ''
        self.token = ''
        self.arriveaddr = ''
        self.dcs = ''

    def getmslg(self):
        if self.arriveaddr =='':
            self.dvid = self.toAscii(self.dvid)
            data = (self.vern + ',' + self.mslg + ',' + self.errc + ',' + self.timp + ',' + self.msid + ',' + self.hcs + ',' \
                   + self.dvtp + ',' + self.dvlg + ',' + self.dvid + ',' + self.msgtp + ',' + self.token + ',' + self.dcs).split(',')
        else:
            self.arriveaddr = self.toAscii(self.arriveaddr)
            self.dvid = self.toAscii(self.dvid)
            data = (self.vern + ',' + self.mslg + ',' + self.errc + ',' + self.timp + ',' + self.msid + ',' + self.hcs + ',' \
                   + self.dvtp + ',' + self.dvlg + ',' + self.dvid + ',' + self.msgtp + ',' + self.token + ',' + self.arriveaddr + ',' +self.dcs).split(',')
        self.mslg = '0,0,0,'+str(len(data))
        logging.debug("mslg::"+str(self.mslg))

    def gethcs(self):
        headdata = (self.vern + ',' + self.mslg + ',' + self.errc + ',' + self.timp + ',' + self.msid).split(',')
        logging.debug(headdata)
        hcs = 0
        for i in headdata:
            hcs += int(i)
            if hcs > 256:
                hcs = hcs - 256
        self.hcs = str(hcs)
        logging.debug("hcs:  "+ str(self.hcs))

    def getdcs(self):
        if self.arriveaddr == '':
            bodydata = (self.dvtp + ',' + self.dvlg + ',' + self.dvid + ',' + self.msgtp + ',' + self.token).split(',')
        else:
            bodydata = (self.dvtp + ',' + self.dvlg + ',' + self.dvid + ',' + self.msgtp + ',' + self.token + ',' + self.arriveaddr).split(',')
        dcs = 0
        for i in bodydata:
            dcs += int(i)
            if dcs > 256:
                dcs = dcs - 256
        self.dcs = str(dcs)
        logging.debug("dcs:  "+ str(self.dcs))

    def getdata(self):
        self.getmslg()
        self.gethcs()
        self.getdcs()
        if self.arriveaddr =='':
            data = (self.vern + ',' + self.mslg + ',' + self.errc + ',' + self.timp + ',' + self.msid + ',' + self.hcs + ',' \
                   + self.dvtp + ',' + self.dvlg + ',' + self.dvid + ',' + self.msgtp + ',' + self.token + ',' + self.dcs).split(',')
        else:
            data = (self.vern + ',' + self.mslg + ',' + self.errc + ',' + self.timp + ',' + self.msid + ',' + self.hcs + ',' \
                   + self.dvtp + ',' + self.dvlg + ',' + self.dvid + ',' + self.msgtp + ',' + self.token + ',' + self.arriveaddr + ',' +self.dcs).split(',')
        for i in range(len(data)):
            if int(data[i]) < 0:
                j = str(int(data[i]) + 256)
                data[i] = j
        data = ",".join(data)
        logging.debug(data)
        return data

    def toAscii(self,tmpval):
        tmpStr = ''
        asciiList = map(ord, tmpval)
        for tmp in asciiList:
            tmpStr = tmpStr + ',' + str(tmp)
        asciiCode = tmpStr[1:len(tmpStr)]
        return asciiCode

    def getSendMsg(self):
        data = self.getdata()
        logging.debug(
            'send:' + data)
        data = bytearray(eval(
            '[' + data + ']'))
        logging.debug(data)
        return data




