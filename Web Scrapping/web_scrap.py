import requests
from bs4 import BeautifulSoup # Parsing HTML & XML docs
url = "https://www.hamropatro.com/rashifal"
data = requests.get(url=url)
soup = BeautifulSoup(data.content)
print(soup)