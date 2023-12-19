import pathlib
import os

for path in pathlib.Path("input").iterdir():
    if path.is_file():
        current_file = open(path, "rb").read()
        # everytime it finds this binary pattern it will split the file
        x = current_file.split(b'\x12\x91\x29\x10')
        i = 1
        while i < len(x):
            print(i)
            print (os.path.basename(path))
            f = open((str(i) + str(os.path.basename(path))), "wb")
            f.write((x)[i])
            i += 1
            f.close
            

        

