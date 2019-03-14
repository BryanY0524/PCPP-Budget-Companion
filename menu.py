import budget_Formula
import pcpp_Scrape
import pcpp_Filter


def drawline():
    '''
    Draws Line, used mostly for TUI formatting
    '''
    ln_Symbol = "*"  # Symbol for line drawing
    ln_Length = 134  # Length of symbol drawing
    print(ln_Symbol * ln_Length)


def exposition():
    '''
    Prints exposition of project
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
    drawline()
    print("Welcome to Desktop Builder")
    print("The purpose of this program is to:" +
          "\n---Assist those that are either novices or veterans at computer" +
          " building and provide useful tools that can be applicable at a" +
          " lower and higher level of understanding.")
    print("This is why we decided to do this ASDKAJSLDKAJSDLKAJSDLJKASD")
    drawline()


def startMenu():
    '''
    Returns parameter list based on user input
    '''
    exposition()  # Load Exposition of TUI
    symbol_Length = int(48 / 2)
    print("-" * symbol_Length + "Menu" + "-" * symbol_Length)
    print("---Option 1: Start Creating Desktop with Guided Parameters")
    print("---Option 2: Create Custom Desktop")
    print("---Enter \"q\" or \"Q\" to quit the program")
    menuSelect = "1"  # input("Select an option: ")
    while str(menuSelect).lower() != "q":
        # Parses and validates user menu option
        try:
            if menuSelect == "1":
                pList = menu_parameter(1)
                break
            if menuSelect == "2":
                pList = menu_parameter(2)
                break
        except:
            print("***Error: Invalid Option***")
            menuSelect = input("Select an option: ")
    return pList


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
    para_Q = ["What type of desktop do you want?"]
    returnList = []
    if userOption == 1:
        print(para_Q[0])
        for index, items in enumerate(para_Option["p1"]):
            print("---Option", str(index + 1) + ":", items)
        q1_userOption = input("Please choose an option: ")
        while q1_userOption.lower() != "q":
            try:
                if int(q1_userOption) > 0 and int(q1_userOption) < 4:
                    returnList = [
                        q1_userOption,
                        userBudget(int(q1_userOption))
                    ]
                    break
                else:
                    print("***Error: Invalid Option***")
                    q1_userOption = input("Please choose an option: ")
            except:
                print("***Error: Invalid Option***")
                q1_userOption = input("Please choose an option: ")
    return returnList


def userBudget(option):
    '''
    Filler Description
    '''
    drawline()
    budgetFloor = [500, 700, 1000]
    budgetStatus = True
    budget = input("Enter your budget: ")
    while str(budget).lower() != "q":
        # Parses and validates user budget
        budget = float(budget)
        try:
            while budgetStatus:
                if budget < budgetFloor[option - 1]:
                    print("Please make sure your input is more than $%.2f" %
                          budgetFloor[option - 1])
                    budget = float(input("Enter your budget: "))
                else:
                    budgetStatus = False
            break
        except:
            print("***Error: Invalid Value***")
            budget = input("Enter your budget: ")
    print("Budget = $%.2f" % budget)
    return budget


def help_parameter():
    helpDirectory = []
    with open("HELPMENU.txt", "r") as textFile:
        helpDirectory.append(textFile.readlines())
    print(helpDirectory)


print("Please wait while the program scrapes the web...")
MASTER_LIST = pcpp_Scrape.update()
# (CPU, Motherboard, Memory, Storage, GPU, Case, PSU)
pList = (1, 500)  # startMenu()
compList = budget_Formula.giveFormula(pList[0], pList[1])
print(pcpp_Filter.getCPU(compList, MASTER_LIST[0]))
