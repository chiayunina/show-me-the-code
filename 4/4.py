"""
show-me-the-code #4
Created on Wed Oct 11 11:07:57 2017

@author: jyuchen
"""
import re
from collections import Counter

with open('test.txt', 'r') as f:
    content = f.read()

content = re.sub('[^\w\s]', '', content).split()
t_count = Counter(content)

print(t_count)