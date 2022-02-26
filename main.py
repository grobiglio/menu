from rich.console import Console
from menu import Menu
from clean_console import clean_console
# Add here another imports
# Consider PEP 8 for imorts -> https://www.python.org/dev/peps/pep-0008/#imports

clean_console()
console = Console()

# Set menu options.
# By default, last option will be Exit, there's no need to specify it.
# Menu options will be auto numerated
options = """
Option 1
Option 2
Option 3
"""
menu = Menu(options)

option = ""
while option != "Exit":
    console.print(menu.get_menu())
    option = menu.request_option() 
    if option == 1:
        # Code for option 1
        pass
    elif option == 2:
        # Code for option 2
        pass
    elif option == 3:
        # Code for option 3
        pass

# Code to execute befor exit main program