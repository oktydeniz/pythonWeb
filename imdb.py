import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")
re = float(input("Rating :"))
headers = soup.find_all("td", {"class": "titleColumn"})
rating = soup.find_all("td", {"class": "ratingColumn imdbRating"})
for title, rat in zip(headers, rating):
    title = title.text
    rat = rat.text
    title = title.strip()
    title = title.replace("\n", "")
    rat = rat.strip()
    rat = rat.replace("\n", "")

    if float(rat) > re:
        print("\n Movie -> {} Rating : {}".format(title, rat))
