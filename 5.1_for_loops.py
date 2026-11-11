"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the list from exercise 4.0 (the list below is a PLACEHOLDER, replace it
#    with the exact list from my 4.0 file)
# 2. Process: loop over every item with enumerate(), compute its length, and
#    compare it with a threshold
# 3. Out: exactly one line per item: position, item, length, long or short
# 4. What I compute for each item, and why it is worth showing:
#    The number of characters in the name, and whether it is "long" (more than
#    12 characters). The reader sees which names are too long for an email
#    subject or an ad title. The threshold of 12 is my own decision.


# Your code below
items = ["Summer Sale", "Black Friday", "Spring Launch", "Back to School", "Christmas"]

THRESHOLD = 12
lines_printed = 0

for position, item in enumerate(items, start=1):
    length = len(item)
    if length > THRESHOLD:
        verdict = "long"
    else:
        verdict = "short"
    print(position, item, "-", length, "characters -", verdict)
    lines_printed += 1

# CHECK: lines printed must equal the number of items
print("Lines printed:", lines_printed, "/ items in list:", len(items))
if lines_printed == len(items):
    print("OK: no off-by-one.")
else:
    print("ERROR: off-by-one!")