#--------------------------------------------------Exercise 3-8: Seeing the World-----------------------
'''Store the locations in a list. Make sure the list is not in alphabetical order.
•	 Print your list in its original order. Don’t worry about printing the list neatly,
just print it as a raw Python list.
•	 Use sorted() to print your list in alphabetical order without modifying the
actual list.
•	 Show that your list is still in its original order by printing it.
•	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
•	 Show that your list is still in its original order by printing it again.
•	 Use reverse() to change the order of your list. Print the list to show that its
order has changed.
•	 Use reverse() to change the order of your list again. Print the list to show
it’s back to its original order.
•	 Use sort() to change your list so it’s stored in alphabetical order. Print the
list to show that its order has been changed.
•	 Use sort() to change your list so it’s stored in reverse alphabetical order.
Print the list to show that its order has changed.'''

# Step 1: Store the locations in a list
places = ["Tokyo", "Paris", "New York", "Sydney", "Cape Town"]

# Step 2: Print the list in its original order
print("Original list:", places)

# Step 3: Use sorted() to print the list in alphabetical order without modifying the original list
print("Alphabetical order:", sorted(places))

# Step 4: Show that the list is still in its original order by printing it
print("List after sorted():", places)

# Step 5: Use sorted() to print the list in reverse alphabetical order without changing the original list
print("Reverse alphabetical order:", sorted(places, reverse=True))

# Step 6: Show that the list is still in its original order by printing it again
print("List after reverse sorted():", places)

# Step 7: Use reverse() to change the order of the list
places.reverse()
print("List after reverse():", places)

# Step 8: Use reverse() to change the order of the list again
places.reverse()
print("List after second reverse():", places)

# Step 9: Use sort() to change the list so it’s stored in alphabetical order
places.sort()
print("List after sort():", places)

# Step 10: Use sort() to change the list so it’s stored in reverse alphabetical order
places.sort(reverse=True)
print("List after sort(reverse=True):", places)


#------------------------------------------------Exercise 3-9: Dinner ------------------------------------
#Working with one of the programs from Exercises 3-4 through 3-7 (page 42), use len() to print a message indicating the number of people you are inviting to dinner.

# List of people to invite to dinner
guests = ["Alice", "Bob", "Charlie", "Diana", "Edward"]

# Print the number of people invited to dinner
print(f"I am inviting {len(guests)} people to dinner.")




#-------------------------------------------------Exercise 3-10: Every Function-----------------------------------------
#Create a list of items (mountains, rivers, countries, cities, languages, etc.). Use each function introduced in the chapter at least once.

languages = ["Python", "JavaScript", "C++", "Ruby", "Java"]

# Print the original list
print("Original list:", languages)

# Access an element using index
print("First language:", languages[0])

# Modify an element
languages[0] = "Go"
print("Modified list:", languages)

# Append a new element
languages.append("Swift")
print("List after append:", languages)

# Insert an element at a specific position
languages.insert(2, "Rust")
print("List after insert:", languages)

# Remove an element by value
languages.remove("C++")
print("List after remove:", languages)

# Pop an element from the list
popped_language = languages.pop()
print("List after pop:", languages)
print("Popped language:", popped_language)

# Pop an element from a specific position
popped_language = languages.pop(1)
print("List after pop(1):", languages)
print("Popped language:", popped_language)

# Delete an element using del
del languages[2]
print("List after del:", languages)

# Use sorted() to print the list in alphabetical order without modifying the original list
print("Alphabetical order:", sorted(languages))

# Show that the list is still in its original order by printing it
print("List after sorted():", languages)

# Use sorted() to print the list in reverse alphabetical order without changing the original list
print("Reverse alphabetical order:", sorted(languages, reverse=True))

# Show that the list is still in its original order by printing it again
print("List after reverse sorted():", languages)

# Use reverse() to change the order of the list
languages.reverse()
print("List after reverse():", languages)

# Use reverse() to change the order of the list again
languages.reverse()
print("List after second reverse():", languages)

# Use sort() to change the list so it’s stored in alphabetical order
languages.sort()
print("List after sort():", languages)

# Use sort() to change the list so it’s stored in reverse alphabetical order
languages.sort(reverse=True)
print("List after sort(reverse=True):", languages)

# Check the length of the list
print("Length of the list:", len(languages))
