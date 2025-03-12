from selenium import webdriver

# By default chrome browser gets closed after opening
# To keep it open, we need to set chrome_options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options = chrome_options)
driver.get("https://www.amazon.in/")

#Closing chrome browser programatically
#close() closes the active tab, while quit completely closes the browser
#driver.close()
driver.quit()