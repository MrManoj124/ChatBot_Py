print("Welcome to play the Quiz game")

playing=input("Do you want to play the game : ")
if playing.lower() != "yes":
    quit()
    
print("Let's play the game ")
score=0

answer=input("What does it mean by CPU ")
if answer.lower() == "Central processing unit":
    print('your answer is correct ')
    score += 1
else:
    print("Please enter the correct answer")

answer=input("What does it mean by PSU ")
if answer.lower() == "Power Supply unit":
    print("You're answered correctly ")
    score+=1
else:
    print("Please enter the correct answer")

answer=input("What does it mean by GPU ")
if answer.lower() == "Graphical processing unit":
    print("You're answered correctly ")
    score+=1
else:
    print("Please enter the correct answer")


answer=input("What does it mean by CLI")
if answer.lower() == "Command Line Interface":
    print("You're answered correctly ")
    score+=1
else:
    print("Please enter the correct answer")

print("You're got " + str(score) + "of question")
print("You're got " + str((score/4)*100) + "%.")
