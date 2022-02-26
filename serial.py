"""
File name : serial.py
Description : code for serial communication (UART)
Author : Luis
"""

from typing import Any
import serial

#
def readPort() -> Any: 
    
    with serial.Serial('/dev/ttys3', 19200, timeout = 10) as ser:
        #x = ser.read()          # read one byte
        s = ser.read(10)        # read up to ten bytes (timeout)
        #line = ser.readline()   # read a '\n' terminated line
        return s

    return Any

#
def writePort(message : str) -> None : 
    ser = serial.Serial('/dev/ttys3')  # open serial port
    print('Port name : %s' % ser.name)         # check which port was really used
    ser.write(bytes(message, 'utf-8'))     # write a string message
    ser.close()             # close port



# util function to read data from command
def readData() -> str :
    readVar = input()
    return readVar

# util function to print data
def printData(data : str) -> None :
    print('\n %s \n' % data)