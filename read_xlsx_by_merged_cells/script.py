import xlrd

workbook = xlrd.open_workbook('a.xlsx')
worksheet = workbook.sheet_by_index(0)

num_rows = worksheet.nrows
num_cells = worksheet.ncols

curr_row = 0

data = {}
merged_cell_count = 0

while curr_row < num_rows:
    row = worksheet.row(curr_row)
    print ('Row:', curr_row)

    first_cell_value = worksheet.cell_value(curr_row, 0)
    
    if first_cell_value:
        merged_cell_count = merged_cell_count + 1
        data[merged_cell_count - 1] = []
    
    row_data = {}
    curr_cell = 1

    while curr_cell < num_cells:
        row_data[curr_cell] = worksheet.cell_value(curr_row, curr_cell)
        curr_cell = curr_cell + 1

    data[merged_cell_count - 1].append(row_data)
    curr_row = curr_row + 1

print(data)
