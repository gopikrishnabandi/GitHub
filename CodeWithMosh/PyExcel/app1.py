# command query seperation
# principle states that methods or functions should either be commands that perform an action or change the state of a system, or a query that return the answer to the caller without changing the state or causing side effects, they cannot be both

# violation below
import openpyxl
wb = openpyxl.load_workbook("transactions.xlsx")
sheet = wb["Sheet1"]
for row in range(1, 10):
    cell = sheet.cell(row, 1)
    print(cell.value)
sheet.append([1, 2, 3])
wb.save("transactions2.xlsx")  # new row is added after spaces instead of adding after the records, this is because original sheet has 4 rows, but for loop created a rwo instead of giving a value, this is violation of command query principle

# in lists if we try to accees an elemnt that doesnot exist, it raises an exception, it does not create one, same with dictionary if we try ro access an id that doesnt exist
# so beaware of cell method
