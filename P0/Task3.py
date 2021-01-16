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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
# Part A
def isFixedline(num: str):
  return num[0] == '('

def fixedlineCode(num: str):
  pos = num.find(')')
  return num[1:pos]

def isMobile(num: str):
  return num.find(' ') != -1

def mobileCode(num: str):
  return num[:4]

def isTelemarketer(num: str):
  return num[:3] == '140'

def telemarketerCode(num: str):
  return num[:3]

def getAreaCode(num):
  if isFixedline(num): return fixedlineCode(num)
  if isMobile(num): return mobileCode(num)
  if isTelemarketer(num): return telemarketerCode(num)
  return None

def isBangalore(num: str):
  return num[:5] == '(080)'

codes = []
for call in calls:
  calling = call[0]
  if isBangalore(calling):
    receiving = call[1]
    codes.append(getAreaCode(receiving))

uniquecodes = list(set(codes))
uniquecodes.sort()
print("The numbers called by people in Bangalore have codes:")
for code in uniquecodes:
  print(code)

# Part B
callBangalore = 0
receiveBangalore = 0
for call in calls:
  calling = call[0]
  if isBangalore(calling):
    callBangalore += 1
    receiving = call[1]
    if isBangalore(receiving):
      receiveBangalore += 1

print(f"{receiveBangalore/callBangalore*100:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

"""
Runtime: O(n)
"""