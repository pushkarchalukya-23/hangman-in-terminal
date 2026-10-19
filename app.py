import words , ui

if __name__ == '__main__' :

    words.csvread()
    life : int = 5
    word : str = words.choose()
    gletters : str = []
    hword : str = []

    ui.loadingbar()
    while True :

        #breaks when returned False
        if not ui.main() :
            break
