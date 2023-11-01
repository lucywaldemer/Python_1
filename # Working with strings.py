# Working with strings
print("Giraffe Academy")
print("\"")

#set it at a variable
phrase = "This is a phrase"
print(phrase + " that says hello.")

# can do case changes and booleans for isupper or islower
print(phrase.lower())
print(phrase.upper())
print(phrase.upper().isupper())

# len is the length function
print(len(phrase))

# individual characters, index starts at 0
print(phrase[11])

# index funtion
print(phrase.index("a"))

# replace function
print(phrase.replace("phrase", "elephant"))
