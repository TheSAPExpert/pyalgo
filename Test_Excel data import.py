import xlrd
book = xlrd.open_workbook('Database1.xlsx')
sheet = book.sheet_by_name('Sheet1')
data = [[sheet.cell_value(r, c) for r in range(sheet.nrows)] for c in range(sheet.ncols)]
#Profit !
print(data)