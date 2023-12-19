import os
img_paths = []
for root, directory, files in os.walk("C:\\images"):
    for file in files:
        if '.png' in file:
            img_paths.append(root+'/'+file)

inp = os.path.getsize("C:\\input.png")
for file in img_paths:
    compare = os.path.getsize(file)
    if inp == compare:
        print(file)