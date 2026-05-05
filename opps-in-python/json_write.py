import json

data = {
    "name": "Atharv",
    "age": 20,
    "skills": ["Python", "AI"]
}

with open("data.txt", "w") as f:
    json.dump(data, f)