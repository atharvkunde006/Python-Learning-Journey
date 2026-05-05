import json
data='{"name": "Atharv", "age": 20, "isStudent": true}'
object=json.loads(data)
print(object)
print(type(object))