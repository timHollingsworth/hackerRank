"""
Given a time in -hour AM/PM format, convert it to military (-hour) time.
"""
#!/bin/python3

import sys


time = input().strip()
hour = time[0:2]
minute = time[3:5]
second = time[6:8]
amPM = time[8:10]

if hour == '12' and amPM == 'AM':
    hour = '00'
elif amPM == 'PM' and hour != '12':
    hour = int(hour) + 12
print(str(hour) + ':' + str(minute) + ':' + str(second))