def odd_even(number):
    """Check if a number is odd or even."""
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


# Test the function
if __name__ == "__main__":
    print(f"4 is {odd_even(4)}")   # even
    print(f"7 is {odd_even(7)}")   # odd
    print(f"0 is {odd_even(0)}")   # even
    print(f"-3 is {odd_even(-3)}") # odd
