print("\n===== 1. Lambda =====\n")

from functools import reduce

# One line anonymous function
add = lambda x, y: x + y
print(f"Lambda: {add(5, 7)} (5 + 7)")

numbers = [5, 4, 3, 2, 1]
print(f"\nList: {numbers}\n")

# The most common usage is as an argument
sorted_numbers = sorted(numbers, key=lambda x: (x < 3, x))
print(f"Sorted: {sorted_numbers}")

# Transform each element with a function
my_map = map(lambda x: x * 2, numbers)
# We should convert a result to a list
print(f"Map: {list(my_map)}")

# Return all elements that satisfy the condition
my_filter = filter(lambda x: x > 2, numbers)
print(f"Filter: {list(my_filter)}")

# We can combine this two functions
new_numbers = [x * 2 for x in numbers if x > 2]
print(f"\nMix: {new_numbers}")

# Repeatedly apply the function to
# the elements and return a single value
my_reduce = reduce(lambda x, y: x + y, numbers)
print(f"Reduce: {my_reduce}")
