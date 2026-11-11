"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:a list of 11 numbers written in the code (no typing by the user)
# 2. Process:show the list, pick items, sort a copy, remove the last item from each list, and compute the total and the average
# 3. Out: the whole list, the 2nd and 5th items, the sorted list, the removed items, the lists after removal, the total and the average
# 4. What my list is about, and what I computed from it: My list is the number of leads each marketing campaign brought in (one number per campaign). CHANGE this sentence if your numbers mean something else.
#    I computed the total and the average. The average is interesting because it shows what a "normal" campaign brings, so I can see which campaigns are below or above it.


# Your code below
numbers = [3, 5, 7, 9, 26, 34, 21, 13, 16, 20, 30]
print("The whole list is: ", numbers)
print("The second item of the list is: ", numbers[1])
print("The fifth item of the list is: ", numbers[4])
 
sorted_numbers = sorted(numbers)
print("The sorted list is: ", sorted_numbers)
 
removed_number = numbers.pop()
print("The removed item is: ", removed_number)
print("The list after removing the last item is : ", numbers)
print("The sorted list after removing the last item is : ", sorted_numbers)
removed_number_last = sorted_numbers.pop()
print("The removed item from the sorted list is : ", removed_number_last)
print("The sorted list after removing the last item is : ", sorted_numbers)
 
# Something computed from the list (on the list after the removals above)
total = sum(numbers)
average = total / len(numbers)
print("The total of the list is: ", total)
print("The average of the list is: ", round(average, 1))