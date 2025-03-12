from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text



soup = BeautifulSoup(yc_web_page, "html.parser")
#1 printing title of html page
print(soup.title)

#2 Printing title of articles or news listed
article_tags = soup.find_all(name = "a" , class_ = "storyLink")
article_texts = []
article_links = []
for article_tag in article_tags:
    text = article_tag.getText()
    article_texts.append((text))
    link = article_tag.get("href")
    article_links.append(link)
article_upvotes = [score.getText() for score in soup.find_all(name ="span", class_ = "score").getText()]

print(article_texts)
print(article_links)
print(article_upvotes)

#We can see what can be scraped and what can be :

#news.ycombinator.com/robots.txt

#-> Disallow means that particular endpoint is not allowed for scrapping