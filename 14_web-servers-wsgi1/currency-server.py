import openpyxl

def read_rates():
    rates = {}
    wb = openpyxl.load_workbook('rates-example.xlsx')
    ws = wb.worksheets[0]
    for r in ws.iter_rows(values_only=True):
        ccode1, ccode2, rate = r
        key = (ccode1, ccode2)
        rates[key] = rate
    return rates
#-----------------------------------------


