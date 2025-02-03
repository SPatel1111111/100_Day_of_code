#Udemy day24
PLACEHOLDER = "[name]"

with open("D:/SNEHA1/100_Day_of_code/22_1_DAY_14/mail_merge/input/Names/invited_name.txt") as name_file:
    names = name_file.readlines()
    print(names)

with open("D:/SNEHA1/100_Day_of_code/22_1_DAY_14/mail_merge/input/Letters/starting_letter.docs") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        print(new_letter)
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.docs", mode="w") as letter:
            letter1 = letter.write(new_letter)
