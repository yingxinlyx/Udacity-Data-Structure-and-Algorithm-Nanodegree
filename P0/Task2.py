"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
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

d = {}
for rec in calls:
    if rec[0] in d:
        d[rec[0]] += int(rec[3])
    else:
        d[rec[0]] = int(rec[3])
    if rec[1] in d:
        d[rec[1]] += int(rec[3])
    else:
        d[rec[1]] = int(rec[3])


res = sorted(d.items(), key = lambda x: x[1], reverse = True)
print("%s spent the longest time, %s seconds, on the phone during September 2016." % (res[0]))