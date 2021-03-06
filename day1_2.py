#get user input
userInput=input("Input integers separated by spaces: \n")

userList=[]
#convert input to list
numbers=userInput.split(" ")
for i in numbers:
    numberConvert=int(i)
    userList.append(numberConvert)
    
print(len(userList))

#create a function that counts the number of elements in a list
def listCounter(userlist):
    counter=0;
    for i in userList:
        counter+=1
    return counter
#call function
print("The number of elements of the list is : ",listCounter(userList))

