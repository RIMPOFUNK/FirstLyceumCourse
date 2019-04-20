nums = input().split()
strings = input().split()

lst = []
strings[0] = strings[0].lower()

for i in nums:
    lst.append(strings[int(i) - 1])
        
lst[0] = lst[0].capitalize()

for i in lst:
    print(i, end=' ')