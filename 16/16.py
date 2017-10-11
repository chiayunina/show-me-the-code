"""
show-me-the-code #16
Created on Wed Oct 11 11:07:57 2017

@author: jyuchen
"""
import json
import xlwt

with open('numbers.txt', 'r', encoding='utf-8') as f:
    nums = json.loads(f.read())
    
wb = xlwt.Workbook()
ws = wb.add_sheet('numbers')

c = 0
for r, num in enumerate(nums):
    for n in num:
        ws.write(r, c, n)
        c += 1
        
    c = 0
    
wb.save('numbers.xls')