"""
show-me-the-code #14
Created on Wed Oct 11 11:07:57 2017

@author: jyuchen
"""
import json
import xlwt

with open('student.txt', 'r', encoding='utf-8') as f:
    student = json.loads(f.read())
    
wb = xlwt.Workbook()
ws = wb.add_sheet('student')

c = 0
for r, s in enumerate(student):
    ws.write(r, c, s)
    c += 1
    for data in student[s]:
        ws.write(r, c, data)
        c += 1
        
    c = 0
    
wb.save('student.xls')