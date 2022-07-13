from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
from my_library import *
import colorama
from colorama import Fore, Back, Style
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser
from bs4 import BeautifulSoup
from lxml import html
import requests


class WD:
    def init(self):
        self.site_url = 'https://kosmetika-krym.ru/'
        config = configparser.ConfigParser()
    def __init__(self):
        self.init()


    def __del__(self):
        try:
            pass
        except: pass


    def Get_HTML(self, curl):
        r = requests.get(curl)
        self.page_source = r.text
        return r.text


    def Get_List_Of_Links_On_Goods_From_Catalog(self, pc_link):
        print(Fore.RED + 'Список товаров каталога: ' + Fore.YELLOW + pc_link + Fore.RESET)
        ll_catalog_items = []
        self.Get_HTML(pc_link)
        soup = BeautifulSoup(self.page_source, features='html5lib')
        items = soup.find_all('div', {'class': 'product-thumb'})
        print('count:', len(items))
        for item in items:
            hrefs_soup = BeautifulSoup(str(item.contents[1]), features='html5lib')
            lc_link = hrefs_soup.find('a')['href'].replace('./',self.site_url)
            if lc_link not in ll_catalog_items:
                ll_catalog_items.append(lc_link)
        return ll_catalog_items


    def Write_To_File(self, cfilename):
        file = open(cfilename, "w", encoding='utf-8')
        file.write(self.page_source)
        file.close()


def Login():
    return WD()


colorama.init()

#wd = Login()
#print(wd.Get_List_Of_Links_On_Goods_From_Catalog('https://kosmetika-krym.ru/catalog/travyanoy_chay_kryima/'))
