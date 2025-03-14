from selenium import webdriver
from selenium.webdriver.common.by import By


# By default chrome browser gets closed after opening
# To keep it open, we need to set chrome_options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options = chrome_options)
# driver.get("https://www.amazon.in/")
driver.get("https://www.python.org/")


# price_dollar = driver.find_element(By.CLASS_NAME, value = "a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value= "a-price-fraction")
#
# print(f"The price is {price_dollar.text}.{price_cents.text}")

# search_bar = driver.find_element(By.NAME, value ="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value ="submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

#Closing chrome browser programatically
#close() closes the active tab, while quit completely closes the browser
#driver.close()

link = driver.find_element(By.XPATH, value ='//*[@id="community"]/a')
print(link.text)




#printing event dates from python.org
event_times = driver.find_elements(By.CSS_SELECTOR, value =".event-widget time")
for time in event_times:
    print(time.text)

#printing event names from python.org
event_names = driver.find_elements(By.CSS_SELECTOR, value =".event-widget a")
for name in event_names:
    print(name.text)

events_dict= {}

for n in range(len(event_times)):
    events_dict[n] = {
    "time": event_times[n].text,
    "name": event_names[n].text
    }

    print(events_dict)

driver.quit()
