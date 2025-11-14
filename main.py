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

if __name__ == "__main__":
    opening_function()
    characters_function()
    word_function()
    # lowerletter_function()
    # Slines_function()
    # no_words_function()
    
