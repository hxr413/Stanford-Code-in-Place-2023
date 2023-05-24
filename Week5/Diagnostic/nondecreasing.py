def main():
    # TODO write your solution here
    print("Enter a sequence of non-decreasing numbers.")
    
    counter = 1
    num1 = float(input("Enter num: "))
    num2 = float(input("Enter num: "))
    
    while (num1 <= num2):
        num1 = num2
        num2 = float(input("Enter num: "))
        counter += 1
    
    print("Thanks for playing!")
    print("Sequence length:", counter)

    
if __name__ == "__main__":
    main()
