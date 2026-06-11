import json

data_string = '{"name": "Atharv", "age": 20, "skils": "python"}'

data = json.loads(data_string)

print(data)