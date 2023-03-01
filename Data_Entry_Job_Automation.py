#!/usr/bin/env python
# coding: utf-8

# In[112]:


from bs4 import BeautifulSoup
import requests

headers={
    "User-Agent":"",
    "Accept-Language":""
}

response=requests.get("https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.916810261970156%2C%22east%22%3A-122.23832167578125%2C%22south%22%3A37.633501230568804%2C%22west%22%3A-122.62833632421875%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D",headers=headers)
data=response.text

soup = BeautifulSoup(data, "html.parser")

all_link_elements=soup.find_all("a","StyledPropertyCardDataArea-c11n-8-82-3__sc-yipmu-0 hiBOYq property-card-link")


all_links = []
for link in all_link_elements:
    href = link["href"]
    
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

all_adress_elements=soup.select("body article address")

all_addresses=[addr.get_text().split(" | ")[-1] for addr in all_adress_elements]


all_prices_elements=soup.select("body ul li article span")
all_prices=[price.get_text().split("+")[0] for price in prices_elements if "$" in price.text]
print(all_prices)


# In[130]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

google_form_link="your google form link"

chrome_driver_path = Service("")

driver=webdriver.Chrome(service=chrome_driver_path)


for n in range(len(all_links)):
    
    
    driver.get(google_form_link)
    time.sleep(5)
    your_addr=driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    your_addr.send_keys(all_addresses[n])
    time.sleep(2)
    your_price=driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    your_price.send_keys(all_prices[n])
    time.sleep(2)
    your_link=driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    your_link.send_keys(all_links[n])
    time.sleep(3)
    submit_button=driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_button.click()


# In[ ]:




