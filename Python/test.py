from colorama import Fore, Back, Style, init

# Initialize (required on Windows, harmless on other OS)
init()

# Foreground colors
print(Fore.RED + "This is red text")
print(Fore.GREEN + "This is green text")
print(Fore.BLUE + "This is blue text")
print(Fore.YELLOW + "This is yellow text")
print(Fore.CYAN + "This is cyan text")
print(Fore.MAGENTA + "This is magenta text")
print(Fore.WHITE + "This is white text")
print(Back.BLACK + "This is text with black background")

# Reset color after printing
print(Fore.RED + "Red text" + Style.RESET_ALL + " Back to normal")