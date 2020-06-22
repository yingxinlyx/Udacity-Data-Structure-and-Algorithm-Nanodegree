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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

text_out = set()
text_in = set()
for rec in texts:
    text_out.add(rec[0])
    text_in.add(rec[1])
    
call_out = set()
call_in = set()
for rec in calls:
    call_out.add(rec[0])
    call_in.add(rec[1])

res = call_out - call_in - text_out - text_in

print('These numbers could be telemarketers: ')

for item in sorted(res):
    print(item)
