''' write a program to fill in a letter template given name and date.'''
from datetime import date


letter='''Dear<|name|>,
          you are selected!
          <|Date|>'''
name=input("Enter the name: ")
date=input("Enter the date: ")
letter=letter.replace("<|name|>",name)
letter=letter.replace("<|Date|>",date)

print(letter)