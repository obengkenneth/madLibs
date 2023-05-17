# functions for the game
lol = lambda a: input("Enter a boy's name : ")
def food():
    ans = input("Enter the food : ")
    if ans.isalpha() == True:
        return ans
    else:
        print("Please enter a valid input")
        food()

def boy_name():
    ans = input("Enter a boy's name : ").title()
    if ans.isalpha() == True:
        return ans
    else:
        print("Please enter a valid input")
        return lol
def female_name():
    ans = input("Enter a female's name : ").title()
    if ans.isalpha() == True:
        return ans
    else:
        print("Please enter a valid input")
        female_name()

def utensil():
    ans = input("Enter an eating utensil : ")
    if ans.isalpha() == True:
        return ans
    else:
        print("Please enter a valid input")
        utensil()

# intro
print("*" * 50)
print("Hurray! You are about to play the MadLibs game!!")
print("*" * 50)

# instructions
print("In every bracket, fill in with an appropriate word as indicated in the brackets.")
print()

# loop to run the game
playAgain = "yes"
while playAgain == "yes":

    # story with options to be filled
    story = """At long last, the (food) was ready. (boy's name) rushed to the kitchen to get his 
(eating utensil). (Female Name) served him."""
    print(story)
    story = f"""At long last, the {food()} was ready. {boy_name()} rushed to the kitchen to get his 
{utensil()}. {female_name()} served him."""
    print(story)
    playAgain = input("Type yes to play again or no to quit the game : ").lower()

# end message
print("*" * 40)
print("\tThank you for playing.")
print("*" * 40)

