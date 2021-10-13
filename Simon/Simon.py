import simon
import binascii
import sys

mess='hello'


k='0x1918111009080100'

def getBinary(word):
    return int(binascii.hexlify(word), 16)

if (len(sys.argv)>1):
	mess=str(sys.argv[1])
	m=getBinary(mess)

if (len(sys.argv)>2):
	k=str(sys.argv[2])

key=int(k,16)

print ("Message:\t",mess)
print ("Key:\t\t",k)

ksize=(len(k)-2)*4

bsize=32
if (ksize==72): bsize=48
if (ksize==96): bsize=48
if (ksize==128): bsize=64

print ("Key size:\t",ksize)
print ("Block size:\t",bsize)

w = simon.SimonCipher(key, key_size=ksize, block_size=bsize)

t = w.encrypt(int.from_bytes(mess.encode(), byteorder='big'))

print ("Encrypted:\t",hex(t))

res = w.decrypt(t)

hexstr= hex(res)
print ("Decrypt:\t",hexstr)

res_str=bytes.fromhex(hexstr[2:]).decode('utf-8')
print ("Decrypt:\t",res_str)