Calculating Distance Between Two Points Using Math and I/O Libraries

Description
- My program helps calculate the distance between two points using the Math library.

How to Run
- Open the program.
- Run the program.
- Use sqrt() and pow() from the Math library
- Input the two points (x1, y1) and (x2, y2)

Input Needed
- Enter x1: 2
- Enter y1: 3
- Enter x2: 7
- Enter y2: 8

Sample Output
   
    import math

    X1 = float(input("Enter coordinate: X"))
    Y1 = float(input("Enter coordinate: Y"))
    X2 = float(input("Enter coordinate: X"))
    Y2 = float(input("Enter coordinate: Y"))
    distance = math.sqrt(math.pow(X1 - X2, 2) + math.pow(Y2 - Y1, 2))
    print(f"The Distance between the coordinate is, {distance:.2f}")

Author
- Name: Padilla, Carlene Aisha S.
- Section: 8 - Acacia

