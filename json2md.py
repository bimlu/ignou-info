import json
import os


def json2md(in_file_name, out_file_name):
  with open(in_file_name, 'r') as in_file:
    json_data = in_file.read()
    in_data = json.loads(json_data)

    with open(out_file_name, 'w') as out_file:
      if 'army' in in_file_name:
        out_file.write('| Sl. | Regional Centre | RC Code | Address | Operational Area |' + '\n')
      else:
        out_file.write('| Sl. | Regional Centre | RC Code | Address | Jurisdiction |' + '\n')

      out_file.write('| --- | --------------- | ------- | ------- | ------------ |' + '\n')
      count = 1
      for (rc_name, rc_code, rc_address, rc_juridiction) in in_data:
        out_file.write('|' + str(count))
        out_file.write('|' + rc_name)
        out_file.write('|' + rc_code)
        out_file.write('|' + rc_address)
        out_file.write('|' + rc_juridiction )
        out_file.write('|' + '\n')
        count += 1

# json2md('rc.json', 'rc.md')
json2md('rc_army.json', 'rc_army.md')
