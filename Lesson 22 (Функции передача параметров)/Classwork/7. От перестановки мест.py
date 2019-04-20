value = "14"
addition = "91"
value += addition

print(id(value + addition))
print(id(value), end='\n\n')

value = 14
addition = 91
value += addition

print(id(value + addition))
print(id(value))

# Когда операнды is not mutable, отличия будут,
# а когда изменяемые – отличий не будет