date = input("enter date ")
name = input("enter name ")
letter = """hey <|name|>
YOU are selected!
<|date|>
"""

letter = letter.replace("<|name|>", name)
letter = letter.replace("<|date|>", date)
print(letter)
