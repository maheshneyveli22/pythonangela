import requests
from bs4 import BeautifulSoup
URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

# print(soup.prettify())

all_movies = soup.find_all(name="h3").find("strong")
print(all_movies)