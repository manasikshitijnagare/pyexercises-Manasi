"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:a sentence typed by the user
# 2. Process:four different string methods are applied to the same sentence
# 3. Out:the original (between brackets so spaces are visible) and the four results
# 4. My four transformations, and when each is useful:
#    a) strip()  -> cleaning what a user typed before saving or comparing it
#    b) title()  -> showing a name or a headline nicely
#    c) lower() + replace(" ", "-") -> making a URL slug or a file name
#    d) upper()  -> an alert or banner message that must stand out


# Your code below
sentence = input("Type a sentence: ")

stripped = sentence.strip()
titled = stripped.title()
slug = stripped.lower().replace(" ", "-")
shouting = stripped.upper()

print("Original  : [" + sentence + "]")
print("1. strip  : [" + stripped + "]")
print("2. title  : [" + titled + "]")
print("3. slug   : [" + slug + "]")
print("4. upper  : [" + shouting + "]")