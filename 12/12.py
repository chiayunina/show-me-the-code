"""
show-me-the-code #12
Created on Wed Sep 27 15:55:45 2017

@author: jyuchen
"""
import re

stopwords = [line.strip() for line in open('filtered_words.txt', encoding='utf-8')]

text = input("Please input some content: ")
for s in stopwords:
    if s in text:
        text = re.sub(s, '*'*len(s), text)
        
print(text)
#print(re.sub('({})'.format('|'.join(stopwords)), '*', text))
