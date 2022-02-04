import csv
import json

agencies = {}

with open('data/raw/Fire_Open_Data.csv') as source_data:

  csv_reader = csv.reader(source_data)
  next(csv_reader)

  for agency_name, date, create_time, dispatch, enroute, \
      arrive, clear, hour_of, location, event_type, priority, \
      fd_event_num, zip_code in csv_reader:

    if agency_name in agencies:
      agencies[agency_name] += 1
    else:
      agencies[agency_name] = 1

with open('calls_by_agencies.json', 'w') as json_output:
  json.dump(agencies, json_output, indent=4)
