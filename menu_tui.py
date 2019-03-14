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
    print("-" * symbol_Length + "Menu" + "-" * symbol_Length)
    print("---Option 1: Create Desktop with Guided Parameters")
    print("---Option 2: Create Custom Desktop")
    menuSelect = "1"  #input("Select an option: ")
    while str(menuSelect).lower() != "q":
        # Parses and validates user menu option
        try:
            if menuSelect == "1":
                menu_parameter(1)
                break
            if menuSelect == "2":
                menu_parameter(2)
                break
        except:
            print("***Error: Invalid Option***")
            menuSelect = input("Select an option: ")
    return


def menu_parameter(userOption):
    '''
    Filler description
    '''
    drawline()
    user_Parameter = []
    # menuInput = input("Type q or Q to quit, ? for help")
    para_Option = {
        "p1": ["General Usage", "Gaming Desktop", "Media Editing Workstation"],
        "p2": ["AMD", "Intel"],  # Brand of CPU
        "p3": ["Yes", "No"]  # Option for Overclock enabled CPU
    }
    para_Q = ["Question 1: What type of desktop do you want?"]
    if userOption == 1:
        print(para_Q[0])
        for index, items in enumerate(para_Option["p1"]):
            print("---Option", str(index + 1) + ":", items)
        q1_userOption = input("Please choose an option: ")
        while q1_userOption.lower() != "q":
            try:
                if int(q1_userOption) > 0 and int(q1_userOption) < 4:
                    print(q1_userOption, userBudget())
                    break
                else:
                    print("***Error: Invalid Option***")
                    q1_userOption = input("Please choose an option: ")
            except:
                print("***Error: Invalid Option***")
                q1_userOption = input("Please choose an option: ")

    return user_Parameter


def userBudget():
    budget = input("To start, please enter your budget: ")
    while str(budget).lower() != "q":
        # Parses and validates user budget
        try:
            budget = float(budget)
            print("Budget = $%.2f" % budget)
            break
        except:
            print("***Error: Invalid Value***")
            budget = input("To start, please enter your budget: ")
    return budget


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