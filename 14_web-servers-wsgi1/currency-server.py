import openpyxl

wb = openpyxl.load_workbook('rates-example.xlsx')
ws = wb.worksheets[0]
for r in ws.iter_rows(values_only=True):
    print(r)
