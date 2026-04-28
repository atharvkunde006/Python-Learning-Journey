import requests

query = input("Bhai konsi news chahiye: ")

url = f"https://newsdata.io/api/1/latest?apikey=pub_608e405f451c4b238cf23eca56a11a43&q={query}&language=en"

r = requests.get(url)
news = r.json()

if news["status"] == "success":
    for article in news["results"]:
        print("Title:", article["title"])
        print("Description:", article["description"])
        print("-" * 50)
else:
    print("Error:", news["message"])