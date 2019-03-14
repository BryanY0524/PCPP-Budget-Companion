from PCPartPicker_API import pcpartpicker as pcpp
import csv


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

def write_CSV(productLists):
     

if __name__ == "__main__":
    BIGLIST = update()
    write_CSV(BIGLIST)