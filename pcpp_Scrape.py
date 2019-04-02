from PCPartPicker_API import pcpartpicker as pcpp
import json


def update():
    '''
    Scrapes PCPartPicker product pages and parses data
    Calls dump_JSON()
    Returns
    -   Product List of (CPU, Motherboard, Memory, Storage, GPU, Case, PSU)
    '''
    pcpp.setRegion("ca")  # Selects Canada Region for PCPartPicker API
    cpuList = pcpp.productLists.getProductList("cpu")  # Grab CPU Product List
    mbList = pcpp.productLists.getProductList(
        "motherboard")  # Grab Motherboard Product List
    memList = pcpp.productLists.getProductList(
        "memory")  # Grab Memory Product List
    stor_List = pcpp.productLists.getProductList(
        "internal-hard-drive")  # Grab Internal Harddrive Product List
    gpu_List = pcpp.productLists.getProductList(
        "video-card")  # Grab GPU Product List
    case_List = pcpp.productLists.getProductList(
        "case")  # Grab Case Product List
    psu_List = pcpp.productLists.getProductList(
        "power-supply")  # Grab PSU Product List
    cpucool_List = pcpp.productLists.getProductList(
        "cpu-cooler")  # Grab CPU Cooler List
    dump_JSON((cpuList, mbList, memList, stor_List, gpu_List, case_List,
              psu_List, cpucool_List))


def dump_JSON(productLists):
    '''
    Take parsed product list from update() and writes to JSON files
    Arguments
    -   Set of specified product lists
    '''
    path = ".\\INPUTFILES\\"
    component_set = ("CPU", "MOTHERBOARD", "MEMORY", "STORAGE", "GPU", "CASE",
                     "PSU", "CPU_COOLER")
    for index, components in enumerate(component_set):
        with open(path + components + ".json", "w") as outFile:
            dictList = []
            for items in productLists[index]:
                dictList.append(items)
            json.dump(dictList, outFile)


def read_JSON():
    '''
    Reads Component JSON product files
    '''
    path = ".\\INPUTFILES\\"
    component_set = ("CPU", "MOTHERBOARD", "MEMORY", "STORAGE", "GPU", "CASE",
                     "PSU", "CPU_COOLER")
    MASTER_LIST = []
    for components in component_set:
        with open(path + components + ".json", "r") as inputJSON:
            MASTER_LIST.append(json.load(inputJSON))
    return MASTER_LIST


if __name__ == "__main__":
    update()
