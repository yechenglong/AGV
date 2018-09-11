from sendModel import *



agv_handshake_11=sendModel()
agv_handshake_11.vern='0,0,-6,-86'
agv_handshake_11.mslg='0,0,0,104'
agv_handshake_11.errc='0,0,0,0'
agv_handshake_11.timp='0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'
agv_handshake_11.msid='0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'
agv_handshake_11.hcs='12'
agv_handshake_11.dvtp='0,1'
agv_handshake_11.dvlg='5'
agv_handshake_11.dvid='49,48,48,48,49'
agv_handshake_11.msgtp='7,-47'
agv_handshake_11.token='0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'
agv_handshake_11.dcs='208'

print(agv_handshake_11.getdata())

# + ',' + agv_handshake_11.hcs + ',' + agv_handshake_11.dvtp + ',' + agv_handshake_11.dvlg \
#        + ',' + agv_handshake_11.dvid + ',' + agv_handshake_11.msgtp + ',' + agv_handshake_11.token + ',' + agv_handshake_11.dcs
# data = bytearray(eval(
#     '[' + agv_handshake_11.vern + ',' + agv_handshake_11.mslg + ',' + agv_handshake_11.errc + ',' + agv_handshake_11.timp + ',' + agv_handshake_11.msid + ',' + agv_handshake_11.hcs + ',' + agv_handshake_11.dvtp + ',' + agv_handshake_11.dvlg + ',' + agv_handshake_11.dvid + ',' + agv_handshake_11.msgtp + ',' + agv_handshake_11.token + ',' + agv_handshake_11.dcs + ']'))
# MLSG = len(data)
# agv_handshake_11.mslg='0,0,0,'+str(MLSG)
# print(agv_handshake_11.mslg)
# data = bytearray(eval(
#     '[' + agv_handshake_11.vern + ',' + agv_handshake_11.mslg + ',' + agv_handshake_11.errc + ',' + agv_handshake_11.timp + ',' + agv_handshake_11.msid + ',' + agv_handshake_11.hcs + ',' + agv_handshake_11.dvtp + ',' + agv_handshake_11.dvlg + ',' + agv_handshake_11.dvid + ',' + agv_handshake_11.msgtp + ',' + agv_handshake_11.token + ',' + agv_handshake_11.dcs + ']'))
