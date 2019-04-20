import xlsxwriter


def export_check(text):
    workbook = xlsxwriter.Workbook('res.xlsx')
    worksheet = workbook.add_worksheet()

    data = [i.split('\t') for i in text.split('\n')]

    for row, (item, price, count) in enumerate(data):
        worksheet.write(row, 0, item)
        worksheet.write(row, 1, float(price))
        worksheet.write(row, 2, float(count))
        worksheet.write(row, 3, f'=B{row + 1}*C{row + 1}')

    row += 1

    worksheet.write(row, 0, 'Итого')
    worksheet.write(row, 3, f'=SUM(D1:D{row})')

    workbook.close()
