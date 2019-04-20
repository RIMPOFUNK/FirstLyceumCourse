import xlsxwriter
from sys import stdin


def create_stat():
    val = {i.split()[0]: int(i.strip().split()[1]) for i in stdin.readlines()}
    print(val)

    workbook = xlsxwriter.Workbook('res.xlsx')
    worksheet = workbook.add_worksheet()

    for row, (item, price) in enumerate(val.items()):
        worksheet.write(row, 0, item)
        worksheet.write(row, 1, price)

    chart = workbook.add_chart({'type': 'pie'})
    chart.add_series({'values': f'=Sheet1!B1:B{row + 1}',
                      'categories': f'=Sheet1!A1:A{row + 1}'})

    worksheet.insert_chart('C3', chart)
    workbook.close()

