import words , ui

if __name__ == '__main__' :

    words.wcsvread()
    life : int = 6    #[1-6]
    word : str = words.choose()
    gletters : str = []
    hword : str = []

    ui.loadingbar()
    while True :

        #breaks when returned False
        if not ui.main(life) :
            break
