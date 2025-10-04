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
    
