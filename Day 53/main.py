from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://appbrewery.github.io/Zillow-Clone/"
GOOGLE_FORMS_LINK = "https://docs.google.com/forms/d/e/1FAIpQLScw5j36ZuNqwVuU-y3DQz6pcoUeXbxceTfVLodcTEXiERmjmw/viewform?usp=dialog"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(URL, headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")

link = soup.select(".StyledPropertyCardDataWrapper a")
links = [link["href"] for link in link]
print(f"There are {len(links)} links in total: \n")
print(links)

address = soup.select(".StyledPropertyCardDataWrapper address")
addresses = [address.get_text().replace(" | ", " ").strip() for address in address]
print(f"\n Here is all {len(addresses)} addresses: \n")
print(addresses)

price = soup.select(".PropertyCardWrapper span")
prices = [price.get_text().replace("/mo", "").split("+")[0] for price in price if "$" in price.text]
print(f"\n Here is all {len(prices)} prices: \n")
print(prices)

chrome = webdriver.ChromeOptions()
chrome.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome)

for n in range(len(links)):
    driver.get(GOOGLE_FORMS_LINK)
    time.sleep(2)
    address = driver.find_element(by=By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(by=By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(by=By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(by=By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address.send_keys(addresses[n])
    price.send_keys(prices[n])
    link.send_keys(links[n])
    submit_button.click()

    time.sleep(1)

print(f"All data has been stored in google forms.")