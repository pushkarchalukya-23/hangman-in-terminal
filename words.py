import csv , random

#Choosing random word from the csv file and its hints
def csvread() -> str :
    with open(r"assets\hangman_words.csv" , "r") as file:
        reader = csv.reader(file)
        #Turns the CSV rows into a single list of words
        global data
        data = [row for row in reader]

def choose() -> str :
    return random.choice(data)

if __name__ == "__main__" :
    ...