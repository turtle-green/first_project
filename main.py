"""
File name : main.py
Description : Main file to execute serial interface
Author : Luis
"""

from utils import readPort, writePort


# main function
def main() -> None : 
    writePort('holi')
    print(readPort())


# this file is the main function
if __name__ == '__main__' : 
    main()
