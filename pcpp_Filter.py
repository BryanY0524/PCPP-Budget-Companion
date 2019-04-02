from PCPartPicker_API import pcpartpicker as pcpp


def getCPU(compList, cpuList):
    '''
    '''
    CPU_PARAMETER = [
        'AMD Ryzen', 'Intel Core i3-8', 'Intel Core i5-8', 'Intel Core i7-8',
        'Intel Core i3-9', 'Intel Core i5-9', 'Intel Core i7-9700',
        'Intel Core i9-9900K'
    ]
    CPU_EXCLUDE = 'OEM'
    cpu_Dict = []

    for cpu in cpuList:
        for model in CPU_PARAMETER:
            if model in cpu['name']:
                if CPU_EXCLUDE not in cpu['name']:
                    if cpu['price'] != '':
                        cpu_Dict.append(cpu)

    for cpu in cpu_Dict:
        if type(cpu['price']) == float:
            continue
        else:
            cpu['price'] = float(cpu['price'].strip('$'))

    desktop_type = compList["name"]
    chosen_set = []
    if 'gen' in desktop_type:
        for cpu in cpu_Dict:
            if 'AMD' in cpu['name'] and 'G' in cpu['name']:
                chosen_set.append(cpu)
            if 'Intel' in cpu['name'] and 'F' not in cpu['name']:
                chosen_set.append(cpu)
    elif 'game' in desktop_type or 'ws' in desktop_type:
        for cpu in cpu_Dict:
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


def getmobo(compList, mobo_info, chosen_cpu):
    '''
    '''
    # Special ASUS motherboard from 8th gen that support 9th gen intel CPU
    ASUS_INTEL9 = [
        'STRIX Z370-E', 'STRIX Z370-F', 'STRIX Z370-H', 'STRIX Z370-G',
        'PRIME Z370-A', 'TUF Z370-PRO GAMING', 'TUF Z370-PLUS GAMING',
        'PRIME Z370-P', 'STRIX Z370-I', 'ROG MAXIMUS X ', 'STRIX H370-F',
        'STRIX H370-I', 'TUF H370-PRO GAMING', 'PRIME H370-A',
        'PRIME H370-PLUS', 'PRIME H370M-PLUS', 'STRIX B360-H GAMING',
        'STRIX B360-F GAMING', 'STRIX B360-G GAMING', 'STRIX B360-I GAMING',
        'TUF B360-PRO GAMING', 'TUF B360-PLUS GAMING', 'TUF B360M-E GAMING',
        'TUF B360M-PLUS GAMING', 'PRIME B360-PLUS', 'PRIME B360M-A',
        'PRIME B360M-C', 'PRIME B360M-D', 'PRIME B360M-K', 'EX-B360M-V',
        'TUF H310-PLUS GAMING', 'PRIME H310-PLUS', 'TUF H310M-PLUS GAMING',
        'PRIME H310M-A', 'PRIME H310M-C', 'PRIME H310I-PLUS', 'PRIME H310M-E',
        'PRIME H310M-K', 'PRIME H310M-D', 'PRIME H310T'
    ]

    GIGA_INTEL9 = [
        'Z370 AORUS', 'Z370 HD3', 'Z370M D3H', 'Z370M DS3H', 'Z370N WIFI',
        'Z370P D3', 'Z370 UD3H', 'Z370XP SLI', 'H370 AORUS GAMING 3',
        'H370M D3H', 'H370M DS3H', 'H370M D3H', 'H370 HD3', 'H370N WIFI',
        'B360 AORUS', 'B360 HD3', 'B360M GAMING', 'B360 HD3P', 'B360M D2V',
        'B360M D3H', 'B360M D3P', 'B360M D3V', 'B360M DS3H', 'B360M H',
        'B360M HD3', 'B360N WIFI', 'H310M S2H', 'H310M DS2', 'H310 D3',
        'H310M A', 'H310M H', 'H310M S2', 'H310N'
    ]
    # Special Gigabyte motherboard from 8th gen that support 9th gen intel CPU

    MSI_INTEL9 = [
        'MSI B360 GAMING', 'MSI B360-A PRO', 'MSI B360M BAZOOKA',
        'MSI B360I GAMING PRO AC', 'MSI B360M GAMING', 'MSI B360M MORTAR',
        'MSI B360M PRO-V', 'MSI H310-A PRO', 'MSI H310I PRO',
        'MSI H310M GAMING', 'MSI H310M PRO-', 'MSI H370 GAMING',
        'MSI H370M BAZOOKA', 'MSI Z370 GAMING', 'MSI Z370 GODLIKE',
        'MSI Z370 KRAIT', 'MSI Z370 PC PRO', 'MSI Z370 SLI PLUS',
        'MSI Z370 TOMAHAWK', 'MSI Z370-A PRO', 'MSI Z370I GAMING PRO',
        'MSI Z370M GAMING PRO', 'MSI Z370M MORTAR'
    ]
    # Special MSI motherboard from 8th gen that support 9th gen intel CPU

    ASROCK_INTEL9 = [
        'ASRock Z370M-ITX/ac', 'ASRock Z370M Pro4', 'ASRock Z370 Taichi',
        'ASRock Z370 Pro4', 'ASRock Z370 Killer SLI', 'ASRock Z370 Extreme4',
        'ASRock H370M-ITX/ac', 'ASRock H370M Pro4', 'ASRock H370 Pro4',
        'ASRock H310M-ITX/ac', 'ASRock H310M-HDV', 'ASRock H310M-G/M.2',
        'ASRock H310M-DGS', 'ASRock Fatal1ty Z370',
        'ASRock Fatal1ty H370 Performance', 'ASRock Fatal1ty B360 Gaming K4',
        'ASRock B360M-ITX/ac', 'ASRock B360M-HDV', 'ASRock B360M Pro4',
        'ASRock B360M Performance', 'ASRock B360 Pro4'
    ]
    # Special ASROCK motherboard from 8th gen that support 9th gen intel CPU

    INTEL_9_BASE = ['Z390', 'Asus ROG MAXIMUS XI ']
    # Basic motherboard chipset that support Intel 9th gen CPU

    INTEL_9_PARA = INTEL_9_BASE + ASUS_INTEL9 + \
        GIGA_INTEL9 + MSI_INTEL9 + ASROCK_INTEL9
    # Parameter for all motherboard that support intel 9th gen CPU

    INTEL_8_PARA = [
        'Z370', 'H310', 'H370', 'Z390', 'B360', 'Asus ROG MAXIMUS X ',
        'Asus ROG MAXIMUS XI '
    ]
    # Parameter for all motherboard that support intel 8th gen CPU

    AMD_PARA = ['A320', 'B350', 'B450', 'X370', 'X470', 'Asus CROSSHAIR VI ']
    # Parameter for all motherboard that support AMD Ryzen CPU

    INTEL_8_CPU = ['Intel Core i3-8', 'Intel Core i5-8', 'Intel Core i7-8']
    INTEL_9_CPU = [
        'Intel Core i3-9', 'Intel Core i5-9', 'Intel Core i7-9700',
        'Intel Core i9-9900K'
    ]
    AMD_CPU = ['AMD Ryzen']
    # list of names to identify CPU brand and series

    cpu_model = [INTEL_8_CPU, INTEL_9_CPU, AMD_CPU]
    motherboard_for_cpu = [INTEL_8_PARA, INTEL_9_PARA, AMD_PARA]

    mobo_dict = []
    for model in cpu_model:
        for cpu in model:
            if cpu in chosen_cpu['name']:
                for motherboard in mobo_info:
                    for para in motherboard_for_cpu[cpu_model.index(model)]:
                        if para in motherboard['name']:
                            if motherboard['price'] != '':
                                mobo_dict.append(motherboard)
    # Filter a list of motherboards that is compatible with the CPU chosen and has a price.

    for motherboard in mobo_dict:
        if type(motherboard['price']) == float:
            continue
        else:
            motherboard['price'] = float(
                motherboard['price'].strip('$'))  # remove dollar sign

    mobo_dict_budget = []
    for motherboard in mobo_dict:
        if motherboard['price'] < compList['motherboard']:
            mobo_dict_budget.append(
                motherboard
            )  # alternative list of motherboard, filtered by price

    chosen_mobo_set = []
    if 'Intel' in chosen_cpu['name']:
        if 'K' in chosen_cpu['name']:
            for motherboard in mobo_dict:
                if ('Z370' in motherboard['name']) \
                    or ('Z390' in motherboard['name']) \
                        or ('MAXIMUS' in motherboard['name']):
                    chosen_mobo_set.append(motherboard)
        else:
            for motherboard in mobo_dict:
                if ('B360' in motherboard['name']) \
                        or ('H310' in motherboard['name']) \
                        or ('H370' in motherboard['name']):
                    chosen_mobo_set.append(motherboard)
    elif 'AMD' in chosen_cpu['name']:
        if 'X' in chosen_cpu['name']:
            for motherboard in mobo_dict:
                if ('X370' in motherboard['name']) \
                        or ('X470' in motherboard['name']) \
                        or ('CROSSHAIR' in motherboard['name']):
                    chosen_mobo_set.append(motherboard)
        else:
            for motherboard in mobo_dict:
                chosen_mobo_set.append(motherboard)
    # Filter a list of chosen motherboard in reasonable parameter.
    # e.g. unlocked intel CPU with overclock enabled motherboard

    mobo_set = []
    for motherboard in chosen_mobo_set:
        if motherboard['price'] < compList['motherboard']:
            mobo_set.append(motherboard)  # filter by price

    if mobo_set == []:
        for motherboard in mobo_dict_budget:
            mobo_set.append(
                motherboard
            )  # use alternative list if the optimal list is empty

    mobo_p = []
    for motherboard in mobo_set:
        mobo_p.append(motherboard['price'])

    # pick highest value within budget
    chosen_motherboard = mobo_set[mobo_p.index(max(mobo_p))]
    return chosen_motherboard


def getram(compList, ram_info, chosen_mobo):
    ram_dict = []
    for ram in ram_info:
        if ('288' in ram['type']) \
                and (ram['price'] != '')\
                and (ram['cas'] != 'N/A'):
            ram_dict.append(ram)
    # filter out DDR4 desktop ram

    for ram in ram_dict:
        if type(ram['price']) == float:
            continue
        else:
            ram['price'] = float(ram['price'].strip('$'))
        if type(ram['price/gb']) == float:
            continue
        else:
            ram['price/gb'] = float(ram['price/gb'].strip('$'))
        ram['speed'] = int(ram['speed'].strip('DDR4-'))
        if type(ram['cas']) != int:
            ram['cas'] = int(ram['cas'])
        ram['size'] = int(ram['size'].strip('GB'))
    # change price and price/gb to float, and speed,size,cas to int, for easier processing.

    ram_set = []
    for ram in ram_dict:
        if ('x4' not in ram['modules']) and \
                ('8x8' not in ram['modules']) and \
                ('1x16' not in ram['modules']):
            if 8 <= ram['size'] <= 64:
                if ram['price/gb'] < 12.00:
                    ram_set.append(ram)
    # filter out ram that is too expensive in terms of price/performance.

    ram_budget_set = []
    for ram in ram_set:
        if ram['price'] < compList['memory']:
            ram_budget_set.append(ram)
    # filter out all ram that is within budget

    ram_chosen_set = []
    ram_size_list = [64, 32, 16, 8]
    for size in ram_size_list:
        if ram_chosen_set == []:
            for ram in ram_budget_set:
                if ram['size'] == size:
                    ram_chosen_set.append(ram)
    # filter ram by the maximum capacity available

    ram_count_set = []
    for ram in ram_chosen_set:
        if int(ram['modules'][0]) <= int(chosen_mobo['ram-slots']):
            ram_count_set.append(ram)
    # filter ram by the maximum ram-slots by the chosen motherboard

    ram_speed_cas_list = []
    for ram in ram_count_set:
        ram_speed_cas_list.append(ram['speed'] / ram['cas'])
    # make a list thats in the same order as ram_count_set, but in terms of speed/cas

    ram_select_set = []
    for index, speedcas in enumerate(ram_speed_cas_list, 0):
        if speedcas == max(ram_speed_cas_list):
            ram_select_set.append(ram_count_set[index])
    # filter the ram modules with the maximum speed/cas ratio for performance

    ram_speed_list = []
    for ram in ram_select_set:
        ram_speed_list.append(ram['speed'])
    # make a list thats in the same order as ram_select_set, but in terms of ram speed only

    ram_speed_module = []
    for index, speed in enumerate(ram_speed_list, 0):
        if speed == max(ram_speed_list):
            ram_speed_module.append(ram_select_set[index])
    # filter the ram modules with the maximum speed

    ram_price_list = []
    for ram in ram_speed_module:
        ram_price_list.append(ram['price'])
    # make a list thats in the same order as ram_select_set, but in terms of ram speed only

    ram_price_module = []
    for index, price in enumerate(ram_price_list, 0):
        if price == min(ram_price_list):
            ram_price_module.append(ram_speed_module[index])
    # filter the ram modules with the minimum price

    chosen_ram = ram_price_module[0]

    return chosen_ram


def getstor(compList, stor_info):
    stor_dict = []
    for drives in stor_info:
        if drives['price'] != '' and drives['price/gb'] != '':
            stor_dict.append(drives)
    # remove items with empty price value

    hdd_dict = []
    ssd_dict = []
    for drives in stor_dict:
        if type(drives['price']) == float:
            continue
        else:
            drives['price'] = float(drives['price'].strip('$'))
        if type(drives['price/gb']) == float:
            continue
        else:
            drives['price/gb'] = float(drives['price/gb'].strip('$'))
        if drives['capacity'] != '':
            if 'TB' in drives['capacity']:
                drives['capacity'] = float(
                    drives['capacity'].strip(' TB')) * 1024
            elif 'GB' in drives['capacity']:
                drives['capacity'] = float(drives['capacity'].strip(' GB'))

    for drives in stor_dict:
        if '7200' in drives['type'] or '5400' in drives['type']:
            hdd_dict.append(drives)
        elif 'SSD' == drives['type']:
            ssd_dict.append(drives)
    # turn price and capacity into float for future comparison, and split into list of SSD and HDD.

    ssd_budget_list = []
    for drives in ssd_dict:
        if 'M.2-2280' == drives[
                'form'] and drives['price'] <= compList['storage']:
            ssd_budget_list.append(drives)
    # filter specific form factor and SSD within price range

    ssd_comp_type_limit = []
    if 'ws' in compList['name']:
        for drives in ssd_budget_list:
            if drives['capacity'] < 1200:
                ssd_comp_type_limit.append(drives)
    else:
        ssd_comp_type_limit = ssd_budget_list
    # limit work station to have maximum of 1TB SSD, reserve extra budget for HDD if available

    ssd_cap_list = []
    for drives in ssd_comp_type_limit:
        ssd_cap_list.append(drives['capacity'])

    ssd_size_list = []
    for index, cap in enumerate(ssd_cap_list, 0):
        if cap > max(ssd_cap_list) * 0.9:
            ssd_size_list.append(ssd_comp_type_limit[index])
    # filter SSD to the top 10% of capacity

    ssd_pgb_list = []
    for drives in ssd_size_list:
        ssd_pgb_list.append(drives['price/gb'])

    ssd_value_list = []
    for index, pgb in enumerate(ssd_pgb_list, 0):
        if pgb < min(ssd_pgb_list) * 1.2:
            ssd_value_list.append(ssd_size_list[index])
    # filter SSD to the lowest price/gb and within 20% more

    ssd_price_list = []
    for drives in ssd_value_list:
        ssd_price_list.append(drives['price'])

    ssd_min_price = []
    for index, price in enumerate(ssd_price_list, 0):
        if price == min(ssd_price_list):
            ssd_min_price.append(ssd_value_list[index])

    selected_ssd = ssd_min_price[0]
    # filter a single SSD from filtered set

    # -----------------------SSD SECTION ENDED-------------------------#

    hdd_budget = compList['storage'] - selected_ssd['price']
    hdd_brand = ['Western Digital', 'Seagate']
    hdd_model = ['Barra', 'Blue']

    hdd_budget_list = []
    for drives in hdd_dict:
        for brand in hdd_brand:
            if brand in drives['name']:
                for model in hdd_model:
                    if model in drives['series']:
                        if drives['price'] <= hdd_budget and drives[
                                'form'] == '3.5"':
                            hdd_budget_list.append(drives)
    # filter specific form factor and models of HDD within price range

    hdd_cap_list = []
    for drives in hdd_budget_list:
        hdd_cap_list.append(drives['capacity'])

    hdd_size_list = []
    for index, cap in enumerate(hdd_cap_list, 0):
        if cap > max(hdd_cap_list) * 0.9:
            hdd_size_list.append(hdd_budget_list[index])
    # filter HDD to the top 10% of capacity

    hdd_pgb_list = []
    for drives in hdd_size_list:
        hdd_pgb_list.append(drives['price/gb'])

    hdd_value_list = []
    for index, pgb in enumerate(hdd_pgb_list, 0):
        if pgb < min(hdd_pgb_list) * 1.2:
            hdd_value_list.append(hdd_size_list[index])
    # filter HDD to the lowest price/gb and within 20% more

    hdd_price_list = []
    for drives in hdd_value_list:
        hdd_price_list.append(drives['price'])

    hdd_min_price = []
    for index, price in enumerate(hdd_price_list, 0):
        if price == min(hdd_price_list):
            hdd_min_price.append(hdd_value_list[index])

    if len(hdd_min_price) > 0 and hdd_min_price[0][
            'capacity'] > 900 and 'ws' in compList['name']:
        select_hdd = hdd_min_price[0]
    else:
        select_hdd = 'NO HDD'
    # filter a single HDD from filtered set

    return [selected_ssd, select_hdd]