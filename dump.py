import json
data={
    "name":"Atharv",
    "age": 20,
    "skils":"python"
}
with open("file.json","w") as f:
    json.dump(data,f)