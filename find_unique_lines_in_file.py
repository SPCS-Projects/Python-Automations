with open(r'check.txt','r') as masterdata:
    with open(r'compare.txt','r') as useddata:
        with open(r'unique.txt','w+') as Newdata:

            usedfile = [ x.strip('\n') for x in list(useddata) ] #1
            masterfile = [ x.strip('\n') for x in list(masterdata) ] #2

            for line in masterfile: #3
                if line not in usedfile: #4
                    Newdata.write(line + '\n') #5