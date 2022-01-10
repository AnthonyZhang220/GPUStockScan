import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver as wd
from IPython.display import display
import pandas as pd
# from selenium.webdriver.chrome.options import Options

# from webdriver_manager.chrome import ChromeDriverManager

# driver = wd.Chrome(ChromeDriverManager().install())

# wd.implicitly_wait(60)


URL = "https://www.bestbuy.com/site/searchpage.jsp?id=pcat17071&qp=gpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203060%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203060%20Ti%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203070&sp=%2Bcurrentprice%20skuidsaas&st=graphics+card"

options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--start-maximized")
options.add_argument("window-size=1920,1080")
wd = wd.Chrome(options=options)

wd.get(URL)
# wd.find_element_by_xpath()

wd.save_screenshot("screenshot.png")


soup = BeautifulSoup(wd.page_source, features="html.parser")
lists = soup.find("ol", {"class": "sku-item-list"})
# print(lists);

items = lists.findAll("li", {"class": "sku-item"})

rows_processed = []


for item in items:
    title = item.find("h4", {"class": "sku-header"})
    button = item.find("div", {"class": "sku-list-item-button"})
    row = []

    row.append(title.text)
    row.append(button.text)

    print(title.text)
    print(button.text)

    rows_processed.append(row)


pd.set_option("display.max_colwidth", -1)


df = pd.DataFrame.from_records(rows_processed, columns=[
                               "Item Title", "Status"])

display(df)

print(len(items))

isAvailable = "Add to Cart" in df["Status"].values
print(isAvailable)
