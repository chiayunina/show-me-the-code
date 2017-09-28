"""
show-me-the-code #11
Created on Wed Sep 27 15:55:45 2017

@author: jyuchen
"""
import re

stopwords = re.compile('|'.join(set(line.strip() for line in open('filtered_words.txt', encoding='utf-8'))))

text = input("Please input some content: ")
if stopwords.search(text):
    print("Freedom")
else:
    print("Human Right")