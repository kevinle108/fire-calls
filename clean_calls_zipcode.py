import csv
import json
from unicodedata import category

INPUT_FILE_PATH = 'data/raw/Fire_Open_Data.csv'

zipcode_data = {}

with open(INPUT_FILE_PATH) as source_data:

  csv_reader = csv.reader(source_data)
  next(csv_reader)

  for agency_name, date, create_time, dispatch, enroute, \
      arrive, clear, hour_of, location, event_type, priority, \
      fd_event_num, zip_code in csv_reader:

    if zip_code in zipcode_data:
      zipcode_data[zip_code]['CALL_TOTAL'] += 1
    else:
      zipcode_data[zip_code] = {
         'CALL_TOTAL': 1, 'FIRE_TOTAL': 0, 'OTHER_TOTAL': 0 
      }
    
    category = event_type.split('--')[0]
    if category == 'FIRE':
      zipcode_data[zip_code]['FIRE_TOTAL'] += 1
    else:
      zipcode_data[zip_code]['OTHER_TOTAL'] += 1

# replace empty zipcode with 'Unknown'
zipcode_data['Unknown'] = zipcode_data.pop('')     

with open('data/clean2/calls_by_zipcode.json', 'w') as json_output:
  json.dump(zipcode_data, json_output, indent=4)
