import math

def calculate_square_root_of_triangle_area(base, height):
    # Calculate the area of the triangle
    area = 0.5 * base * height
    # Calculate the square root of the area
    square_root = math.sqrt(area)
    return square_root

def calculate_square_root_of_triangle_area_heron(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    # Calculate the square root of the area
    square_root = math.sqrt(area)
    return square_root

def main():
    #choice = input("Choose the method (1 for base and height, 2 for Heron's formula): ")
    
    
        # Input base and height
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        # Calculate the square root of the area
        result = calculate_square_root_of_triangle_area(base, height)
    
  #  elif choice == '2':
        # Input the sides of the triangle
        a = float(input("Enter the length of side a: "))
        b = float(input("Enter the length of side b: "))
        c = float(input("Enter the length of side c: "))
        # Check if the sides form a valid triangle
        if a + b > c and a + c > b and b + c > a:
            # Calculate the square root of the area using Heron's formula
            result = calculate_square_root_of_triangle_area_heron(a, b, c)
        else:
            print("The given sides do not form a valid triangle.")
            return
    
    
        
        
    
    # Display the result
    print("the value")

if __name__ == "__main__":
    main()

