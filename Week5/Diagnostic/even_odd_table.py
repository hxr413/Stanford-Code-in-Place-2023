# print numbers from 1 up until MAX_NUMBER, inclusive
MAX_NUMBER = 100

def main():
    # TODO: your code here
    for i in range(MAX_NUMBER):
        if (i % 2 == 0):
            print(i+1, "is even")
        else:
            print(i+1, "is odd")

if __name__ == "__main__":
    main()
