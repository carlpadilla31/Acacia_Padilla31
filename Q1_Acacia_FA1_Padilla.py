import math #To make the math library functions work (pow. and sqrt.)

#Coordinates
X1 = float(input("Enter coordinate: X")) 
Y1 = float(input("Enter coordinate: Y"))
X2 = float(input("Enter coordinate: X"))
Y2 = float(input("Enter coordinate: Y"))

distance = math.sqrt(math.pow(X1 - X2, 2) + math.pow(Y2 - Y1, 2)) # Equation of the answer 

print(f"The Distance between the coordinate is, {distance:.2f}") #Round off to the nearest 2 decimals

#reflection
#Using a library is more practical than writing all calculations from scratch because it will make coding work faster. 
#It will also make it more easier because it will serve as an extra help for us.
#Like in our activity we didn't write the code from scratch instead we used the Math library as a guide and it made our coding process shorter.
