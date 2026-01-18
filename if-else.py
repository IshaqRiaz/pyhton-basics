# Demonstration of if, elif, else in Python

def check_number(num):
    if num > 0:
        return "Positive number"
    elif num < 0:
        return "Negative number"
    else:
        return "Zero"

print(check_number(10))
print(check_number(-5))
print(check_number(0))
