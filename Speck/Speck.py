# import timeit

# mysetup = "from speck import SpeckCipher, speck"
from speck import SpeckCipher, speck

# mycode = '''

import binascii
import sys

mess='TelkomUniversity'

k='0x4109010405c0f53e4eeeb48d9c188f43'

def getBinary(word):
    return int(binascii.hexlify(word), 16)

if (len(sys.argv)>1):
	mess=str(sys.argv[1])
	m=getBinary(mess)

if (len(sys.argv)>2):
	k=str(sys.argv[2])

key=int(k,16)

print ("Message \t\t\t:\t",mess)
print ("Key\t\t\t\t\t:\t",k)

ksize=(len(k)-2)*4
bsize=128
# if (ksize==72): bsize=48
# if (ksize==96): bsize=48
# if (ksize==128): bsize=64
print ("Key size \t\t\t:\t",ksize)
print ("Block size\t\t\t:\t",bsize)

w = speck.SpeckCipher(key, key_size=ksize, block_size=bsize)
t = w.encrypt(int.from_bytes(mess.encode(), byteorder='big'))
print ("Encrypted\t\t\t:\t",hex(t))

scale = 16
res = bin(int(hex(t), scale)).zfill(8)
print ("Encrypted binary\t:\t", str(res))

res = w.decrypt(t)
hexstr= hex(res)
res_str=bytes.fromhex(hexstr[2:]).decode('utf-8')
print ("Decrypted\t\t\t:\t",res_str)
print ("Decrypted\t\t\t:\t",hexstr)

rest = bin(int(hexstr, scale)).zfill(8)
print ("Decrypted binary\t:\t", str(rest))
# '''

# print("Time:\t",timeit.timeit(setup = mysetup,
# 	  						  stmt= mycode,
# 							  number = 10))