print("INDIAN MOM ASKING FOR YOUR GRADE")
print("What are your grades son?")
mark1=int(input("Math enter here: "))
mark2=int(input("Science enter here: "))
mark3=int(input("History enter here: "))
mark4=int(input("ELA enter here: "))
mark5=int(input("Spanish enter here: "))
tot=mark1+mark2+mark3+mark4+mark5
avg=int(tot/5)
validrange= range(0,100)
if avg not in validrange:
    print("Invalid enter again")
elif avg in range(91,100):
    print("You got an A/Average, give me 101 percent")
elif avg in range(81,91):
    print("You got an B/You might get Bullied")
elif avg in range(71,81):
    print("You got an C/Cry because my slipper will hit you")
elif avg in range(61,71):
    print("You got an D/Don't come near me or th house or I will turn your face into a samosa")
else:
    print("You failed/Adoption begins now Failure")