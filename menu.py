import budget_Formula
import pcpp_Scrape
import pcpp_Filter
import sys


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
    symbol_Length = int(48 / 2)
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
    print("The purpose of this program is to:")
    print("---Assist those that are either novices or veterans at computer" +
          " building and provide useful tools that can be applicable at a" +
          " lower and higher level of understanding.")
    print("\nThis is why we decided to do this ASDKAJSLDKAJSDLKAJSDLJKASD")
    drawline()
    print("-" * symbol_Length + "Menu" + "-" * symbol_Length)


def startMenu():
    '''
    Menu for program, allows user to start program or update/store local files
    Return:
    -   User-based parameter List(Desktop Type, User Budget)
    '''
    exposition()  # Load Exposition of TUI
    print("At anytime in the program, enter \"q\" or \"Q\" to quit...")
    print("---Option 1: Start Creating Desktop with Guided Parameters")
    print("---Option 2: Update Local Files")
    menuSelect = input("Select an option: ")
    while menuSelect.lower() != "q":
        # Parses and validates user menu option, entering q quits program
        try:
            if menuSelect == "1":
                parameter_List = menu_parameter()  # Gets Parameter List
                return parameter_List  # Returns Parameter List(type, budget)
            elif menuSelect == "2":
                input("Press enter to update...")
                print("Please wait for program to finish scraping data")
                print("This will take several minutes...")
                pcpp_Scrape.update()
            else:
                raise ValueError("***Error: Invalid Option***")
        except ValueError as error:
            print(error)
            menuSelect = input("Select an option: ")  # Prompt user for input
    exit()


def menu_parameter():
    '''
    Filler description
    '''
    drawline()
    user_Parameter = []
    para_Option = {
        "p1": ["General Usage", "Gaming Desktop", "Media Editing Workstation"],
        "p2": ["AMD", "Intel"],  # Brand of CPU
        "p3": ["Yes", "No"],  # Option for Overclock enabled CPU
        "p4": ["Micro ATX", "ATX"]  # Size of Motherboard
    }
    para_Q = ["What type of desktop do you want?"]
    print(para_Q[0])
    for index, items in enumerate(para_Option["p1"]):
        print("---Option", str(index + 1) + ":", items)
    u_desktopType = input("Please choose an option: ")
    while u_desktopType.lower() != "q":
        try:
            if int(u_desktopType) > 0 and int(u_desktopType) < 4:
                user_Parameter = [
                    u_desktopType,
                    userBudget(int(u_desktopType))
                ]
                return user_Parameter
                break
            else:
                raise ValueError("***Error: Invalid Option***")
        except ValueError as error:
            print(error)
            u_desktopType = input("Please choose an option: ")
    exit()


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


def exit():
    sys.exit(0)


def help_parameter():
    helpDirectory = []
    with open("HELPMENU.txt", "r") as textFile:
        helpDirectory.append(textFile.readlines())
    print(helpDirectory)


MASTER_LIST = pcpp_Scrape.read_JSON()
# (CPU, Motherboard, Memory, Storage, GPU, Case, PSU)
# parameter_List = startMenu()
testvalues = [(1, 500), (1, 1000), (2, 700), (2, 1500), (2, 2000),
              (2, 2500), (2, 3000), (3, 1000), (3, 1500), (3, 3000)]
for testsubject in testvalues:
    # parameter_List[0], parameter_List[1])
    compList = budget_Formula.giveFormula(testsubject[0], testsubject[1])
    chosen_cpu = pcpp_Filter.getCPU(compList, MASTER_LIST[0])
    print(testsubject)
    print(chosen_cpu)
    print(pcpp_Filter.getmobo(compList, MASTER_LIST[1], chosen_cpu))
