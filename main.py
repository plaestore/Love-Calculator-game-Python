print("Welcome to the Love Calculator!")

# Get both names from the users
name1 = input("What is your name? \n")
name2 = input("What is your name? \n")

# Combine both names and convert everything to lowercase
combined_name = name1 + name2
to_lowercase = combined_name.lower()

# Count the letters in "TRUE"
t = to_lowercase.count("t")
r = to_lowercase.count("r")
u = to_lowercase.count("u")
e = to_lowercase.count("e")

# Add the TRUE letter counts together
true_score = t + r + u + e

# Count the letters in "LOVE"
l = to_lowercase.count("l")
o = to_lowercase.count("o")
v = to_lowercase.count("v")
e = to_lowercase.count("e")

# Add the LOVE letter counts together
love_score = l + o + v + e

# Combine both scores to get the final love score
final_score = true_score + love_score

# Determine the message based on the score
if final_score < 10 or final_score > 90:
    print(f"Your score is {final_score}, you go together like coke and mentos.")

elif 40 <= final_score <= 50:
    print(f"Your score is {final_score}, you are alright together.")

else:
    print(f"Your score is {final_score}")