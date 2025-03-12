from bs4 import BeautifulSoup
import requests




#1 Use BeautifulSoup to get hold of the price of the item as a floating point number and print it out.

live_url = "https://www.amazon.in/Lifelong-Dumbbells-Equipment-Exercise-Warranty/dp/B09W5PSTBP/?_encoding=UTF8&content-id=amzn1.sym.211684f4-ebe1-443f-8a4a-0773471e979f&pd_rd_r=0140ff3a-58cf-49e3-b7b2-db3e4e75c965&pd_rd_w=R9M3E&pd_rd_wg=A6dMD&pf_rd_p=211684f4-ebe1-443f-8a4a-0773471e979f&pf_rd_r=KDRFX0JX48JG0T1C282B&th=1&ref_=nav_ya_signin"
response = requests.get(live_url)

soup = BeautifulSoup(response.content, "html.parser")
print(response.text)

# Find the HTML element that contains the price
price = soup.find(class_="a-offscreen")
print(price.text)

# Remove the dollar sign using split
price_without_currency = price.text.split("₹")[1]
print(price_without_currency)
# Convert to floating point number
price_as_float = float(price_without_currency)
print(price_as_float)