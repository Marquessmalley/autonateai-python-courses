def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if(b==0):
        print("Error: Division by zero")
        return None
    return a / b

def power(base, exponent):
        return base ** exponent

print(add(10, 5))      # 15
print(subtract(10, 5)) # 5
print(multiply(10, 5)) # 50
print(divide(10, 5))   # 2.0
print(power(10, 5))   # 100000