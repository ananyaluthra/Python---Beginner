letter=''' Dear <|NAME|>,
Congrats you are selected!



Date:<|DATE|>
'''
name=input("Enter your name here: ")
date=input("Enter here today's date: ")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)
