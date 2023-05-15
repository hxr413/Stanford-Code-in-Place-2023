import random

def main():
    print("Khansole Academy")
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    print("What is " + str(num1) + " + " + str(num2) + "?" )
    true_answer = num1 + num2
    user_answer = int(input("Your answer: "))
    if true_answer == user_answer:
        print("Correct!")
    else:
        print("Incorrect.")
        print("The expected answer is", true_answer)
    
if __name__ == '__main__':
    main()
