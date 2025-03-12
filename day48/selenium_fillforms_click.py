from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

#navigate to wikipedia
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(article_count.text)
# article_count.click()


#Find element by link text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

#find the "search" <input> by Name
search = driver.find_element(By.NAME, value="search")

#Sending keyboard input to selenium
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

#navigate to registration page and fill the form
driver.get("https://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

# filling the form
first_name.send_keys("Maheswaran")
last_name.send_keys("Elumalai")
email.send_keys("mddee@test.com")

#locate the signup button
signup_button = driver.find_element(By.CSS_SELECTOR, value="form button")
signup_button.click()
