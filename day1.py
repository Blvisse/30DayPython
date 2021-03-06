def checkNumbers(startPoint,endPoint):
    for i in range(startPoint,endPoint+1):
        if i %2==0 and i%3!=0:
            print(i,end=",")

#get user input 
userInput=input("Input start and end points of the numbers")
points=userInput.split(" ")
startPoint=int(points[0])
endPoint=int(points[1])

checkNumbers(startPoint,endPoint)