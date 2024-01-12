def prima_decorator(func):
    def wrapper(n):
        result = func(n)
        if result:
            return f"{n} adalah bilangan prima."
        else:
            return f"{n} bukan bilangan prima."
    return wrapper

@prima_decorator
def is_prima(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

print(is_prima(5))  
print(is_prima(4)) 
