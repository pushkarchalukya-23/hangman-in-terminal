import csv , random

#Choosing random word from the csv file and its hints
def wcsvread() -> str :
    with open(r"assets\hangman_words.csv" , "r") as file :
        reader = csv.reader(file)
        #Turns the CSV rows into a single list of words
        global data
        data = [row for row in reader]

def choose() -> str :
    return random.choice(data)

def acsvread() -> str :
    with open(r"assets\ascii_tree_stages.csv" , "r") as file :
        reader = csv.reader(file)
        #Turns the CSV rows into a single list of words
        global asciiart
        asciiart = [row for row in reader]

def asciiartshow(life) -> str :
    for i in asciiart[6 - life] :
        print(f"{i}", end="\n")

def hworder(word , gletters) -> str :
    ...

if __name__ == "__main__" :
    acsvread()
    asciiartshow(6)