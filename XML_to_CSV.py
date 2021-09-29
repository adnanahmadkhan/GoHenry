import xml.etree.ElementTree as ET
import json
from csv import DictWriter

# loading environment
with open("env.json") as config_json:
    config = json.load(config_json)

# get an iterable
context = ET.iterparse(config['dbfile'], events=("start", "end"))

# turn it into an iterator
context = iter(context)

# get the root element
event, root = context.__next__()

# initializing data structures
row = {}
columns = []
f = open(f"{config['dbfile'][:-3]}csv", "a+", newline='\n', encoding='utf-8')
columns = ["ACCOUNTNUMBER", "CURRENCYCODE", "BALANCE", "CARDID", "PRIMARY", "CARDSTATUS", "EXPIRYDATE", "TEST"]
writer = DictWriter(f, fieldnames=columns)
row_count = 0
# iterating over the xml one account element at a time
# and dumping into csv according to bulk size
try:
    #while there is content to read in the xml file
    while event:
        (event, elem) = context.__next__()
        # get current tag and its text
        tag = str(elem.tag).strip()
        value = str(elem.text)
        # if tag is anything but an ending account tag i.e. not </account>
        if event == "end" and tag != "ACCOUNT":
            # and the tag and the value are not null or empty
            if tag not in ["", "CARD", None]:
                # put the tag as key and value as value into a dictionary
                row[tag] = value
                # also save the tag name as the 
                root.clear()
        elif event == "end" and tag == "ACCOUNT":
            if row_count == 0:
                writer.writeheader()
            row_count += 1
            writer.writerow(row)
            row = {}
except Exception as err:
    if err:
        print(err)
finally:
    f.close()
