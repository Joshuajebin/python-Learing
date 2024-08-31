import math

def calculate_square_root_of_rectangle_area(length, width):
    # Calculate the area of the rectangle
    area = length * width
    # Calculate the square root of the area
    square_root = math.sqrt(area)
    return square_root

def main():
    # Input length and width
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    
    # Calculate the square root of the area
    result = calculate_square_root_of_rectangle_area(length, width)
    
    # Display the result
    print(f"The square root of the area of the rectangle is: {result:.2f}")

if __name__ == "__main__":
    main()
