# Prints the title of the challenge 
print("=== Challenge 1: Collatz Conjecture ===")

# Asking the user to enter a starting number and set step counter to 0
current_number = int(input("Enter starting number: "))
step_count = 0

# First part of the print statement
print("Sequence:", end=" ")

# Tells the loop to run as long as the current number is not 1
while current_number != 1:
    # Prints the current number 
    print(current_number, end=" ")

    # Determines if the current number is even and divides it by 2
    if current_number % 2 == 0:
        current_number = current_number // 2
    else:
        # Determines if the current number is odd and multiplies it by 3 and adds 1
        current_number = (current_number * 3) + 1
    
    # Adds a step to the step count
    step_count = step_count + 1

# Prints the final number 
print(current_number)

# Prints the total number of steps taken 
print(f"Steps: {step_count}\n")
    
# Challenge 2: Prime Number Checker

# Printing the title of challenge 2
print("=== Challenge 2: Prime Number Checker ===")

# Asks user to input a number
number = int(input("Enter a number: "))

# Determines if the number is greater than 1
if number > 1:
    print(f"Testing divisors from 2 to {number - 1}...")
    # Loops through the numbers 2 to the number inputted minus 1
    for num in range(2, number):
        # Determines if the number is evenly divisible 
        if (number % num) == 0:
            print(f"{number} is not prime (divisible by {num})\n")
            break
    # Determines if the number cannot be divided evenly
    else:
        print(f"{number} is prime!\n")

# Challenge 3: Multiplication Table Grid

# Printing the title of challenge 3
print("=== Challenge 3: Multiplication Table ===")

# Print header
print("Multiplication Table:")

# Prints a space to separate row from products
print("    ", end="")

# Print column header of numbers
for column in range(1, 11):
    print(f"{column:4}", end="")

# Prints a new line
print()

# Prints rows of numbers
for row in range(1, 11):
    print(f"{row:4}", end="")

    # Prints the products of the rows and columns
    for column in range(1, 11):
        product = row * column
        print(f"{product:4}", end="")
    print()