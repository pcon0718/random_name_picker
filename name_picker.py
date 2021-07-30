import random

# Empty list
names =[]

prompt = "Enter name you would like to add.\n"
prompt += "To end, type 'Done': "

# User Input
while True:
    entered_name = input(prompt)
    if entered_name.lower() == 'done':
        break
    # Add user input to list
    names.append(entered_name)

# Chose a name from the list
chosen_name = random.choice(names)

print(f"The random name chosen from the list is: {chosen_name.title()}")
