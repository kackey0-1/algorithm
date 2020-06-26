import socket # https://linuxjm.osdn.jp/html/LDP_man-pages/man2/socket.2.html
import utils

"""
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # SOCK_STREAM
    # 順序性と信頼性があり、双方向の、接続された バイトストリーム (byte stream) を提供する。
    # 帯域外 (out-of-band) データ転送メカニズムもサポートされる。
    s.connect(('127.0.0.1', 50007))
    # 日本語文字列
    s.sendall(utils.convert_e('あいうえお'))
    data = s.recv(1024)
    print(repr(utils.convert_d(data)))
"""

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    # s.sendto(b'Hello UDP', ('127.0.0.1', 50008))
    data = 'あいうえお'
    s.sendto(b'Hello UDP', ('127.0.0.1', 50008))
