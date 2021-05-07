def fibonacci (n):
    
    if n > 1 :
        previous_1 = fibonacci(n-1)
        previous_2 = fibonacci(n-2)
        return previous_1 + previous_2


# Base cases 
    if n == 0 :
        return 0
    
    if n == 1 :
        return 1

