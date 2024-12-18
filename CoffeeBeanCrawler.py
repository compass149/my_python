from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

from selenium import webdriver
import time

#[CODE 1]
def CoffeeBean_store(result):
    CoffeeBean_URL = "https://www.coffeebeankorea.com/store/store.asp"
   # wd = webdriver.Chrome('WebDriver 설치경로/chromedriver.exe')
    wd = webdriver.Chrome()
    
    for i in range(1, 10):
        wd.get(CoffeeBean_URL)
        time.sleep(1)
        try:
            wd.execute_script("storePop2(%d)" %i)
            time.sleep(1)
            html = wd.page_source
            soupCB=BeautifulSoup(html, 'html.parser')
            store_name_h2 = soupCB.select("div.store_txt > h2")
            store_name=store_name_h2[0].string
            print(store_name)
            store_info = soupCB.select("div.store_txt > table.store_table > tbody > tr >td")
            store_address_list = list(store_info[2])
            store_address=store_address_list[0]
            store_phone = store_info[3].string
            result.append([store_name]+[store_address]+[store_phone])
        except:
            continue
        return
    
#[code 0]
def main():
    result = []
    print('CoffeeBean store crawling >>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    CoffeeBean_store(result) #[CODE1]
    
    CB_tb1 = pd.DataFrame(result, columns=('store', 'address','phone'))
    #CB_tb1.to_csb('./6장_data/CoffeeBean.csv',encoding='cp949', mode='w'. index=True)
    CB_tb1.to_csv('./CoffeeBean.csv',encoding='cp949', mode='w', index=True)
if __name__ == '__main__':
    main()