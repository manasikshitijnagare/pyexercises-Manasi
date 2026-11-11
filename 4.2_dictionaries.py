"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the dictionary is written in the code; the user only types a field name to look up
# 2. Process: read one field, change two, remove one, then loop over the remaining fields
# 3. Out: the value read, every remaining field with its value, and the result of asking for a field that does not exist
# 4. My object, my five fields, and why those:
#     Object: a marketing campaign
#    - name       : to identify it in reports
#    - channel    : where it runs (email, social...), needed to compare results
#    - budget     : money allocated, the main constraint
#    - start_date : needed for planning and reporting periods
#    - status     : draft / running / finished, to know what needs action
#    - internal_note : sixth field, only there so I can remove it


# Your code below
campaign = {
    "name": "Spring Launch",
    "channel": "email",
    "budget": 5000,
    "start_date": "2026-03-01",
    "status": "draft",
    "internal_note": "waiting for design",
}

# Read
print("Campaign name:", campaign["name"])

# Change
campaign["status"] = "running"
campaign["budget"] = 6500

# Remove
campaign.pop("internal_note")

# Display every field with its value
for field, value in campaign.items():
    print(field + ":", value)

# CHECK: asking for a field that does not exist.
# With campaign["owner"] Python raises KeyError: 'owner' and the program crashes.
# To survive it I use .get() with a default value.
asked = input("Which field do you want to see? ").strip()
print(asked, "->", campaign.get(asked, "this field does not exist"))