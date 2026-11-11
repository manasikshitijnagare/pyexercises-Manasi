"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the list from exercise 4.0 (the list below is a PLACEHOLDER, replace it with the exact list from my 4.0 file)
# 2. Process: build four different orders, always on copies, never on the original
# 3. Out: the four orders, then the original list again
# 4. My four orders, and which ones modify the original:
#    a) sorted(original)               -> returns a NEW list, original unchanged
#    b) sorted(original, reverse=True) -> returns a NEW list, original unchanged
#    c) original[::-1]                 -> slice makes a NEW list, original unchanged
#    d) copy.sort(key=len)             -> .sort() changes the list IN PLACE (and
#       returns None), so I only use it on a copy made with original.copy()
#    Rule: sorted() and slicing copy. .sort() and .reverse() modify.


# Your code below
original = ["Summer Sale", "Black Friday", "Spring Launch", "Back to School", "Christmas"]
snapshot = original.copy()  # reference copy to compare with at the end

alphabetical = sorted(original)
reverse_alphabetical = sorted(original, reverse=True)
reversed_order = original[::-1]

by_length = original.copy()
by_length.sort(key=len)  # in place, but only on the copy

print("Alphabetical         :", alphabetical)
print("Reverse alphabetical :", reverse_alphabetical)
print("Reversed order       :", reversed_order)
print("By length (copy)     :", by_length)
print("Original list        :", original)

# CHECK: the original must be identical to my 4.0 list
if original == snapshot:
    print("OK: the original list is unchanged.")
else:
    print("ERROR: the original list was modified!")