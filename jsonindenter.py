import json
jsonfile = ''


with open(jsonfile) as f:
    data = json.load(f)

with open(jsonfile, 'w') as f:
    json.dump(data, f, indent=2)