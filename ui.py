import words , time

def loadingbar(total=50) -> None :
    for i in range(total + 1):
        percent = int((i / total) * 100)
        filled = int(30 * i // total)
        bar = '█' * filled + '-' * (30 - filled)
    
        print(f"\033[H\033[JLoading: |{bar}| {percent}% complete")
        time.sleep(0.05)

def main(life) -> bool :
    print("\033[H\033[J" , end = "" )
    print(r"""    __  __                                            
   / / / /____ _ ____   ____ _ ____ ___   ____ _ ____ 
  / /_/ // __ `// __ \ / __ `// __ `__ \ / __ `// __ \
 / __  // /_/ // / / // /_/ // / / / / // /_/ // / / /
/_/ /_/ \__,_//_/ /_/ \__, //_/ /_/ /_/ \__,_//_/ /_/ 
                     /____/                           
           ______                                             
          / ____/____ _ ____ ___   ___                        
         / / __ / __ `// __ `__ \ / _ \                       
        / /_/ // /_/ // / / / / //  __/                       
        \____/ \__,_//_/ /_/ /_/ \___|                        
""" , end = "\n")
    print(f"                   STAGE {7 - life} ")
    words.acsvread()
    words.asciiartshow(life)
    return False

if __name__ == "__main__" :
    ...
    #print("\033[H\033[J") = to make cursor at home and clear entire screen