def main():
    # TODO write your solution here
    height = float(input("Enter your height in meters: "))
    
    if height >= 1.9:
        print("Above maximum astronaut height")
    elif height <= 1.6:
        print("Below minimum astronaut height")
    else:
        print("Correct height to be an astronaut")

        
if __name__ == "__main__":
    main()
