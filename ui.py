import time

def loadingbar(total=50) -> None :
    for i in range(total + 1):
        percent = int((i / total) * 100)
        filled = int(30 * i // total)
        bar = '█' * filled + '-' * (30 - filled)
    
        print(f"\033[H\033[JLoading: |{bar}| {percent}% complete")
        time.sleep(0.05)

def main() -> bool :
    print("done")
    return False

if __name__ == "__main__" :
    ...
    #print("\033[H\033[J") = to make cursor at home and clear entire screen