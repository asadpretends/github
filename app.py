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
add(1,2)
subtract(4,1)
multiply(5,6)
divide(15,5)
