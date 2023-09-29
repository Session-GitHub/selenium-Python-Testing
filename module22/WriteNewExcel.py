from openpyxl import Workbook

# create the instance of Workbook
workbook = Workbook()

# get the total sheet name
print(workbook.active.title)
print(workbook.sheetnames)

# change the sheet name
workbook['Sheet'].title = "Programming Languages"

# active the sheet
sheet = workbook.active

# data
sheet['A1'].value = "Python"
sheet['A2'].value = "Java"
sheet['A3'].value = "Perl"
sheet['A4'].value = "Ruby"
sheet['A5'].value = "C++"
sheet['A6'].value = "C"
sheet['A7'].value = "C#"

# save the data
workbook.save("C:\\Users\\Piyush Verma\\OneDrive\\Documents\\readWriteExcelInPython\\languages.xlsx")

# print a message
print("Data has Successfully written...")

# close the workbook
workbook.close()