# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
names = []

with open("./Input/Names/invited_names.txt", mode='r') as file:
    names = file.readlines()
with open("./Input/Letters/starting_letter.txt", mode='r') as starting_letter:
    s_letter = starting_letter.read()

print(s_letter)

for name in names:
    with open(f"./Output/ReadyToSend/{name}.txt", mode='w') as letter:

        f_letter = s_letter.replace("[name]", name.strip("\n"))
        letter.write(f_letter)
