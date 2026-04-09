# def factors(n):
#     print("Factors of", n, "are:")
    
#     for i in range(1, n+1):
#         if n % i == 0:
#             print(i)

# num = int(input("Enter a number: "))
# factors(num)

def factors(n):
   
    
    for i in range(1, n+1):
        if n % i == 0:
           print(i,end=" ")  
           return 10

num = int(input("Enter a number: "))
factors(5)