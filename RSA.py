'''
常规RSA题：已知p、q、e、的情况下求解明文
'''
import libnum
from Crypto.Util.number import long_to_bytes

def Normal(p, q, e, c):
    p = int(p, 16)
    q = int(q, 16)
    e = int(e, 16)
    c = int(c, 16)

    n = p * q
    d = libnum.invmod(e, (p - 1) * (q - 1)) X
    m = pow(c, d, n)    #解密密文

    print(long_to_bytes(m).decode())
