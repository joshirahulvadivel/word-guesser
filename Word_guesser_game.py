
import random

print("Welcome to Word Guesser Game buddy")

print("Here are the word options to guess:")
print("ronaldo")
print("garnacho")
print("ramos")
print("beckham")
print("ozil")
print("Rodrygo")
print("casemiro")
print("mane")
print("kroos")
print("luka")


word_to_guess = random.choice(["ronaldo", "garnacho", "ramos", "beckham", "ozil", "rodrygo", "casemiro", "mane", "kroos", "luka"])

max_chances = 3

for chance in range(max_chances):
    user_input = input(f"This is your chance {chance + 1}: ")

    if user_input == word_to_guess:
        print("You have won!")
        break  # Corrected the break statement
    else:
        print("Incorrect guess. Try again.")

if user_input != word_to_guess:
    print(f"Sorry, you have used all {max_chances} chances. The correct word was: {word_to_guess}")
