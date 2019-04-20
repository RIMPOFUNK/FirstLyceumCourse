size = int(input())
lst = []

for i in range(size):
    value = int(input())
    lst.append(value)

begin = int(input()) - 1
end = int(input())

print(sum(lst[begin:end]))
