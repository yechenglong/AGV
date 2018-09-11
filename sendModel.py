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
            data = self.vern + ',' + self.mslg + ',' + self.errc + ',' + self.timp + ',' + self.msid + ',' + self.hcs + ',' \
                   + self.dvtp + ',' + self.dvlg + ',' + self.dvid + ',' + self.msgtp + ',' + self.token + ',' + self.dcs
        else:
            data = self.vern + ',' + self.mslg + ',' + self.errc + ',' + self.timp + ',' + self.msid + ',' + self.hcs + ',' \
                   + self.dvtp + ',' + self.dvlg + ',' + self.dvid + ',' + self.msgtp + ',' + self.token + ',' + self.arriveaddr + ',' +self.dcs
        self.mslg = '0,0,0,'+str(len(data))

    def gethcs(self):
        headdata = (self.vern + ',' + self.mslg + ',' + self.errc + ',' + self.timp + ',' + self.msid).split(',')
        hcs = 0
        for i in headdata:
            hcs += int(i)
            if dcs > 256:
                dcs = dcs - 256
        self.hcs = str(hcs)
        logging.debug(self.hcs)

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
        logging.debug(self.dcs)

    def getdata(self):
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

    def getSendMsg(self, ac):
        if self.arriveaddr == '':
            logging.debug(
                'send:' + ac.vern + ',' + ac.mslg + ',' + ac.errc + ',' + ac.timp + ',' + ac.msid + ',' + ac.hcs + ',' + ac.dvtp + ',' + ac.dvlg + ',' + ac.dvid + ',' + ac.msgtp + ',' + ac.token + ',' + ac.arriveaddr + ',' + ac.dcs)
            data = bytearray(eval(
                '[' + ac.vern + ',' + ac.mslg + ',' + ac.errc + ',' + ac.timp + ',' + ac.msid + ',' + ac.hcs + ',' + ac.dvtp + ',' + ac.dvlg + ',' + ac.dvid + ',' + ac.msgtp + ',' + ac.token + ',' + ac.arriveaddr + ',' + ac.dcs + ']'))
        else:
            logging.debug(
                'send:' + ac.vern + ',' + ac.mslg + ',' + ac.errc + ',' + ac.timp + ',' + ac.msid + ',' + ac.hcs + ',' + ac.dvtp + ',' + ac.dvlg + ',' + ac.dvid + ',' + ac.msgtp + ',' + ac.token + ',' + ac.dcs)
            data = bytearray(eval(
                '[' + ac.vern + ',' + ac.mslg + ',' + ac.errc + ',' + ac.timp + ',' + ac.msid + ',' + ac.hcs + ',' + ac.dvtp + ',' + ac.dvlg + ',' + ac.dvid + ',' + ac.msgtp + ',' + ac.token + ','  + ac.dcs + ']'))
        return data

    def getSendMsgtm(self,ac):
        message = self.toAscii(ac.jsonattr)
        data = bytearray(eval('['+message+']'))
        return data

    def run(self, ac):
        dcstmp = bytearray(eval(
            '[' + ac.dvtp + ',' + ac.dvlg + ',' + ac.dvid + ',' + ac.msgtp + ',' + ac.token + ',' + ac.arriveaddr + ']'))
        dcsint = 0
        for i in range(len(dcstmp)):
            dcsint = dcsint + dcstmp[i]
        print(str(dcsint) + " " + str(dcsint % 256))
        ac.dcs = str(dcsint % 256)
        return True


