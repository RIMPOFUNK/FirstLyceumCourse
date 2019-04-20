have_count = int(input())
have = set()

for i in range(have_count):
    product = input()
    have.add(product)

iter_count = int(input())
may_make = []

for i in range(iter_count):
    recipe_name = input()
    needed_product_count = int(input())
    needed_product = set()

    for j in range(needed_product_count):
        product = input()
        needed_product.add(product)

    if have >= needed_product:
        may_make.append(recipe_name)

for i in may_make:
    print(i)
