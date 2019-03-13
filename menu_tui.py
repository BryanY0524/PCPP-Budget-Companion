def drawline():
    '''
    Draws Line
    '''
    ln_Symbol = "*"
    ln_Length = 134
    print(ln_Symbol * ln_Length)


def projectTitle():
    '''
    Prints Project Title
    '''
    print(
        " _______                       __          __                      " +
        "          _______             __  __        __                       "
    )
    print(
        "|       \                     |  \        |  \                     " +
        "         |       \           |  \|  \      |  \                    ")
    print(
        "| $$$$$$$\  ______    _______ | $$   __  _| $$_     ______    _____" +
        "_        | $$$$$$$\ __    __  \$$| $$  ____| $$  ______    ______  ")
    print(
        "| $$  | $$ /      \  /       \| $$  /  \|   $$ \   /      \  /     " +
        " \       | $$__/ $$|  \  |  \|  \| $$ /      $$ /      \  /      \ ")
    print(
        "| $$  | $$|  $$$$$$\|  $$$$$$$| $$_/  $$ \$$$$$$  |  $$$$$$\|  $$$$" +
        "$$\      | $$    $$| $$  | $$| $$| $$|  $$$$$$$|  $$$$$$\|  $$$$$$\\")
    print(
        "| $$  | $$| $$    $$ \$$    \ | $$   $$   | $$ __ | $$  | $$| $$  |" +
        " $$      | $$$$$$$\| $$  | $$| $$| $$| $$  | $$| $$    $$| $$   \$$")
    print(
        "| $$__/ $$| $$$$$$$$ _\$$$$$$\| $$$$$$\   | $$|  \| $$__/ $$| $$__/" +
        " $$      | $$__/ $$| $$__/ $$| $$| $$| $$__| $$| $$$$$$$$| $$      ")
    print(
        "| $$    $$ \$$     \|       $$| $$  \$$\   \$$  $$ \$$    $$| $$   " +
        " $$      | $$    $$ \$$    $$| $$| $$ \$$    $$ \$$     \| $$      ")
    print(
        " \$$$$$$$   \$$$$$$$ \$$$$$$$  \$$   \$$    \$$$$   \$$$$$$ | $$$$$" +
        "$$        \$$$$$$$   \$$$$$$  \$$ \$$  \$$$$$$$  \$$$$$$$ \$$      ")
    print(
        "                                                            | $$  " +
        "                                                                    ")
    print(
        "                                                            | $$   " +
        "                                                                   ")
    print(
        "                                                             \$$   " +
        "                                                                   ")
    print("\n\nCreated By: Jimmy Ho, Bryan Yuen, Charles Harold Llanto")


def exposition():
    print("Welcome to Desktop Builder")
    print("The purpose of this program is to:" +
          "\n-something\n-something\n-something")
    print("This is why we decided to do this ASDKAJSLDKAJSDLKAJSDLJKASD")
    drawline()


def startMenu():
    '''
    '''
    exposition()
    symbol_Length = int(48 / 2)
    menuOption = ["1", "2"]
    print("-" * symbol_Length + "Menu" + "-" * symbol_Length)
    print("Option 1: Create Desktop with Guided Parameters")
    print("Option 2: Create Custom Desktop")
    menuSelect = input("Select an option: ")
    while str(menuSelect).lower() != "q":
        # Parses and validates user menu option
        try:
            if menuSelect == menuOption[0]:
                menu_parameter(0)
                break
            if menuSelect == menuOption[1]:
                menu_parameter(1)
                break
        except:
            print("***Error: Invalid Option***")
            menuSelect = input("Select an option: ")
    return


def menu_parameter(userOption, userBudget):
    '''
    Filler description
    '''
    user_Parameter = []
    # menuInput = input("Type q or Q to quit, ? for help")
    para_Option = {
        "p1": ["Home Office", "Gaming Desktop", "Media Editing Workstation"],
        "p2": ["AMD", "Intel"],  # Brand of CPU
        "p3": ["Yes", "No"]  # Option for Overclock enabled CPU
    }
    para_Questions = ["Question 1: What type of desktop do you want?"]
    userBudget = input("To start, please enter your budget: ")
    while str(userBudget).lower() != "q":
        # Parses and validates user budget
        try:
            userBudget = float(userBudget)
            print("Budget = $%.2f" % userBudget)
            break
        except:
            print("***Error: Invalid Value***")
            userBudget = input("To start, please enter your budget: ")
    return user_Parameter


def help_parameter():
    helpDirectory = []
    with open("HELPMENU.txt", "r") as textFile:
        helpDirectory.append(textFile.readlines())
    print(helpDirectory)


parameter_List = []
projectTitle()
drawline()
startMenu()
#help_parameter()