GET = input().split('?')[1]
tag = input()

GET = [i for i in GET.split('&')]

for i in GET:
    if tag in i:
        print(i.split('=')[1])
