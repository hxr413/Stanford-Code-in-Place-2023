"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.

Note that the user should type in a planet with 
the first letter as uppercase, and you do not need
to handle the case where a user types in something 
other than one of the planets (that is not Earth). 
"""

# Gravitational constants for each planet compared to Earth's gravity
MERCURY = 0.376
VENUS = 0.89
MARS = 0.378
JUPITER = 2.36
SATURN = 1.081
URANUS = 0.82
NEPTUNE = 1.14

def main():
    weight = float(input("Enter a weight on Earth: "))
    planet = input("Enter a planet: ")
    
    if planet == "Mercury":
        new_weight = weight * MERCURY
    if planet == "Venus":
        new_weight = weight * VENUS
    if planet == "Mars":
        new_weight = weight * MARS
    if planet == "Jupiter":
        new_weight = weight * JUPITER    
    if planet == "Saturn":
        new_weight = weight * SATURN
    if planet == "Uranus":
        new_weight = weight * URANUS
    if planet == "Neptune":
        new_weight = weight * NEPTUNE
    
    new_weight = round(new_weight, 2)
    
    print("The equivalent weight on", planet, ":", new_weight)


if __name__ == "__main__":
    main()
