#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".


with open("./Input/Names/invited_names.txt", 'r') as names:
    list_names = names.readlines()


with open("./Input/Letters/starting_letter.txt", 'r') as letter:
    blueprint_letter = letter.read()


for name in list_names:
    stripped_name = name.strip()
    latter = blueprint_letter.replace('[name]', stripped_name)
    with open(f'./Output/ReadyToSend/invite_for_{stripped_name}.txt', 'w') as completed_letters:
        completed_letters.write(latter)
