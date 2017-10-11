"""
show-me-the-code #15
Created on Wed Oct 11 11:07:57 2017

@author: jyuchen
"""
import json
import xlwt

with open('city.txt', 'r', encoding='utf-8') as f:
    city = json.loads(f.read())
    
wb = xlwt.Workbook()
ws = wb.add_sheet('city')

c = 0
for r, s in enumerate(city):
    ws.write(r, c, s)
    c += 1
    ws.write(r, c, city[s])
    c += 1
        
    c = 0
    
wb.save('city.xls')