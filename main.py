from rich import print
from rich.panel import Panel
from menu import Menu
from clean_console import clean_console
# Add here another imports
# Consider PEP 8 for imorts -> https://www.python.org/dev/peps/pep-0008/#imports

# Set menu options.
# By default, last option will be Exit, there's no need to specify it.
# Menu options will be auto numerated
OPTIONS = """
Option 1
Option 2
Option 3
"""

clean_console()
menu = Menu(OPTIONS)
menu_options = Panel(menu.get_menu(),
                     expand=False,
                     title="[bold] M E N U [/]",
                     padding=(1, 5, 0, 2),
                     highlight=True)

option = ""
while option != "Exit":
    print(menu_options)
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