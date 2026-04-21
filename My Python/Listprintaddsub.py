lst=[8,10,12,13,16,21]
print(lst)
for i in range(len(lst)):
    if lst[i]%2==0:
          lst[i]-=5
    else:
         lst[i]+=5 
         print(lst)



# nums= list(map(int,input("enter numbers: ").split()))

# result =[]

# for num in nums:
#     if num%2 ==0:
#         result.append(num -5)
#     else:
#         result.append(nums+5)   
#         print("Updated list: ", result)      