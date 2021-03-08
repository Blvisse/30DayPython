#Papap Blaise 
#A program that calculates the factorial of a given number
# Get user Input
userRange=input("Input number: ")
userRange=int(userRange)

#loop through the numbers within the range and calculate the range
product=1

for i in range(1,userRange+1):
    product=product*i


print(product)