import json

with open('calls_by_agencies.json') as jsonInput:
  agencies = json.load(jsonInput)
  for k in agencies:
    print(k)
  
  selection = input('\nEnter an agency: ')
  if selection in agencies:
    print(f'{selection} had {agencies[selection]} calls')
  else:
    print('agency does not exist')