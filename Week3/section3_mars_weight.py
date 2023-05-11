"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

# Gravitational constants for MARS compared to Earth's gravity
MARS = 0.378

def main():
    weight = float(input("Enter a weight on Earth: "))
    new_weight = round(weight * MARS, 2)
    print("The equivalent weight on Mars:", new_weight)


if __name__ == "__main__":
    main()
