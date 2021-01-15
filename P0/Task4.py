"""
Read file into texts and calls.
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

outgoingcalls = []
others = []
for call in calls:
    outgoingcalls.append(call[0])
    others.append(call[1])

for text in texts:
    others += text[:2]

telemarketers = list(set(outgoingcalls) - set(others))
telemarketers.sort()
print("These numbers could be telemarketers: ")
for t in telemarketers:
    print(t)

"""
Runtime: O(n)
"""