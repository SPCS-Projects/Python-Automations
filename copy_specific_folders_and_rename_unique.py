import os
import shutil

basedir = r"output"
movdir = r"input"
# Walk through all files in the directory that contains the files to copy

log = ""
logFile = open('32-log.txt', 'w')

for root, dirs, files in os.walk(movdir):
    for dirName in dirs:
        if dirName[0:4] == "0032":
            # I use absolute path, case you want to move several dirs.
            old_name = os.path.join( os.path.abspath(root), dirName )
            # Initial new name
            new_name = os.path.join(basedir, dirName)
            # If folder basedir/base does not exist... You don't want to create it?
            if not os.path.exists(new_name):
                print ("File didn't exist")
                log = "File didn't exist \n"
                shutil.copytree(old_name, new_name)
                print ("Copied", old_name, "as", new_name)
                log = log + "Copied " + str(old_name) + " as " + str(new_name) + "\n \n" 
                continue    # Next filename
            else:
                print("File already exists")
                log = log + "File already exists" + "\n"
                ii = 1
                while True:
                    new_name = os.path.join(basedir,dirName + "_" + str(ii))
                    if not os.path.exists(new_name):
                        shutil.copytree(old_name, new_name)
                        print ("Copied", old_name, "as", new_name)
                        log = log + "Copied " + str(old_name) + " as " + str(new_name) + "\n \n"
                        break 
                    else:
                        ii += 1
            logFile.write(log)
logFile.close()

