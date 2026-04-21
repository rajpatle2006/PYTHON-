# Appoend
lst = [1, 2, 3]
lst.append(4)
print(lst)   # [1, 2, 3, 4]

#INsert
lst = [1, 2, 3]
lst.insert(1, 100)
print(lst)   # [1, 100, 2, 3]

#Remove
lst = [1, 2, 3]
lst.remove(2)
print(lst)   # [1, 3]

# Pop
lst = [1, 2, 3]
lst.remove(2)
print(lst)   # [1, 3]

# Sort
lst = [5, 2, 8, 1]
lst.sort()
print(lst)   # [1, 2, 5, 8]

# reversed
lst = [1, 2, 3]
lst.reverse()
print(lst)   # [3, 2, 1]

#Index
lst = [10, 20, 30]
print(lst.index(20))   # 1

#Count
lst = [1, 2, 2, 3]
print(lst.count(2))   # 2

#Clear
lst = [1, 2, 3]
lst.clear()
print(lst)   # []

#Copy
lst = [1, 2, 3]
new_lst = lst.copy()
print(new_lst)