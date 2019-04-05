import budget_Formula
import pcpp_Scrape
import pcpp_Filter
import time


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
    print("-" * symbol_Length + "Menu" + "-" * symbol_Length)


def startMenu():
    '''
    Menu for program, allows user to start program or update/store local files
    Return:
    -   User-based parameter List(Desktop Type, User Budget)
    '''
    exposition()  # Load Exposition of TUI
    print("At anytime in the program, enter \"q\" or \"Q\" to quit...")
    print("---Option 1: Start Creating Custom Desktop with Guided Parameters")
    print("---Option 2: Create Desktop Based on Type")
    print("---Option 3: Update Local Files")
    menuSelect = input("Select an option: ")
    # Parses and validates user menu option
    try:
        if menuSelect is "1":
            return menu_parameter(0)  # Returns Parameter List
        elif menuSelect is "2":
            return menu_parameter(1)  # Returns Parameter List
        elif menuSelect is "3":
            input("Press enter to update...")
            print("Please wait for program to finish scraping data")
            print("This will take several minutes...")
            pcpp_Scrape.update()
            print("The Update is finished")
            print("The program will End in 5 seconds")
            print("Please Restart the program to Build Your computer")
            time.sleep(5)
        else:
            raise ValueError("***Error: Invalid Option***")
    except ValueError as error:
        print(error)
        menuSelect = input("Select an option: ")  # Prompt user for input
    exit()


def menu_parameter(userOption):
    '''
    Filler description
    '''
    drawline()
    user_Para = []
    para_Option = {
        "p1": ["General Usage", "Gaming Desktop", "Media Editing Workstation"],
        "p2": ["AMD", "Intel", "Doesn't Matter"],  # Brand of CPU
        "p3": ["Yes", "No",
               "Doesn't Matter"],  # Option for Overclock enabled CPU
        "p4": ["Small", "Regular", "Doesn't Matter"],  # Size of Case and MB
        "p5": ["Nvidia", "Radeon", "Doesn't Matter"]  # Video Card Parameter
    }
    para_Q = {
        "Q1": "What type of desktop do you want?",
        "Q2": "What brand of CPU do you want?",
        "Q3": "Do you want an Overclock enabled CPU?",
        "Q4": "What size of the computer tower do you want?",
        "Q5": "What brand of GPU do you want?"
    }
    skip = 0
    AMT_OF_Q = len(para_Option)
    for num in range(1, AMT_OF_Q + 2):
        errorTrack = False  # Tracks error in menu
        if num + skip < AMT_OF_Q + 1:
            print(para_Q["Q" + str(num + skip)])
            for index, items in enumerate(para_Option["p" + str(num + skip)]):
                print("---Option", str(index + 1) + ":", items)
            userInput = input("Please choose an option: ")
        while errorTrack is False:
            try:
                if str.isdigit(userInput) is False:
                    raise ValueError("***Error: Invalid Value***")
                elif int(userInput) > 0 and int(userInput) < 4:
                    drawline()
                    if userOption is 1:
                        budget = userBudget(int(userInput))
                        user_Para = [
                            (userInput, budget, 1, 3, 3,
                                3),  # AMD Build Option
                            (userInput, budget, 2, 3, 3, 3)  # Intel Option
                        ]
                        errorTrack = True
                        return user_Para
                    else:
                        if len(user_Para) < AMT_OF_Q + 1:
                            user_Para.append(int(userInput))
                            if user_Para[0] is 1:  # General Usage Option
                                if num is 3:  # Skip GPU Question
                                    user_Para.append(3)
                                    skip += 1
                            if len(user_Para) is 3 and int(
                                    userInput) is 1:  # AMD
                                user_Para.append(3)  # Append Default Overclock
                                skip += 1
                            if num is 1:
                                user_Para.append(userBudget(int(userInput)))
                            errorTrack = True
                        else:
                            return [user_Para]
                            errorTrack = True
                else:
                    raise ValueError("***Error: Invalid Option***")
            except (ValueError, TypeError) as error:
                print(error)
                userInput = input("Please choose an option: ")


def userBudget(option):
    '''
    Filler Description
    '''
    budgetFloor = [500, 700, 1000]
    budgetStatus = True
    budget = input("Enter your budget: ")
    while str(budget).lower() != "q":
        # Parses and validates user budget
        try:
            budget = float(budget)
            while budgetStatus:
                if budget < budgetFloor[option - 1] and type(budget) is float:
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
    drawline()
    return budget


MASTER_LIST = pcpp_Scrape.read_JSON()
# (CPU, Motherboard, Memory, Storage, GPU, Case, PSU, CPU Cooler)


parameter_List = startMenu()


for lists in parameter_List:
    compList = budget_Formula.giveFormula(lists[0], lists[1])
    pcpp_Filter.grabBuilds(compList, lists, MASTER_LIST)
    drawline()
