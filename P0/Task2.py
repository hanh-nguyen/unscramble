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
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
callrecord = {}
for call in calls:
    calling = call[0]
    receiving = call[1]
    time = int(call[-1])
    callrecord[calling] = callrecord.get(calling, 0) + time
    callrecord[receiving] = callrecord.get(receiving, 0) + time   

longest_number = max(callrecord, key=callrecord.get)
longest_time = callrecord[longest_number]

print(f"{longest_number} spent the longest time, {longest_time} seconds, on the phone during September 2016.")


"""
Answer: (080)33251027 spent the longest time, 90456 seconds, on the phone during September 2016.
Runtime: O(n)
"""