lst =[2,6,8,7,9]

largest =lst[0]

for num in lst:
    if num> largest:
        largest =num
print("largest element: ", largest)     

first = second =float ('-inf')
for num in lst:
    if num > first:
        second = first
        first =num
    elif num> second and num != first:
        second= num
        print("second Largest:",second ) 
        
    