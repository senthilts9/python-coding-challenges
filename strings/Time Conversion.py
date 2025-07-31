#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hh, mm, ss_period = s[:-2].split(":")  # Extract hours, minutes, and seconds
    period = s[-2:]  # Get AM or PM
    hh = int(hh)  # Convert hour to integer

    # Convert 12-hour format to 24-hour format
    if period == "AM":
        hh = 0 if hh == 12 else hh  # Convert 12 AM to 00
    else:
        hh = hh if hh == 12 else hh + 12  # Convert PM hours except 12 PM

    # Format the result as HH:MM:SS and return
    return "{:02}:{:02}:{:02}".format(hh, int(mm), int(ss_period))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
