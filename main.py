import random
import datetime
import sched, time
import config

from gsheet_reporter import GSheetReporter

g = GSheetReporter(config.app['jsonFile'], config.app['sheetId'])
s = sched.scheduler(time.time, time.sleep)

def poll_sensors():
    timestamp = datetime.datetime.now().replace(microsecond=0).isoformat()    
    return [timestamp, random.randint(5,30), random.randint(20,100), random.randint(100,1000)]

def report_data(sc): 
    sensor_data = poll_sensors()
    print(sensor_data[0], "Reporting Measurements", sensor_data)
    g.insert("measurements", sensor_data, 2)
    
    s.enter(config.app['pollingDelay'], 1, report_data, (sc,))

s.enter(0, 1, report_data, (s,))
s.run()