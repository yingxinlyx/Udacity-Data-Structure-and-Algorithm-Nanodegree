"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

records = set()
for rec in texts:
    records.add(rec[0])
    records.add(rec[1])
    
for rec in calls:
    records.add(rec[0])
    records.add(rec[1])

print("There are " + str(len(records)) + " different telephone numbers in the records.")