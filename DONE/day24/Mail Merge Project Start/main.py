#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

# placeholder = 
with open(r"F:\1JOURNEY_TO-INTERNSHIP\CODES\Mail Merge Project Start\Input\Names\invited_names.txt") as f:
    names = f.readlines()

with open(r"F:\1JOURNEY_TO-INTERNSHIP\CODES\Mail Merge Project Start\Input\Letters\starting_letter.txt"  ) as letter:
    letter_content = letter.read()
    for name in names:
        stripped_name = name.strip()
        new = letter_content.replace("[name]" ,stripped_name )
        with open(f"F:\\1JOURNEY_TO-INTERNSHIP\\CODES\\Mail Merge Project Start\\Output\\ReadyToSend\\{stripped_name}.txt" , "w") as new_letter:
            new_letter.write(new)