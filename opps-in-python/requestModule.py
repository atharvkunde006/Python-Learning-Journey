#
import requests

res = requests.get("https://www.google.com")
print(res.status_code)

##
import requests

res = requests.get("https://www.google.com")
print(res.text)

###
import requests
res = requests.get("https://api.github.com")
print(res.json())