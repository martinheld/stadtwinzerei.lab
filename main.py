import random
import datetime
import sched, time
import config

from gsheet_reporter import GSheetReporter
from bme280 import readBME280All
from co2reader import read_ppm

g = GSheetReporter(config.app['jsonFile'], config.app['sheetId'])
s = sched.scheduler(time.time, time.sleep)

def poll_sensors():
    timestamp = datetime.datetime.now().replace(microsecond=0).isoformat()    
#    temperature, pressure, humidity = readBME280All()
    return [timestamp, read_ppm()]

def report_data(sc): 
    sensor_data = poll_sensors()
    print(sensor_data[0], "Reporting Measurements", sensor_data)
#    g.insert("measurements", sensor_data, 2)
    
    s.enter(config.app['pollingDelay'], 1, report_data, (sc,))

s.enter(0, 1, report_data, (s,))
s.run()