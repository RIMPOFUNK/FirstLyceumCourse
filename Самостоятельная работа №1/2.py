def count(value: str, key="aeiouy"):
    return len(list(filter(lambda x: x.lower() in key, set(value)))) >= 3


size = int(input())
val = [input() for _ in range(size)]

let = "abcdefghijklmnopqrstuvwxyz"

print(*[i for i in val if i[0] in let and count(i) and not (len(set(i)) % 2)], sep='\n')
