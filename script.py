import time
from selenium import webdriver as wd

URL="https://www.bestbuy.com/site/searchpage.jsp?id=pcat17071&qp=gpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203060%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203060%20Ti%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203070&sp=%2Bcurrentprice%20skuidsaas&st=graphics+card"

browser = wd.Chrome(URL)


wd.get(URL)
wd.set_window_size(1920,1080)
wd.save_screenshot(screenshot.png)

from bs4 import BeautifulSoup

soup = BeautifulSoup(wd.page_source)
items = soup.find("li",{"class":"sku-item"})

print(len(items.findAll("li")));




