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

outgoingcalls = set()
others = set()
for call, text in zip(calls, texts):
    outgoingcalls.add(call[0])
    others.add(call[1])
    others = others.union(text[:2])

telemarketers = outgoingcalls - others
print("These numbers could be telemarketers: ")
for t in sorted(telemarketers):
    print(t)

"""
Runtime: O(n)
"""