import base64
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
from my_library import *
from obuv_driver import *
import colorama
from colorama import Fore, Back, Style
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib import request
from urllib.parse import quote
import wget
import uuid
import configparser
from PIL import Image
import requests
from pathlib import Path
import threading
from bs4 import BeautifulSoup
from lxml import html





def poiskpers(url):
    geourl = '{0}'.format(quote(url))
    return geourl




class Good:
    def __init__(self, ol:WD, lc_link, pc_price:str):
        lc_link = lc_link.replace(r'amp;', '')
        self.pictures = []
        self.sizes = []
        self.prices = []
        self.color = ''
        self.article = ''
        self.name = ''
        self.description= ''
        self.price = ''
        self.brand = ''
        print(Fore.LIGHTGREEN_EX, 'Товар: ', Fore.LIGHTBLUE_EX, lc_link, Fore.RESET)
        self.source = ol.Get_HTML(lc_link)
        ol.Get_HTML(lc_link)
        soup = BeautifulSoup(ol.page_source, features='html5lib')
        self.name = soup.find('h1').text
        
        pic1 = str(soup.find('div', "product-image").contents[1])
        pic2 = BeautifulSoup(pic1, features='html5lib')
        self.pictures.append(pic2.find('a')['href'].replace('./',ol.site_url))

        self.price = soup.find('div', 'price').text.strip().replace('руб.','').replace(' ','')
        self.description = soup.find('div', 'tab-pane active').text.strip().replace('\n','').replace('\t','').replace('\r','')
        


