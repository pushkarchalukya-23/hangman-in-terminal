import words , time

def loadingbar(total=50) -> None :
    for i in range(total + 1):
        percent = int((i / total) * 100)
        filled = int(30 * i // total)
        bar = '█' * filled + '-' * (30 - filled)
    
        print(f"\033[H\033[JLoading: |{bar}| {percent}% complete")
        time.sleep(0.05)

def main(life) -> bool :

    words.wcsvread()
    word : str = words.choose()
    gletters : str = []

    hword : str = words.hworder( word , gletters )

    print("\033[H\033[J" , end = "" )
    print("""    __  __                                            
   / / / /____ _ ____   ____ _ ____ ___   ____ _ ____ 
  / /_/ // __ `// __ \\ / __ `// __ `__ \\ / __ `// __ \\
 / __  // /_/ // / / // /_/ // / / / / // /_/ // / / /
/_/ /_/ \\__,_//_/ /_/ \\__, //_/ /_/ /_/ \\__,_//_/ /_/ 
                     /____/                           
           ______                                     
          / ____/____ _ ____ ___   ___                
         / / __ / __ `// __ `__ \\ / _ \\               
        / /_/ // /_/ // / / / / //  __/               
        \\____/ \\__,_//_/ /_/ /_/ \\___|                """ , end = "\n\n")
    
    print(f"                   \033[1m [ STAGE {7 - life} ] \033[0m")

    words.acsvread()
    words.asciiartshow(life)

    print(f"\033[{14};{33}H Word = {hword}")
    letter = input(f"\033[{15};{28}H Guess Letters : ")
    if letter in word :
        gletters.append(f"\033[32m\033[1mletter\033[0m")
    else :
        gletters.append(f"\033[31m\033[1mletter\033[0m")
    print(gletters)
    print(f"\033[{16};{28}HGuessed : ")
    for _ in gletters : 
       print(f"{_}" , end=" ")

    return False

if __name__ == "__main__" :
    main(6)
    #print("\033[H\033[J") = to make cursor at home and clear entire screen