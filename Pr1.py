#Quiz game
print("Welcome to new quiz game")
playing=input("Do you want to play : ")
if playing != "yes":
    quit()
print("okey Let's play the game ")
score = 0

answer=input("What does CPU Mean for ")
if answer.lower()=="Central Procesing Unit":
    print("Correct Answer!")
    score += 1

else:
    print("Incorrect Answer !")


answer=input("What does PSU Mean for ")
if answer.lower()=="Power Supply Unit":
    print("Correct Answer!")
    score += 1

else:
    print("Incorrect Answer !")

answer=input("What does GPU Mean for ")
if answer.lower()=="Graphical Procesing Unit":
    print("Correct Answer!")
    score += 1

else:
    print("Incorrect Answer !")

answer=input("What does CLI Mean for ")
if answer.lower()=="Command Line Interface":
    print("Correct Answer!")
    score += 1

else:
    print("Incorrect Answer !")

print("You got " + str(score) + "of 4 quetions")
print("You got " + str((score / 4) * 100) + "%")