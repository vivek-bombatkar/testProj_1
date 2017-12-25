import requests
import time
import datetime
import random
from time import sleep

pattern = '%d.%m.%Y %H:%M:%S'

'''pick a randome line from file'''
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

def getItFromFile(recordCount):
    for i in range(1, recordCount):
        sleep(1)
        line = random_line(r'C:\VIVEK\PROJECTS\DATA\trailer-A.json')
        '''find and replace timestamp from line with current one'''
        string, key, TS = line.partition("\"timestamp\": ")
        date_time = datetime.datetime.fromtimestamp(time.time()).strftime(pattern)
        epoch = int(time.mktime(time.strptime(date_time, pattern)) * 1000)
        '''new line with latest timestamp'''
        content=string + key + str(epoch) + TS[13:]
    #    print(line)
        print(content)
    #    requests.post("http://127.0.0.1:8080", json=content)

def getOnlyTemprature(recordCount,tempratureMax):
    #{"sensorType": "TEMPERATURE", "valueLength": 2, "values": [22.75, 19.09375], "timestamp": 1512052877529, "sensorLocation": "trailer"}
    for i in range(1,recordCount):
        sleep(1)
        date_time = datetime.datetime.fromtimestamp(time.time()).strftime(pattern)
        epoch = int(time.mktime(time.strptime(date_time, pattern)) * 1000)

        temprature = random.randint(1,tempratureMax)
        content = """{"sensorType": "TEMPERATURE", "valueLength": 1, "values": [%s], "timestamp": %s, "sensorLocation": "trailer"}"""%(temprature,epoch)
        print(content)


def main():
    getOnlyTemprature(10,20)
    getOnlyTemprature(10,50)



if __name__ == '__main__':
    main()


