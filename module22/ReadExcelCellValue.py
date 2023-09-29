import openpyxl

# load the Excel sheet where it is
workbook = openpyxl.load_workbook("C:\\Users\\Piyush Verma\\OneDrive\\Documents\\readWriteExcelInPython\\readExcel.xlsx")

# active the sheet
sheet = workbook.active

# cell for fetch the cell value
cell = sheet.cell(row=1, column=1)
data = cell.value

# print the cell value
print("The value of the cell(row=1, column=1) : ", data)