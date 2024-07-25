#A)Objective: Create a list of people you’d like to invite to dinner and print an invitation message for each person.
# Initial guest list
guests = ['Albert Einstein', 'Marie Curie', 'Leonardo da Vinci']

# Sending out invitations
for guest in guests:
    print(f"Dear {guest}, I would like to invite you to dinner.")

# Output
# Dear Albert Einstein, I would like to invite you to dinner.
# Dear Marie Curie, I would like to invite you to dinner.
# Dear Leonardo da Vinci, I would like to invite you to dinner.

#B) Objective: Update the guest list because one person can’t attend and send out new invitations
# Initial guest list
guests = ['Albert Einstein', 'Marie Curie', 'Leonardo da Vinci']

# Notify the guest who can't make it
unable_to_attend = 'Leonardo da Vinci'
print(f"Unfortunately, {unable_to_attend} can't make it to the dinner.")

# Replace the guest who can't make it
guests.remove(unable_to_attend)
guests.append('Nikola Tesla')

# Send new invitations
for guest in guests:
    print(f"Dear {guest}, I would like to invite you to dinner.")

# Output
# Unfortunately, Leonardo da Vinci can't make it to the dinner.
# Dear Albert Einstein, I would like to invite you to dinner.
# Dear Marie Curie, I would like to invite you to dinner.
# Dear Nikola Tesla, I would like to invite you to dinner.

#C Objective: Add more guests to the list and print updated invitations.
# Initial guest list after changes from Exercise 3-5
guests = ['Albert Einstein', 'Marie Curie', 'Nikola Tesla']

# Inform about the bigger dinner table
print("Good news! I found a bigger dinner table.")

# Add more guests
guests.insert(0, 'Isaac Newton')          # Add to the beginning
guests.insert(2, 'Ada Lovelace')          # Add to the middle
guests.append('Alan Turing')              # Add to the end

# Print new invitations
for guest in guests:
    print(f"Dear {guest}, I would like to invite you to dinner.")

# Output
# Good news! I found a bigger dinner table.
# Dear Isaac Newton, I would like to invite you to dinner.
# Dear Albert Einstein, I would like to invite you to dinner.
# Dear Ada Lovelace, I would like to invite you to dinner.
# Dear Marie Curie, I would like to invite you to dinner.
# Dear Nikola Tesla, I would like to invite you to dinner.
# Dear Alan Turing, I would like to invite you to dinner.

#D) Objective: Reduce the guest list to only two people and notify those who can’t be invited.
# Initial guest list after changes from Exercise 3-6
guests = ['Isaac Newton', 'Albert Einstein', 'Ada Lovelace', 'Marie Curie', 'Nikola Tesla', 'Alan Turing']

# Notify about the limited space
print("Due to limited space, I can only invite two people to dinner.")

# Remove guests until only two remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, I can no longer invite you to dinner.")

# Notify the remaining guests
for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner.")

# Remove the last two guests
del guests[:]
print("Final guest list:", guests)  # Output should be an empty list

# Output
# Due to limited space, I can only invite two people to dinner.
# Sorry Alan Turing, I can no longer invite you to dinner.
# Sorry Nikola Tesla, I can no longer invite you to dinner.
# Sorry Marie Curie, I can no longer invite you to dinner.
# Sorry Ada Lovelace, I can no longer invite you to dinner.
# Sorry Albert Einstein, I can no longer invite you to dinner.
# Dear Isaac Newton, you are still invited to dinner.
# Dear Albert Einstein, you are still invited to dinner.
# Final guest list: []
