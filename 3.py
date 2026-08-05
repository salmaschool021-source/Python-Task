import random
print("Welcome Player")
print("I'm thinking of a number between 1 and 100.")
print("You have 6 attempts to guess it.")
x=random.randint(1,100)
rp=0
rw=0
s=0
u1=x-5
u2=x+5
r="y"
m=1
while (r!="n"):
    for i in range(1,8):
        if(i<=6):
          print(f"Attempt {i}/6")
          g=int(input("Enter your guess: "))
          if(g<u1):
             print("Too low")
          elif(g>u2):
             print("Too high")
          elif(g>=u1 and g<x):
             print("Higher")
          elif(g<=u2 and g>x):
             print("Lower")
          elif(g==x):
             print("Congratulations!")
             print("You guessed the number")
             rw+=1  
             rp+=1
             if(i!=6):
                 print(f"Guesses remaining: {6-i}")  
                 m=6-i+1
                 print(f"Multiplier: x{m}")
                 s=s+1*m
                 print(f"Points earned: {s}")  
             else:
                 s=s+1
                 print(f"Points earned: {s}")  
             break
        else:
          print(f"Hard luck")
          print(f"the number is {x}")
          rp+=1
    r=input("Play another round? (y/n): ")
print(f"Rounds Played: {rp}")
print(f"Rounds Won: {rw}")
print(f"Final Score: {s}")