sentences=[]
userInputs=[]

while True:
    userInput=input()
    if userInput:
        userInputs.append(userInput)
        sentences.append(userInput.upper())
    else:
        break    

print(userInput)
print(sentences)
