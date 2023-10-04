with open("Input/Names/invited_names.txt", "r") as names:
    for i in range(8):
        name = names.__next__()
        name = name.strip()
        with open("Input/Letters/starting_letter.txt", "r") as letters:
            contents = letters.read()
        contents = contents.replace("[name]", name)
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as send:
            send.write(contents)
