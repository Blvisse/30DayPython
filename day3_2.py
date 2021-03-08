#Papa Blaise 
#program to find the highest n-values in a dictionary

#user input
userInput=input("Input Threshold: ")
userInput=int(userInput)

userDict={'a':500,'b':5874,'c':560,'d':400,'e':5000,'f':20}
def max_n(dicty,thresh):
    dictValues=[]
    for i in dicty.values():
        
        dictValues.append(i)
    dictValues.sort(reverse=True)

    return (dictValues[:thresh])

print(max_n(userDict,userInput))