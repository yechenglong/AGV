from RunTcp import *
from sendModel import *


runtcp=RunTcp()
runtcp.host = '127.0.0.1'
runtcp.port = 31555
runtcp.connect()

agv_handshake_11=sendModel()
agv_handshake_11.vern='0,0,-6,-86'
agv_handshake_11.mslg='0,0,0,104'
agv_handshake_11.errc='0,0,0,0'
agv_handshake_11.timp='0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'
agv_handshake_11.msid='0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'
agv_handshake_11.hcs='12'
agv_handshake_11.dvtp='0,1'
agv_handshake_11.dvlg='5'
agv_handshake_11.dvid='10003'
agv_handshake_11.msgtp='7,209'
agv_handshake_11.token='0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'
agv_handshake_11.dcs='208'

runtcp.data = agv_handshake_11.getSendMsg()
res = runtcp.run()
token = ",".join(res.split(',')[72:104])
print(token)

agv_handshake_12=sendModel()
agv_handshake_12.vern='0,0,-6,-86'
agv_handshake_12.mslg='0,0,0,104'
agv_handshake_12.errc='0,0,0,0'
agv_handshake_12.timp='0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'
agv_handshake_12.msid='0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'
agv_handshake_12.hcs='12'
agv_handshake_12.dvtp='0,1'
agv_handshake_12.dvlg='5'
agv_handshake_12.dvid='10003'
agv_handshake_12.msgtp='11,185'
agv_handshake_12.token=token
agv_handshake_12.arriveaddr='1002'
agv_handshake_12.dcs='208'

runtcp.data = agv_handshake_12.getSendMsg()
runtcp.run()
time.sleep(2)
agv_handshake_13=sendModel()
agv_handshake_13.vern='0,0,-6,-86'
agv_handshake_13.mslg='0,0,0,104'
agv_handshake_13.errc='0,0,0,0'
agv_handshake_13.timp='0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'
agv_handshake_13.msid='0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'
agv_handshake_13.hcs='12'
agv_handshake_13.dvtp='0,1'
agv_handshake_13.dvlg='5'
agv_handshake_13.dvid='10003'
agv_handshake_13.msgtp='11,185'
agv_handshake_13.token=token
agv_handshake_13.arriveaddr='1003'
agv_handshake_13.dcs='208'
runtcp.data = agv_handshake_13.getSendMsg()
runtcp.run()