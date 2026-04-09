def odd_fact(n):
    fact = 1
    for i in range(1, n+1, 2):
        fact = fact * i
    print("Odd factorial =", fact)

def even_fact(n):
    fact = 1
    for i in range(2, n+1, 2):
        fact = fact * i
    print("Even factorial =", fact)
num = int(input("Enter a number: "))

if num % 2 == 0:
    odd_fact(num)     # input even → odd factorial
else:
    even_fact(num)    # input odd → even factorial

# 2.function se solve 


# def factorial_check(num):
#     fact = 1
    
#     if num % 2 == 0:   # number even hai
#         for i in range(1, num+1, 2):   # odd numbers
#             fact = fact * i
#     else:   # number odd hai
#         for i in range(2, num+1, 2):   # even numbers
#             fact = fact * i
    
#     print("Result =", fact)

# num = int(input("Enter a number: "))
# factorial_check(num)

# 3.simply code


# num = int(input("Enter a number: "))
# fact = 1

# if num % 2 == 0:   # number even hai
#     for i in range(1, num+1, 2):   # odd numbers
#         fact = fact * i
# else:   # number odd hai
#     for i in range(2, num+1, 2):   # even numbers
#         fact = fact * i

# print("Factorial =", fact)