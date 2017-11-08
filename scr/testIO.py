import time


def readFile(path):
    f = open(path, mode='r')
    return f

def writeFile(path):
    #f = open(path,mode='w')
    f = open(path, mode='a')
    return

def getFile(path,mode):
    return open(path,mode=mode)

filePath=r'C:\VIVEK\test2.txt'

#f2 = writeFile(r'C:\VIVEK\test1.txt')
#f2.write(time.strftime('%d/%m/%Y_%H%M%S')+'\n')
#f2.close()

#f1 = readFile(r'C:\VIVEK\test1.txt')
#print(f1.read())

getFile(filePath,'a').write(time.strftime('%d/%m/%Y_%H%M%S')+'\n')
print(getFile(filePath,'r').read())


