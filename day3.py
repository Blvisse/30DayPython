#Papa Blaise
#Program to split a into two parts

#get user input
userInput=input("Input Split number: ")
userInput=int(userInput)

#create a list
userList=['a','b','c','d','e','f','g','h','i','k']
secondList=[]

toPop=userList[:userInput]
finishedList=userList[userInput:]
# for i in range(userInput):
#     secondList.insert(i,toPop[i])
#     del userList[toPop[i]]
   
print(toPop,finishedList)