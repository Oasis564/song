def opening_function():
    f = open("Heatwave.txt", 'r')
    data = f.read()
    print(data)
    f.close()


def characters_function():
    f = open("Heatwave.txt", 'r')
    data = f.read()
    length = len(data)
    print("Total characters:", length)


def word_function():
    f = open("Heatwave.txt", 'r')
    data = f.read()
    split = data.split()
    print("Total words:", len(split))


def lowerletter_function():
    f = open("Heatwave.txt", 'r')
    data = f.read()
    print(data.lower())


def search_operations():
    """
    Perform multiple search operations using if conditions.
    You can customize the search terms.
    """
    f = open("Heatwave.txt", 'r')
    data = f.read().lower()

    # Example searches
    word1 = "heat"
    word2 = "waves"
    word3 = "glass"

    if word1 in data:
        print(f"'{word1}' found in the song.")

    if word2 in data:
        print(f"'{word2}' found in the song.")

    if word3 in data:
        print(f"'{word3}' found in the song.")

    if "midnight" in data:
        print("'midnight' found in the song.")
    else:
        print("'midnight' NOT found in the song.")


def Slines_function():
    """
    Reads lines and prints those starting with 's'.
    """
    f = open("Heatwave.txt", 'r')
    lines = f.readlines()

    count_s = 0
    for line in lines:
        if len(line) > 0 and line[0].lower() == "s":
            print(line.strip())
            count_s += 1

    print("Total lines starting with 's':", count_s)


def no_words_function():
    f = open("Heatwave.txt", 'r')
    data = f.read()
    split = data.split()
    print("Word count:", len(split))


if __name__ == "__main__":
    opening_function()
    characters_function()
    word_function()
    lowerletter_function()
    Slines_function()
    no_words_function()
    search_operations()
