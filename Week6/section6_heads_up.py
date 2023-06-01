import random

# Name of the file to read in!
FILE_NAME = 'cswords.txt'

def get_words_from_file():
    """
    This function has been implemented for you. It opens a file, 
    and stores all of the lines into a list of strings. 
    It returns a list of all lines in the file. 
    """
    f = open(FILE_NAME)
    lines = []
    for line in f:
        # removes whitespace characters (\n) from the start and end of the line
        line = line.strip() 
        # if the line was only whitespace characters, skip it 
        if line != "":
            lines.append(line)
    return lines

  
def generate_word(lines, max_index):
    index = random.randint(0, max_index)
    print(lines[index])

    
def main():
    # your code here :) 
    lines = get_words_from_file()
    max_index = len(lines) - 1
    generate_word(lines, max_index)
    
    while True:
        user_input = input("Press Enter to continue.")
        if user_input == '':
            generate_word(lines, max_index)
    

if __name__ == '__main__':
    main()
