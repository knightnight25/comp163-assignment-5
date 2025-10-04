# comp163-assignment-5
This document explains the design choices, loop rationale, and implementation details for the three programming challenges.

---

 Challenge 1: Collatz Conjecture Sequence

Chosen Loop Type: while loop

A while loop was chosen because the number of iterations (steps) required to complete the Collatz sequence is unknown. The loop must continue executing as long as the condition (current_number != 1) is true, making the while structure the most appropriate choice for indeterminate iteration.

Solution Description: 
The solution initializes the starting number and a step counter. It uses the while loop to:
1.  Check if the number is even (% 2 == 0) or odd.
2.  Apply the correct transformation (current_num//2 or 3 * current_num +1).
3.  Increment the step count.
The sequence is printed on a single line using the end="" argument in the print() function.

---

Challenge 2: Prime Number Checker

Chosen Loop Type: for loop

A for loop was chosen because the range of iterations is fixed and known immediately upon input. The algorithm requires testing every divisor from 2 up to n-1. The for num in range(2, number): syntax precisely and cleanly defines this finite, sequential range. The break keyword provides an early exit optimization once a divisor is found.

Solution Description
The code first assumes the number is prime. It then uses the for loop and the modulo operator (%) to test for even division. If number % num == 0, the number is marked as non-prime, the divisor is recorded, and the loop is immediately terminated. The final output provides the result and the first divisor found.

---

Challenge 3: Multiplication Table

Chosen Loop Type: Nested for loops

Nested for loops are required to handle the two-dimensional grid structure of the table. The outer loop iterates through the rows (1-10), and the inner loop iterates through the columns (1-10) for each row. This ensures every row time column combination is calculated exactly once.

Solution Description
The solution uses two nested for loops, both ranging from 1 to 10. F-string formatting with width specifiers (:3 for products and :2 for row numbers) is used extensively to align all products into perfect vertical columns, creating the required grid format.

---

AI Assistance Used

I used the Gemini AI assistant to:
* Confirm the logic and syntax for each challenge.
* Confrim the print statement ouputs matched the specified assignment output
* Structure the documentation and edit the wording for clarity.