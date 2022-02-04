import csv
import json

priority_data = {}

with open('data/raw/Fire_Open_Data.csv') as source_data:

  csv_reader = csv.reader(source_data)
  next(csv_reader)

  for agency_name, date, create_time, dispatch, enroute, \
      arrive, clear, hour_of, location, event_type, priority, \
      fd_event_num, zip_code in csv_reader:

    if priority in priority_data:
      priority_data[priority] += 1
    else:
      priority_data[priority] = 1

with open('data/clean2/calls_by_priority.json', 'w') as json_output:
  json.dump(priority_data, json_output, indent=4)
