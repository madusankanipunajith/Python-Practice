import openpyxl as xl

wb = xl.load_workbook("transactions.xlsx")

sheet = wb["Sheet1"]
cell = sheet["a1"]
cell_2 = sheet.cell(1, 1)

print(cell.value)
print(cell_2.value)



