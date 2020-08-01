import requests 
import random
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

def get_image():
	URL = 'https://www.anekdot.ru/random/mem/'
	first_html = requests.get(URL, headers={'User-Agent': UserAgent().chrome})
	second_html = first_html.content
	real_html = BeautifulSoup(second_html,'html.parser')
	obj = str(real_html.find('div', attrs = {'class':'text'}))
	return obj[obj.find('src') + 5 : obj[obj.find('src') + 5:].find('"') + obj.find('src') + 5]


