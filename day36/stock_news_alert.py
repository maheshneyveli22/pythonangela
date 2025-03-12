
import requests
STOCK_API_KEY = "L4NNS4MZ87EXEKXO"
NEWS_API_KEY = "58affcd35bba4a588a9bcdc9b9fc3e57"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"

#TODO 1. - Get yesterday's closing stock price
    #api key from www.alphavantage.co: L4NNS4MZ87EXEKXO
    #api documentation:
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params= stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

#TODO 2. - Get the day before yesterday's closing stock price

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

#TODO 3. get the positive difference between those closing prices
# abs helps to get positive difference value
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))

print(difference)

#TODO 4. Calculate the percentage difference in price between yesterday closing price and day before yesterday closing price
diff_percent = (difference/ float(yesterday_closing_price ))*100
print(diff_percent)

#TODO 5. if percentage difference is greater than 5, print news
#Use newsapi: https://newsapi.org/register/success
# Your API key is: 58affcd35bba4a588a9bcdc9b9fc3e57
if diff_percent >1:
    news_params = {
        "apiKey" : NEWS_API_KEY,
        "qInTitle": COMPANY_NAME

    }
    news_response = requests.get(NEWS_ENDPOINT,params = news_params)
    articles = news_response.json()["articles"]

    #TODO 6. Use Python slice operator to create a list that contains first 3 articles
    three_articles = articles[:3]
  #  print(three_articles)

    #TODO 7. Create a new list of first 3 article's headline and description using list comprehension
    # "Headline: {article title}. \nBrief: {article description}"
    # [new_item for item in list]
    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)
