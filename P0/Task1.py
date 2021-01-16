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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
phonelist = set()
for text, call in zip(texts, calls):
    phonelist = phonelist.union(text[:2])
    phonelist = phonelist.union(call[:2])
print(f"There are {len(phonelist)} different telephone numbers in the records.")

"""
Answer: There are 570 different telephone numbers in the records.
Runtime: O(n)
"""