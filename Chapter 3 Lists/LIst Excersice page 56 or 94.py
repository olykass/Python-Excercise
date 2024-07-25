#----------------------------Excercise 4-1. Pizza in my case wot
'''
Think of at least three kinds of your favorite pizza. Store these
pizza names in a list, and then use a for loop to print the name of each pizza.
•	 Modify your for loop to print a sentence using the name of the pizza
instead of printing just the name of the pizza. For each pizza you should
have one line of output containing a simple statement like I like pepperoni
pizza.
•	 Add a line at the end of your program, outside the for loop, that states
how much you like pizza. The output should consist of three or more lines
about the kinds of pizza you like and then an additional sentence, such as
I really love pizza!'''

# List of favorite wot
wots = ['Doro Wot', 'Misir Wot', 'Siga Wot']

# Print each wot name
for wot in wots:
    print(wot)

# Print statements about each wot
for wot in wots:
    print(f"I like {wot}.")

# Additional statement about how much you like wot
print("\nI really love wot!")
print("Doro Wot is my favorite because of its rich flavor and spicy kick.")
print("Misir Wot is fantastic for a hearty and nutritious meal.")
print("Siga Wot is perfect for those who enjoy a savory beef stew.")



#--------------------------Excercise 4-2. Animals
'''Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to
print out the name of each animal.
•	 Modify your program to print a statement about each animal, such as
A dog would make a great pet.
•	 Add a line at the end of your program stating what these animals have in
common. You could print a sentence such as Any of these animals would
make a great pet!'''


# List of animals with a common characteristic
animals = ['dog', 'cat', 'rabbit']

# Print each animal's name
for animal in animals:
    print(animal)

# Print statements about each animal
for animal in animals:
    print(f"A {animal} would make a great pet.")

# Additional statement about what these animals have in common
print("\nAny of these animals would make a great pet!")
print("They are all known for their companionship and friendly nature.")
print("Each of these animals can bring joy and comfort to a home.")
