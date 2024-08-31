def calculate_area(name):
    # Convert the name to lowercase for case-insensitive comparison
    name = name.lower()
   
    # Check for the conditions and calculate the area accordingly
    if name == "rectangle":
        l = int(input("Enter rectangle's length: "))
        b = int(input("Enter rectangle's breadth: "))
        # Calculate area of rectangle
        rect_area = l * b
        print(f"The area of the rectangle is {rect_area}.")
   
    elif name == "square":
        s = int(input("Enter square's side length: "))
        # Calculate area of square
        sqt_area = s * s
        print(f"The area of the square is {sqt_area}.")
 
    elif name == "triangle":
        h = int(input("Enter triangle's height length: "))
        b = int(input("Enter triangle's base length: "))
        # Calculate area of triangle
        tri_area = 0.5 * b * h
        print(f"The area of the triangle is {tri_area}.")
 
    elif name == "circle":
        r = int(input("Enter circle's radius length: "))
        pi = 3.14
        # Calculate area of circle
        circ_area = pi * r * r
        print(f"The area of the circle is {circ_area}.")
         
    elif name == 'parallelogram':
        b = int(input("Enter parallelogram's base length: "))
        h = int(input("Enter parallelogram's height length: "))
        # Calculate area of parallelogram
        para_area = b * h
        print(f"The area of the parallelogram is {para_area}.")
     
    else:
        print("Sorry! This shape is not available.")
 
# Driver code
if __name__ == "__main__":
    print("Calculate Shape Area")
    shape_name = input("Enter the name of the shape whose area you want to find: ")
    # Function call
    calculate_area(shape_name)
     
   
