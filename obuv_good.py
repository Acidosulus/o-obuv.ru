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
        self.price = soup.find('span', {'class':'price'}).text.strip().replace('руб.','').replace(' ','').replace('₽','')
        
        
        lc_descr = sx(ol.page_source, '<p class="description"><p>','<ul class="')
        descr = BeautifulSoup(lc_descr, features='html5lib')
        paragraphs = descr.find_all('span')
        for paragraph in paragraphs:
            self.description = self.description + ' ' + paragraph.text.strip().replace('\n','').replace('\t','').replace('\r','')
        self.description = self.description.strip()
        
        images_container = str(soup.find('div', {'id':'product_slideshow'}))
        images_soup = BeautifulSoup(images_container, features='html5lib')
        images = images_soup.find_all('img', {'class':'img-responsive'})
        for image in images:
            self.pictures.append(image['src'])

        return


        pic1 = str(soup.find('div', "product-image").contents[1])
        pic2 = BeautifulSoup(pic1, features='html5lib')
        self.pictures.append(pic2.find('a')['href'].replace('./',ol.site_url))

        self.price = soup.find('div', 'price').text.strip().replace('руб.','').replace(' ','')
        self.description = soup.find('div', 'tab-pane active').text.strip().replace('\n','').replace('\t','').replace('\r','')
        


