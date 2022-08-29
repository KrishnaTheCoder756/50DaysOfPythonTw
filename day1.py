# Day-1 of 50 Days Of Code By Benjamin Bennett Alexander

def divide_or_square(n):
    if n % 5 == 0:
        square_root = n ** 0.5
        return f"We found your number is divisible by 5, so the square root of your number is {square_root}"
    else:
        return f"As your number is not divisible by 5, the remainder of your number divided by 5 is {n%5}"

n1 = input("Enter your number: ")
divide_or_square(n1)
