"""
show-me-the-code #12
Created on Wed Sep 27 15:55:45 2017

@author: jyuchen
"""
import re

stopwords = set(line.strip() for line in open('filtered_words.txt', encoding='utf-8'))

text = input("Please input some content: ")
print(re.sub('({})'.format('|'.join(stopwords)), '*', text))