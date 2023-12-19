import os
import shutil
import struct

def readUShort(file):
    return struct.unpack("H",file.read(2))[0]

basedir = r"output"
movdir = r"input"

log = ""
logFile = open('5-log.txt', 'w')

# Walk through all files in the directory that contains the files to copy
for root, dirs, files in os.walk(movdir):
    for dirName in dirs:
        for fileName in files:
            if fileName[0:4] == "0005":
                file = open((((os.path.abspath(root), fileName)[0])+ "\\" +fileName), "rb")
                i = readUShort(file)
                print(i)
                path = os.path.abspath(root)
                length = len(path)
                if i == 8:
                    if length >= 100:
                        file.seek(2)
                        short = readUShort(file)
                        print(short)
                        # I use absolute path, case you want to move several dirs.
                        old_name = os.path.abspath(root)

                        # Separate base from extension
                        base, extension = os.path.splitext(fileName)

                        # Initial new name
                        new_name = os.path.join(basedir, str(short), os.path.basename(path))
                        
                        # If folder basedir/base does not exist
                        if not os.path.exists(new_name):
                            print("File didn't exist")
                            log = "File didn't exist \n"
                            shutil.copytree(old_name, new_name)
                            print ("Copied", old_name, "as", new_name)
                            log = log + "Copied " + str(old_name) + " as " + str(new_name) + "\n \n" 
                            continue 
                        else:
                            print("File Exists")
                            log = log + "File already exists" + "\n"
                            ii = 1
                            while True:
                                new_name = os.path.join(basedir, str(short), os.path.basename(path) + "_" + str(ii))
                                if not os.path.exists(new_name):
                                    shutil.copytree(old_name, new_name)
                                    print ("Copied", old_name, "as", new_name)
                                    log = log + "Copied " + str(old_name) + " as " + str(new_name) + "\n \n"
                                    break 
                                else:
                                    ii += 1
            logFile.write(log)
logFile.close()