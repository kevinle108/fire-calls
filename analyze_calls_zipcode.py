import json
import math

INPUT_FILE_PATH = 'data/clean2/calls_by_zipcode.json'
with open(INPUT_FILE_PATH) as jsonInput:
  zipcode = json.load(jsonInput)
  for k in zipcode:
    print(k)
  
  selection = input('\nEnter an zipcode: ')
  if selection in zipcode:
    call_total = zipcode[selection].get('CALL_TOTAL')
    call_fire = zipcode[selection].get('FIRE_TOTAL')
    fire_percentage = math.ceil(round((call_fire / call_total * 100), 1))
    # print(call_total, call_fire)
    print(f'Zipcode {selection} had {call_total} calls, {fire_percentage}% of which for fires')
  else:
    print('zipcode does not exist')