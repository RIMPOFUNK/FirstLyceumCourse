may_make_count = int(input())
may_make = set()

for i in range(may_make_count):
	recipe = input()
	may_make.add(recipe)
	
day_count = int(input())
maked = set()

for i in range(day_count):
	recipe_count = int(input())
	maked_in_day = set()
	
	for j in range(recipe_count):
		recipe = input()
		maked_in_day.add(recipe)
	maked = maked | maked_in_day

for i in may_make - maked:
	print(i)