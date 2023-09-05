def add(x,y):
    return x+y
# Function to perform subtraction
def subtract(x, y):
    return x - y


# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y


# Main calculator loop
add(1,1)
subtract(1,1)
multiply(1,10)
divide(15,5)
