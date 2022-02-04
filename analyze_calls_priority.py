import json
INPUT_FILE_PATH = 'data/clean2/calls_by_priority.json'
with open(INPUT_FILE_PATH) as jsonInput:
  priorities = json.load(jsonInput)
  for k in priorities:
    print(k)
  
  selection = input('\nEnter an priority level: ')
  if selection in priorities:
    print(f'There were {priorities[selection]} with priority {selection}')
  else:
    print('priority level does not exist')