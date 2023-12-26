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
from click import echo, style
from fake_useragent import UserAgent

def poiskpers(url):
    geourl = '{0}'.format(quote(url))
    return geourl

class Good:
    def __init__(self, ol:WD, pc_link, pc_price:str):
        pc_link = pc_link.replace(r'amp;', '')
        self.pictures = []
        self.sizes = []
        self.prices = []
        self.color = ''
        self.article = ''
        self.name = ''
        self.description= ''
        self.price = ''
        self.brand = ''
        echo(style('Товар: ', fg='bright_yellow') + style(pc_link, fg='bright_white') + style('  Прайс:', fg='bright_cyan') + style(pc_price, fg='bright_green'))
        self.source = ol.Get_HTML(pc_link)
        ol.Get_HTML(pc_link)
        soup = BeautifulSoup(ol.page_source, features='html5lib')

        self.name = soup.find('h1', {'class':'product-title'}).text
        self.article = soup.find('p', {'class':'model'}).text

        prices = soup.find_all('span', {'class':'price'})
        for price in prices:
            if 'line-through' not in str(price):
                self.price = price.text.strip().replace('руб.','').replace(' ','').replace('₽','')

        
        try: self.description = soup.find('h4').text.replace('\n','').replace('\t','').replace('\r','')
        except: pass
        lc_descr = sx(ol.page_source, '<p class="description"><p>','<ul class="')
        descr = BeautifulSoup(lc_descr, features='html5lib')
        paragraphs = descr.find_all('span')
        for paragraph in paragraphs:
            self.description = self.description + ' ' + paragraph.text.strip().replace('\n','').replace('\t','').replace('\r','')
        self.description = self.description.strip()

        images_soup = BeautifulSoup(str(soup.find('div', {'id':'product_slideshow'})), features='html5lib')
        images = images_soup.find_all('img', {'class':'img-responsive'})
        for image in images:
            self.pictures.append(image['src'])

        sizes_soup = BeautifulSoup(str(soup.find('select', {'class':'form-control select'})), features='html5lib')
        sizes = sizes_soup.find_all('option')
        for size in sizes:
            lc_size = size.text.strip()
            if lc_size not in self.sizes and lc_size!='Выбрать':
                self.sizes.append(lc_size)
