lst = [10, 20, 30, 40, 50, 60]

n = len(lst)

mid = n // 2

first_half = lst[:mid]
second_half = lst[mid:]

print("First half:", first_half)
print("Second half:", second_half)

print("Sum of first half:", sum(first_half))
print("Sum of second half:", sum(second_half))