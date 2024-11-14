# Readtemp

Readtemp is a temperature reading program.
This is an exercise for me to learn Python. And be familiar with Visual Studio Code.

Readtemp reads the current temperature value from a temperature sensor connected to a Raspberry Pi. The temperature sensor is a 1-Wire DS18B20 and connects to GPIO pin 4.

## Function

There are three main programs:
- **Terminal.py**, The main program that stores a temperature value every hour (when the minute is 0). Will run as a service.
- **GetMomentanValue.py** reads the current temperature value.
- **PrintSampledData** prints the desired count of stored values to the console. Default is 24.

The values are stored in a sqlite database in the same location as the executables. The database file name is 'readtemp.db'.
