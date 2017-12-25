import requests
import time
import datetime
import random
from time import sleep

TIMESTAMP=time.strftime("%Y%m%d%H%M%S")

pattern = '%d.%m.%Y %H:%M:%S'

'''pick a randome line from file'''
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

def getItFromFile(recordCount,tempratureMax):
    for i in range(1, recordCount):
        sleep(1)
        line = random_line(r'C:\VIVEK\PROJECTS\DATA\trailer-NEW.json')

        '''calculate the new temprature '''
        string, key, TS = line.partition("\"values\": ")
        temprature=random.randint(1,tempratureMax)

        '''replace timestamp from line with current one'''
        string, key, TS = line.partition("\"timestamp\": ")
        date_time = datetime.datetime.fromtimestamp(time.time()).strftime(pattern)
        epoch = int(time.mktime(time.strptime(date_time, pattern)) * 1000)
        '''new line with latest timestamp'''
        content = """{"sensorType": "TEMPERATURE", "valueLength": 1, "values": [%s], "timestamp": %s, "sensorLocation": "trailer"}""" % (temprature, epoch)
        print(content)
        fileName=r'C:\VIVEK\PROJECTS\DATA\trailer-Calculted_' + TIMESTAMP + '.json'
        file=open(fileName,'a')
        file.write(content)

def getItFromFileNew(recordCount,tempratureMax):
    fileName = r'C:\VIVEK\PROJECTS\DATA\trailer-Calculted_' + TIMESTAMP + '.json'
    file = open(fileName, 'a')
    for i in range(1, recordCount):
        sleep(1)
        line = random_line(r'C:\VIVEK\PROJECTS\DATA\trailer-NEW.json')

        '''calculate the new temprature '''
        string, key, TS = line.partition("\"values\": ")
        temprature=random.randint(1,tempratureMax)

        '''replace timestamp from line with current one'''
        string, key, TS = line.partition("\"timestamp\": ")
        date_time = datetime.datetime.fromtimestamp(time.time()).strftime(pattern)
        epoch = int(time.mktime(time.strptime(date_time, pattern)) * 1000)
        '''new line with latest timestamp'''
        content = """{"sensorType": "TEMPERATURE", "valueLength": 1, "values": [%s], "timestamp": %s, "sensorLocation": "trailer"}\n""" % (temprature, epoch)
        file.write(content)
        content = """{"sensorType": "VIRABRATIONS", "valueLength": 1, "values": [%s], "timestamp": %s, "sensorLocation": "trailer"}\n""" % ((temprature % 5), epoch)
        file.write(content)
    file.close()


def main():
    getItFromFileNew(10,20)


if __name__ == '__main__':
    main()