def make_negative(lst: list):
    ret = list(map(lambda x: x * -1 if x >= 0 else x, lst))
    lst.clear()
    lst.extend(ret)


def square(lst: list):
    ret = list(map(lambda x: x**2, lst))
    lst.clear()
    lst.extend(ret)


def strange_command(lst: list):
    ret = list(map(lambda x: x + 1 if not x % 5 else x, lst))
    lst.clear()
    lst.extend(ret)


val = list(map(int, input().split()))
funcs = {"strange_command": strange_command, 
         "square": square,
         "make_negative": make_negative}

n = int(input())
for i in range(n):
    command = input()
    funcs[command](val) if command in funcs else ...
        
print(*val, sep=' ')