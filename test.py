print('\033[0mNormal Text')
print('\033[1mBold Text\033[0m')
print('\033[2mDim Text\033[0m')
print('\033[3mItalic Text\033[0m')
print('\033[4mUnderlined\033[0m')
print('\033[5mBlinking\033[0m')
print('\033[7mInverted Colors\033[0m')
print('\033[8mHidden Text\033[0m')
print('\033[9mStrikethrough\033[0m')

class Terminal:
    # SGR Styles
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"
    
    # Foreground Colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    
    # TrueColor Helper
    @staticmethod
    def rgb(r, g, b, text):
        return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

    @classmethod
    def success(cls, msg):
        print(f"{cls.GREEN}[✔] {cls.BOLD}{msg}{cls.RESET}")

    @classmethod
    def error(cls, msg):
        print(f"{cls.RED}[✖] {cls.BOLD}{msg}{cls.RESET}")

    @classmethod
    def warning(cls, msg):
        print(f"{cls.YELLOW}[!] {msg}{cls.RESET}")

    @staticmethod
    def clear():
        print("\033[2J\033[H", end="")

# Usage
Terminal.clear()
Terminal.success("Database connection established successfully.")
Terminal.warning("High memory utilization detected (84%).")
Terminal.error("Failed to authenticate API token.")
print(Terminal.rgb(255, 105, 180, "Custom 24-bit RGB Pink Text!"))