from PCPartPicker_API import pcpartpicker as pcpp
import json


def update():
    '''
    Scrapes PCPartPicker product pages
    Returns
        Product List of (CPU, Motherboard, Memory, Storage, GPU, Case, PSU)
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
    return (cpuList, mbList, memList, stor_List, gpu_List, case_List, psu_List)


def dump_JSON(productLists):
    output_path = ".\\INPUTFILES\\"
    component_set = ("CPU", "MOTHERBOARD", "MEMORY",
                     "STORAGE", "GPU", "CASE", "PSU")
    '''with open(output_path + "CPU" + ".json", "w+") as outFile:
            for rows in productLists:
                json.dump(rows, outFile)'''
    
    for index, components in enumerate(component_set):
        with open(output_path + components + ".json", "w+") as outFile:
            for items in productLists[index]:
                json.dump(items, outFile)


if __name__ == "__main__":
    BIGLIST = update()
    dump_JSON(BIGLIST)
