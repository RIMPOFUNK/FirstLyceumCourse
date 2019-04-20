day = int(input())
month = int(input())
year = int(input())

if month > 2:
    month -= 2
elif month == 1:
    month = 11
    year -= 1
elif month == 2:
    month = 12
    year -= 1

YearNumber = year % 100
CenturyCount = year // 100

out = day + ((13 * month - 1) // 5) + YearNumber
out = out + (YearNumber // 4 + CenturyCount // 4 - 2 * CenturyCount + 777)
print(out % 7)