import SQL


def get_rows(data):
    rows = []
    for row in data:
        rows.append(row)
    return rows


def get_columns(data):
    columns = []
    for row in data:
        columns.append([row[0]])
    return columns


SQL.my_cursor.callproc('sal_empl')
print("Printing laptop details")
res2 = []
for result in SQL.my_cursor.stored_results():
    res2.append(result.fetchall())
print(res2)
get_rows(result)
get_columns(result)