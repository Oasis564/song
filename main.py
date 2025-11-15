def opening_function():
    f = open("Believer.txt", 'r')
    data = f.read()
    print(data)
    f.close()

def characters_function():
    f = open("Believer.txt", 'r')
    data = f.read()
    length = len(data)
    print(length)
    
def word_function():
    f = open("Believer.txt", 'r')
    data = f.read()
    split = data.split()
    print(len(split))
    
def lowerletter_function():
    f = open("Believer.txt", 'r')
    data = f.read()
    print(data.lower())
    
def Slines_function():
    """
    step 1:
        read all the lines of a file as a list and store it in a variable.
    
    step 2: 
        loop through the list and check if the first letter is s.
        
    step 3:
        store the number of s found inside a variable.
        
    step 4:
        print the number of S's found.
    """
    f = open("Believer.txt", 'r')
    data = f.readlines()
    for i in range(72):
        if data[i][0].lower() == "s":
            print(data[i])
 

if __name__ == "__main__":
    # opening_function()
    # characters_function()
    # word_function()
    # lowerletter_function()
    Slines_function()
    # no_words_function()
    
