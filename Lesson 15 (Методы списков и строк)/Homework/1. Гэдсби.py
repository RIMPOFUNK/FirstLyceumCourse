letter = input()
words = input().split()
error = [i for i in words if letter in i.lower()]

print(*error, sep='\n')