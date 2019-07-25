# Simple Intent Recognition
Easy and Fast Intent Recognition from a natural language question using [Snips-nlu](https://github.com/snipsco/snips-nlu) as backend.

Install:
```
git clone https://github.com/abhishekyana/Intent-Recognition
cd Intent-Recognition
```
You can try the below code:
Usage:
```
from intentrecognition import IntentRecognition

#Initialize the Recognizer
IR = IntentRecognition()
IR.loadntrain()

#Use the Recognizer
text = 'book a flight from paris to london'
response = IR(text)

#Check the response
print(response)
```
Output is:
```
{'input': 'Book a flight from paris to london',
 'intent': {'intentName': 'bookFlight', 'probability': 0.7604543307451122},
 'slots': [{'entity': 'locality',
   'range': {'end': 24, 'start': 19},
   'rawValue': 'paris',
   'slotName': 'departure',
   'value': {'kind': 'Custom', 'value': 'Paris'}},
  {'entity': 'locality',
   'range': {'end': 34, 'start': 28},
   'rawValue': 'london',
   'slotName': 'destination',
   'value': {'kind': 'Custom', 'value': 'London'}}]}
```
Thank you
