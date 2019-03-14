from PCPartPicker_API import pcpartpicker as pcpp


def pcpp_Scrape():
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


def getCPU(compList, cpu_info):
    '''
    '''
    cpu_para = [
        'AMD Ryzen', 'Intel Core i3-8', 'Intel Core i5-8', 'Intel Core i7-8',
        'Intel Core i3-9', 'Intel Core i5-9', 'Intel Core i7-9700',
        'Intel Core i9-9900K'
    ]
    cpu_ex = 'OEM'
    cpu_dict = []

    for model in cpu_para:
        for cpu in cpu_info:
            if model in cpu['name']:
                if cpu_ex not in cpu['name']:
                    if cpu['price'] != '':
                        cpu_dict.append(cpu)

    for cpu in cpu_dict:
        cpu['price'] = float(cpu['price'].strip('$'))

    type = compList["name"]
    chosen_set = []
    if 'gen' in type:
        for cpu in cpu_dict:
            if 'AMD' in cpu['name'] and 'G' in cpu['name']:
                chosen_set.append(cpu)
            if 'Intel' in cpu['name'] and 'F' not in cpu['name']:
                chosen_set.append(cpu)
    elif 'game' in type or 'ws' in type:
        for cpu in cpu_dict:
            if 'AMD' in cpu['name'] and 'G' not in cpu['name']:
                chosen_set.append(cpu)
            if 'Intel' in cpu['name']:
                chosen_set.append(cpu)

    cpu_set = []
    for cpu in chosen_set:
        if cpu['price'] < compList['cpu']:
            cpu_set.append(cpu)

    cpu_p = []
    for i in cpu_set:
        cpu_p.append(i['price'])

    chosen_cpu = cpu_set[cpu_p.index(max(cpu_p))]

    return chosen_cpu
