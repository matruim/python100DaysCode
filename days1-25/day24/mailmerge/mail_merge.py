with open("Input/Names/invited_names.txt") as name_file:
    with open("Input/Letters/starting_letter.txt") as letter_file:
        letter = letter_file.read()
        for name in name_file:
            complete_letter = letter.replace("[name]", name.rstrip())
            with open(f"Output/ReadyToSend/letter_for_{name.rstrip().replace(' ', '_')}.txt", mode="w") as output_letter:
                output_letter.write(complete_letter)
