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
phonelist = []
for text in texts:
    phonelist += text[:2]
for call in calls:
    phonelist += call[:2]
n = len(set(phonelist))
print(f"There are {n} different telephone numbers in the records.")

"""
Runtime: O(n)
"""