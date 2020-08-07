from pandas import *

xls = ExcelFile('data.xlsx')
data = xls.parse(xls.sheet_names[0])
print(data.to_dict())
print(data['Input[4]'], None)
