n = int(input())
towns = set()

for i in range(n):
    town = input()
    towns.add(town)
    
town = input()
if town in towns:
    print("TRY ANOTHER")
else:
    print("OK")