#creat xlsx file from scratch
from openpyxl import Workbook

wb=Workbook()
#to se name of active sheet   
#print(wb.active.title)
#print(wb.sheetnames)

#change sheet name
wb['Sheet'].title="Page One"

sh1=wb.active
sh1['A1'].value="1st Name"
sh1['B1'].value="2nd Name"
sh1['C1'].value="age"

wb.save("Finalreport003.xlsx")

