import xlsxwriter


def export_check(text):
    workbook = xlsxwriter.Workbook('res.xlsx')

    checks = list(map(lambda x: sorted(x.split('\n')), text.split("---")))
    for i in checks:
        add = {}
        for j in i:
            if j == '':
                continue

            cc = j.split('\t')
            key, val = (cc[0], int(cc[1])), int(cc[2])

            if key in add:
                add[key] += val
            else:
                add[key] = val

        if add:
            worksheet = workbook.add_worksheet()
            for row, (item_price, count) in enumerate(add.items()):
                worksheet.write(row, 0, item_price[0])
                worksheet.write(row, 1, float(item_price[1]))
                worksheet.write(row, 2, float(count))
                worksheet.write(row, 3, f'=B{row + 1}*C{row + 1}')

            row += 1

            worksheet.write(row, 0, 'Итого')
            worksheet.write(row, 3, f'=SUM(D1:D{row})')
    workbook.close()
