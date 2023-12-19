import os
import struct
from shutil import copyfile

basedir = "./input"
movdir = "./output"

def readUShort(file):
    return struct.unpack("H", file.read(2))[0]


def readUInt(file):
    return struct.unpack("I", file.read(4))[0]


def main():
    pointers = []
    for root, dirs, files in os.walk(basedir):
        for fileName in files:
            file = open((basedir+"\\"+fileName), 'rb')
            file.seek(40)
            Ptr = readUInt(file)
            file.seek(Ptr)
            test = readUInt(file)
            i = 1
            inc = 0
            if test == 0:
                inc = 4
            while i != 0:
                file.seek(Ptr + inc)
                value = readUInt(file)
                if value == 0:
                    i = 0
                else:
                    inc += 4
                    pointers.append(value)
            incr = 20
            nextfile = 0
            for ptr in pointers:
                end = 0
                print("Parsing values at pointer: "+ str(ptr))
                while end != 3212836864:
                    file.seek(ptr + incr)
                    check = readUShort(file)
                    print("Parsed value: " +str(check))
                    if 0 < check < 3 or check > 4:
                        print(fileName)
                        copyfile((basedir+"\\"+fileName), (movdir+"\\"+fileName))
                        nextfile = 1
                        break
                    else:
                        file.seek(ptr + incr + 4)
                        end = readUInt(file)
                        print("testing if ended: "+str(end))
                        incr += 24
                incr = 20
                if nextfile == 1:
                    break
main()