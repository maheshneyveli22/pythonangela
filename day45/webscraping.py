from bs4 import BeautifulSoup

# import lxml

with open("website.html") as file:
    contents = file.read()


soup = BeautifulSoup(contents, "html.parser")
# print(soup)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)

#Scrapping all of the anchor or title tags

# all_anchor_tags = soup.find_all(name = "a")
#
# # to get only text in the anchor tag
# for tag in all_anchor_tags:
#     #print(tag.getText())
#     # to get only href
#     print(tag.get("href"))

# # to get a h1 with particular id
# heading = soup.find_all(name="h1" ,id="name")
# print(heading)
#
# section_heading = soup.find(name ="h3", class_="heading")
# print(section_heading)

company_url = soup.select_one(selector="p a")
print(company_url)

# to select Id
name = soup.select_one(selector = "#name")
print(name)

headings = soup.select(".heading")
print(headings)
