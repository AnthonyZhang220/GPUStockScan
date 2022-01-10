import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver as wd
# from selenium.webdriver.chrome.options import Options


# from webdriver_manager.chrome import ChromeDriverManager

# driver = wd.Chrome(ChromeDriverManager().install())

# wd.implicitly_wait(60)


URL="https://www.bestbuy.com/site/searchpage.jsp?id=pcat17071&qp=gpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203060%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203060%20Ti%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203070&sp=%2Bcurrentprice%20skuidsaas&st=graphics+card"

options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
wd = wd.Chrome(options=options)

wd.get(URL)
# wd.find_element_by_xpath()

wd.set_window_size(1920,1080)
wd.save_screenshot("screenshot.png")


soup = BeautifulSoup(wd.page_source, features="html.parser")
lists = soup.find("ol",{"class":"sku-item-list"})
# print(lists);

items = lists.findAll("li",{"class": "sku-item"})

for item in items:
    print(item.text);
    
print(len(items))



