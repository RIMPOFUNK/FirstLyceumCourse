lst = input().split()
lst = [int(lst[i])**2 for i in range(len(lst))]

print(" ".join(str(i) for i in lst))