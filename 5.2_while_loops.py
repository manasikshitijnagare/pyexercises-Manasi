"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the user's answers to "Do you confirm? (yes/no)"
# 2. Process: clean each answer (strip + lower), store it, and repeat until the answer is "yes" or the attempt limit is reached
# 3. Out: a message saying if it was confirmed, then a summary
# 4. My stop condition, my attempt limit, my summary:
#    - Stop condition: the cleaned answer equals "yes"
#    - Attempt limit: 5. When it is reached the program gives up and says so.
#    - "Yes", "yes" and " YES " all count as yes, because I use strip() and
#      lower() before comparing (my decision).
#    - Summary: attempts used, outcome, and the list of answers given


# Your code below
MAX_ATTEMPTS = 5

attempts = 0
answers = []
confirmed = False

while attempts < MAX_ATTEMPTS and not confirmed:
    raw = input("Do you confirm? (yes/no): ")
    attempts += 1
    answers.append(raw)
    if raw.strip().lower() == "yes":
        confirmed = True
    else:
        print("Not confirmed. Attempts left:", MAX_ATTEMPTS - attempts)

if confirmed:
    print("Confirmed.")
else:
    print("Maximum of", MAX_ATTEMPTS, "attempts reached. Giving up.")

print("--- Summary ---")
print("Attempts used:", attempts)
if confirmed:
    print("Outcome: confirmed")
else:
    print("Outcome: not confirmed")
print("Answers given:", answers)

# CHECK: never answering "yes" -> stops after exactly 5 attempts
# Answering "  YES " -> accepted