import requests
import json
query = input("What type of news do you want ?")
url = (f"https://newsapi.org/v2/everything?q={query}&from=2025-04-03&sortBy=publishedAt&apiKey=25070141f6b3445e8836d80d68c11268")

d = requests.get(url)
news = json.loads(d.text)
for article in news["articles"]:
    print(((article["title"])))
    print("***")
    print(article["description"])
    print("--------------------------------")