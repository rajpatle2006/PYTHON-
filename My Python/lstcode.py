lst=[0,1,2,3,4,4,5,6,6,7,8,9,4,4]
lst1=[0]
for i in lst:
    if i!=lst1[-1]:
        lst1.append(i)
print(lst1)        