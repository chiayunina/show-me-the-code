"""
show-me-the-code #13
Created on Wed Oct 20 2017

@author: jyuchen
"""
#import os
import requests
from bs4 import BeautifulSoup

r = requests.get('http://tieba.baidu.com/p/2166231880')
data = r.text
soup = BeautifulSoup(data, 'lxml')

file_count = 0
for link in soup.find_all('img', class_="BDE_Image"):
    image = link.get('src')
#    image_name = os.path.split(image)[1]
    
    r2 = requests.get(image)
    with open('{}.jpg'.format(file_count), 'wb') as f:
        f.write(r2.content)
        
    file_count += 1