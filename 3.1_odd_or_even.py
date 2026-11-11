"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a whole number N typed by the user
# 2. Process: for every number from 1 to N, test number % 2 and count odds and evens
# 3. Out: one line per number ("3 is odd") and a final count of odd and even
# 4. What happens on 0, on a negative number, on a very large number:
#    - 0 or negative: print a message and stop (nothing to list)
#    - above 100: refuse and print a message. My limit is 100 so the screen is not flooded with 5000 lines
#      is not flooded with 5000 lines.
#    - not a whole number (like "abc"): print a message and stop


# Your code below
MAX_N = 100

text = input("Enter a number N: ").strip()

try:
    n = int(text)
except ValueError:
    print("That is not a whole number.")
else:
    if n <= 0:
        print("N must be at least 1. Nothing to show.")
    elif n > MAX_N:
        print("N is too large. The maximum is", MAX_N)
    else:
        odd_count = 0
        even_count = 0
        for number in range(1, n + 1):
            if number % 2 == 0:
                print(number, "is even")
                even_count += 1
            else:
                print(number, "is odd")
                odd_count += 1
        print("Odd:", odd_count, "Even:", even_count)