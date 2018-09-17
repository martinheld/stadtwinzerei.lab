import time
import Adafruit_ADS1x15
import math

# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1

MAX_VOLTS=4.096
MAX_VAL = 32767

RAW_VALUE_400ppm = 22000 # readout at 400 ppm (assumed atmospheric co2)
RAW_VALUE_10000ppm = 12800 # max measure range

VOLTS_400ppm = RAW_VALUE_400ppm * MAX_VOLTS / MAX_VAL
VOLTS_10000ppm = RAW_VALUE_10000ppm * MAX_VOLTS / MAX_VAL

# (LOG_1000_VOLTAGE - LOG_400_VOLTAGE) / (LOG_1000 - LOG_400);
CO2_LOG_SLOPE = (math.log10(VOLTS_10000ppm) - math.log10(VOLTS_400ppm)) / (math.log10(10000) - math.log10(400))
V400 = math.log10(VOLTS_400ppm) - CO2_LOG_SLOPE * math.log10(400)

def convert_to_ppm(raw_value):
    log_volts = math.log10(raw_value * MAX_VOLTS / MAX_VAL)
    return math.pow(10, (log_volts - V400) / CO2_LOG_SLOPE)

def read_ppm():
    return convert_to_ppm(adc.read_adc(0, gain=GAIN))
