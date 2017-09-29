"""
show-me-the-code #1
Created on Thu Sep 28 16:40:25 2017

@author: jyuchen
"""
import random

charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
coupons = set()

# set不重複
while len(coupons) < 200:
    c = ''.join([random.choice(charset) for _ in range(8)])
    coupons.add(c)