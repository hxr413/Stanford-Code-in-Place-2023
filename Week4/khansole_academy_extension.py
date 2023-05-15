import random

def main():
    print("Khansole Academy")
    counter = 0
    
    while (counter < 3):
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        print("What is " + str(num1) + " + " + str(num2) + "?" )
        
        true_answer = num1 + num2
        user_answer = int(input("Your answer: "))
        
        if true_answer == user_answer:
            counter += 1
            print("Correct!")
            print("You've gotten", counter, "correct in a row. ")
        else:
            counter = 0
            print("Incorrect.")
            print("The expected answer is", true_answer)
    
    print("Congratulations! You mastered addition.")
    
if __name__ == '__main__':
    main()
