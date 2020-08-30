"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from collections import defaultdict

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

records = defaultdict(int)
for item in calls:
    records[item[0]] += int(item[3])
    records[item[1]] += int(item[3])

duration = 0
number = ""

for key, value in records.items():
    if value > duration:
        duration = value
        number = key

print(f"{number} spent the longest time, {duration} seconds, on the phone during September 2016.")
