
import time
import datetime
import random
from time import sleep


def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

for i in range(1,10):
    sleep(1)
    line=random_line(r'C:\VIVEK\PROJECTS\DATA\trailer-A.json')
    string,key,TS = line.partition("\"timestamp\": ")
    '''
    print(str)
    print(key)
    print (TS[:13])
    print(TS[14:])
    '''

    pattern = '%d.%m.%Y %H:%M:%S'
    date_time = datetime.datetime.fromtimestamp(time.time()).strftime(pattern )
    epoch = int(time.mktime(time.strptime(date_time, pattern)) * 1000)

    print(string + key + str(epoch) + TS[14:])
    print(line)



