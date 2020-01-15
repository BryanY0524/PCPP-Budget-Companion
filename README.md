# Desktop-Builder
ACIT 1515 Term Project

# Objectives of our program
The overall objective for our program was to have a functional program that provides assistance to beginner-novice level computer builders to pick components suitable for their budget.

# Motivation to do this project
E-Sports has become a huge trend in recent years and the number of gamers, especially in the young generations, has increased substantially. As the E-Sports community grows larger, both casual and hardcore gamers are interested in build their own PC. However, most people lack the knowledge and experience of building a computer. Moreover, because modern PC hardware has a wide range of options and specification, it would be difficult for beginner PC builders to choose compatible components. As a result, they would end up opting for the more expensive and potentially overpriced pre-built computer system from retailers. 

The initial motive of this project is to help people choose reasonable computer components within their budget according to their needs. The program should give the user an overview of potential combinations of hardware they could buy, and how much each component would cost. 

# How we achieved our objectives
Bryan started off by creating dictionaries for the budget, where each contains an identifier and the corresponding allocation of the budget to each component in percentage. This would allow the budget allocated to each component dynamically changes according to different budget price-bracket, and different type of computer the user wants to build. \
●	For example, for a $1500 Build, the budget allocated to the CPU would be 25% for gaming PC, and 28% for workstation PC; similarly for a $2500 gaming PC, 22% of the budget would be allocated to the CPU.

In order to access the budget dictionary, Jimmy implemented a user interface that allows the user to customize and select their parameters and budget. The parameters and the budget list will then correspond with a locally stored JSON file that contains all essential computer component products to create lists of components to choose from. This saves memory and time overhead since the PCPartPicker API is not utilized in every start-up.

Bryan has decided that the program should only include modern consumer level PC hardware. This would avoid the problem where the result includes outdated hardware that is not competent while costing similar to newer hardware. 

# Choosing Hardware: 
The order in which the components are chosen is a crucial part of the algorithm. The order would resolve and identify a streamline of hardware compatibility. Since Bryan has a broad knowledge of computer hardware, he is responsible for this section of the program. All of the following components require extra processing, such as removing items without a price and turning JSON object strings into float/int to compare and match specifications.

# CPU: 
Bryan has set the algorithm to pick a CPU first, which should match the budget and parameters set by the user, such as the brand of the CPU and overclockability. The program would also note if the CPU comes with a CPU cooler, which will be used to determine if an aftermarket CPU cooler is needed.

# Motherboard: 
After a CPU is chosen, the motherboard will then be chosen based on the chosen CPU. There are various motherboard chipsets that are compatible with each generation of CPU offered by Intel and AMD, and there is some backward compatibility offered by motherboard manufacturers; all of these factors would be considered in the process of choosing the motherboard. The algorithm would also prioritize having an overclocking enabled motherboard when the CPU is also overclockable. The user may also choose the size of the motherboard, which would translate to the size of the computer case in the later segment. The motherboard is chosen randomly from a set of motherboards that meets all the user’s parameter and budget.

# Memory Modules (RAM): 
After a motherboard is chosen, a set of memory modules will then be chosen. Since all modern motherboard uses desktop DDR4 memory modules, there is minimum compatibility issue there. However, because each motherboard has its own number of memory module capacity (RAM slots), the algorithm would pick the one that is most suitable. Furthermore, because each set of memory modules has its own memory speed and CAS latency, the algorithm would choose the set of memory modules that is within budget and has the highest speed with the lowest latency (or randomly choose from multiple modules when they have the same specification). 

# Storage (SSD/HDD): 
Since SSD price has dropped significantly and it affects the responsiveness of the PC significantly, Bryan decided to include an SSD drive as the first priority; and then allocate the remaining budget to get an HDD if needed. Because all modern motherboard is compatible with M.2 form factor SSD, and there is SATA port for the HDD, there would be no compatibility issue in this section. The SSD and HDD are both chosen from a set of drives that are within budget while choosing the one that has the lowest price per GB.

# Power Supply (PSU): 
Since all ATX power supplies are compatible with consumer level hardware, there is no compatibility issue to check. The algorithm would first pick out a list of PSU within budget, with a sufficient amount of power (watts) provided according to the type of computer the user has chosen to build. Next, it would filter a list of PSU that has the highest rating of energy efficiency, and then choose the one that has the lowest price.

# Computer Case: 
The computer case is first filtered to a list that matches the size of the motherboard chosen. The computer case is then filtered down to a set of reputable brands. Although this may not be the computer case that the user prefers, Bryan has decided to include this parameter to avoid computer cases that are low quality and flawed. The computer case is chosen randomly from a set of cases that are within budget and in the highest 25% price-bracket. 

# Graphics Card (GPU/Video Card):
Since there is no compatibility issue related to the graphics card, the algorithm to choose the graphics card is also relatively simple. A list of GPU chipset is first created, this is also ranked by the performance of the chipset. The program would utilize all the remaining budgets and pick the highest rank of GPU chipset. On top of that, the algorithm would test if the user can get a significant upgrade while exceeding the budget by a small amount (10% of the GPU budget). The algorithm would pick the higher ranked GPU chipset instead if the extra budget permitted a significant upgrade. In the end, the algorithm would choose the cheapest GPU within the chosen GPU chipset. 

# CPU cooler: 
At the very last stage, the algorithm would then check if the build needs a CPU cooler according to the chosen CPU. A small list of CPU cooler is chosen by Bryan, which he has researched and found them perform exceptionally well compared to the rest of the market. The algorithm has excluded AIO (All-In-One water-cooling solution) because air-cooler would have one less point of possible hardware failure compared to AIO.


After having the algorithm determine the most suitable combination of components to purchase, the program will then open up a web browser and automatically enter each selected part to PCPartPicker’s part list. The user can then check the part list to examine where to obtain each component. 

# Disclaimer: 
Note that this program’s intention is not to provide the cheapest possible computer part list, and the users do not need to follow the part list completely. It should provide a relatively clear direction and allocation of budget to the user, which the user can make changes to the part list to match their personal preference, such as aesthetics and colour scheme. Thus, this is also the reason that the algorithm’s result for the motherboard, memory modules, and case are somewhat randomized. 

# Learning Outcome
●	Learned how to successfully utilize different forms of data containers (Dictionary + Lists) \
●	Learned how to automate browser-based activities (Selenium) \
●	Learned how to utilize different programming functions to obtain the desired outcome (such as filtering a list using for-loop and enumerate) \
●	Learned debug functionalities in PyCharm + VSCode \
●	Learned how to utilize Github for team collaboration \
●	Learned modular design to enable better readability/debugging

# API Used
PCPartPicker_API (Ver 0.0.9)\
Selenium (Webdriver)

# Reference List
https://pypi.org/project/PCPartPicker-API/ \
https://selenium-python.readthedocs.io/ \
https://github.com/CheezyP/Desktop-Builder/commits/master
