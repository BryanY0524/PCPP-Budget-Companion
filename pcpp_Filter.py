from PCPartPicker_API import pcpartpicker as pcpp
import random


def grabBuilds(compList, parameter_List, MASTER_LIST):
    cpu_returns = getCPU(compList, MASTER_LIST[0], parameter_List)
    chosen_cpu = cpu_returns[0]
    cooler_option = cpu_returns[1]
    chosen_motherboard = getmobo(compList, MASTER_LIST[1], chosen_cpu,
                                 parameter_List[4])
    chosen_ram = getram(compList, MASTER_LIST[2], chosen_motherboard)
    storage_list = getstor(compList, MASTER_LIST[3])
    chosen_ssd = storage_list[0]
    chosen_hdd = storage_list[1]
    chosen_psu = getpsu(compList, MASTER_LIST[6])
    chosen_case = getcase(compList, MASTER_LIST[5], chosen_motherboard)
    extra_budget = (compList['cpu'] - chosen_cpu['price']) + (
            compList['motherboard'] - chosen_motherboard['price']) + (
                           compList['memory'] - chosen_ram['price']) + storage_list[2] + (
                           compList['psu'] - chosen_psu['price']) + (
                           compList['case'] - chosen_case['price'])

    chosen_gpu = getgpu(compList, MASTER_LIST[4], extra_budget,
                        parameter_List[5])
    chosen_cooler = getcooler(compList, MASTER_LIST[7], extra_budget,
                              cooler_option, chosen_gpu)

    print(parameter_List)
    print(compList)

    print(chosen_cpu)
    print(chosen_cooler)
    print(chosen_motherboard)
    print(chosen_ram)
    print(chosen_ssd)
    print(chosen_hdd)
    print(chosen_psu)
    print(chosen_gpu)
    print(chosen_case)

    all_parts = [chosen_cpu, chosen_cooler, chosen_motherboard, chosen_ram, chosen_gpu, chosen_ssd, chosen_hdd, chosen_psu, chosen_case]
    exist_parts = []
    for parts in all_parts:
        if isinstance(parts, dict) == True:
            exist_parts.append(parts)

    for parts in exist_parts:
        print(parts['component'], '-' * (30 - len(parts['component'])), parts['name'], '-' * (45 - len(parts['name'])), parts['price'])
    total_price = 0
    for parts in exist_parts:
        total_price += parts['price']
    print('Total Price', '-' * (45 - len('Total Price')), total_price)
    print('Remaining Budget', '-' * (45 - len('Remaining Budget')), parameter_List[1] - total_price)
    """"
    CPU:            'speed'         'cores'
    Cooler:         'fan-rpm'       'noise level'
    Motherboard:    'form-factor'   'ram-slots'
    Memory:         'speed'         'cas'           'modules'       'size'
    SSD:            'series'        'form'          'capacity'
    HDD:            'series'        'form'          'capacity'
    PSU:            'series'        'efficiency'    'watts'         'modular'
    GPU:            'series'        'chipset'
    case:           'type'
    """


def getCPU(compList, cpuList, user_para):
    '''
    '''
    CPU_PARAMETER = [
        'AMD Ryzen', 'Intel Core i3-8', 'Intel Core i5-8', 'Intel Core i7-87',
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
    cpu_user_para = []
    if user_para[2] == 3:
        for cpu in cpu_Dict:
            cpu_user_para.append(cpu)
    elif user_para[2] == 1:
        for cpu in cpu_Dict:
            if 'AMD' in cpu['name']:
                cpu_user_para.append(cpu)
    elif user_para[2] == 2:
        for cpu in cpu_Dict:
            if 'Intel' in cpu['name']:
                cpu_user_para.append(cpu)
    # Filter cpu brand according to user input parameter

    cpu_user = []
    if user_para[3] == 3:
        for cpu in cpu_user_para:
            cpu_user.append(cpu)
    elif user_para[3] == 1:
        for cpu in cpu_user_para:
            if 'K' in cpu['name'] or 'AMD' in cpu['name']:
                cpu_user.append(cpu)
    elif user_para[3] == 2:
        for cpu in cpu_user_para:
            if 'K' not in cpu['name']:
                cpu_user.append(cpu)
    # Filter cpu according to overclocking user input parameter

    for cpu in cpu_user:
        if type(cpu['price']) == float:
            continue
        else:
            cpu['price'] = float(cpu['price'].strip('$'))

    desktop_type = compList["name"]
    chosen_set = []
    if 'gen' in desktop_type:
        for cpu in cpu_user:
            if 'AMD' in cpu['name'] and 'G' in cpu['name']:
                chosen_set.append(cpu)
            if 'Intel' in cpu['name'] and 'F' not in cpu['name']:
                chosen_set.append(cpu)
    elif 'game' in desktop_type or 'ws' in desktop_type:
        for cpu in cpu_user:
            if 'AMD' in cpu['name'] and 'G' not in cpu['name']:
                chosen_set.append(cpu)
            if 'Intel' in cpu['name']:
                chosen_set.append(cpu)

    cpu_set = []
    for cpu in chosen_set:
        if cpu['price'] < compList['cpu']:
            cpu_set.append(cpu)
    # filter CPU within budget

    cpu_game_rank = ['i3', 'Ryzen 3', 'Ryzen 5', 'i5', 'Ryzen 7', 'i7', 'i9']
    cpu_other_rank = ['i3', 'Ryzen 3', 'i5', 'Ryzen 5', 'i7', 'Ryzen 7', 'i9']
    cpu_select_list = []
    list_index = len(cpu_game_rank) - 1
    if 'gen' in desktop_type or 'ws' in desktop_type:
        while len(cpu_select_list) == 0:
            for cpu in cpu_set:
                for rank in cpu_other_rank[list_index]:
                    if rank in cpu['name']:
                        cpu_select_list.append(cpu)
            list_index -= 1
    elif 'game' in desktop_type:
        while len(cpu_select_list) == 0:
            for cpu in cpu_set:
                for rank in cpu_game_rank[list_index]:
                    if rank in cpu['name']:
                        cpu_select_list.append(cpu)
            list_index -= 1

    # select CPU from CPU ranking list, select best SKU first

    cpu_p = []
    for cpu in cpu_select_list:
        cpu_p.append(cpu['price'])

    cpu_max = []
    for cpu in cpu_select_list:
        if cpu['price'] == max(cpu_p):
            cpu_max.append(cpu)
    chosen_cpu = cpu_max[0]
    chosen_cpu['component'] = 'CPU'

    option_list = ['1', '2']
    if 'Intel' in chosen_cpu['name'] and 'K' in chosen_cpu['name']:
        user_cooler_option = '1'
    else:
        user_cooler_option = '0'
        while user_cooler_option not in option_list:
            print('Option 1 -- YES')
            print('Option 2 -- NO')
            user_cooler_option = input('Do you want an aftermarket CPU cooler?')
            if user_cooler_option not in option_list:
                print('***Invalid Option***')
                print('***Please Try Again***')
            #user_cooler_option = '1'
    return chosen_cpu, int(user_cooler_option)


def getmobo(compList, mobo_info, chosen_cpu, user_input):
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
            )  # alternative list of motherboard, filtered by price only

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

    mobo_user = []
    if user_input == 1:
        for mobo in mobo_set:
            if mobo['form-factor'] == 'Micro ATX':
                mobo_user.append(mobo)
    elif user_input == 2:
        for mobo in mobo_set:
            if mobo['form-factor'] == 'ATX':
                mobo_user.append(mobo)
    elif user_input == 3:
        for mobo in mobo_set:
            if mobo['form-factor'] == 'Micro ATX' or mobo[
                    'form-factor'] == 'ATX':
                mobo_user.append(mobo)
    # Filter motherboard size by user input

    mobo_p = []
    for motherboard in mobo_user:
        mobo_p.append(motherboard['price'])

    mobo_list = []
    for mobo in mobo_user:
        if mobo['price'] > 0.9 * (max(mobo_p)):
            mobo_list.append(mobo)
    # pick motherboards within highest 10% price budget

    chosen_motherboard = random.choice(mobo_list)
    chosen_motherboard['component'] = 'Motherboard'
    # choose a random motherboard from the list
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
    for ram in ram_select_set:
        if ram['speed'] == max(ram_speed_list):
            ram_speed_module.append(ram)
    #filter the ram modules with the maximum speed

    ram_price_list = []
    for ram in ram_speed_module:
        ram_price_list.append(ram['price'])

    ram_price_modules = []
    for ram in ram_speed_module:
        if ram['price'] < 1.15 * (min(ram_price_list)):
            ram_price_modules.append(ram)
    # pick ram modules within 15% price difference of cheapest module

    chosen_ram = random.choice(ram_price_modules)
    chosen_ram['component'] = 'Memory'
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
            'capacity'] > 900:
        selected_hdd = hdd_min_price[0]
        remaining_budget = compList['storage'] - selected_ssd[
            'price'] - selected_hdd['price']
    else:
        selected_hdd = 'NO HDD'
        remaining_budget = compList['storage'] - selected_ssd['price']
    # filter a single HDD from filtered set

    selected_ssd['component'] = 'SSD'
    if isinstance(selected_hdd, dict) == True:
        selected_hdd['component'] = 'HDD'

    return selected_ssd, selected_hdd, remaining_budget


def getpsu(compList, psu_info):
    psu_dict = []
    for psu in psu_info:
        if '80+' in psu['efficiency'] and psu['price'] != '' and psu[
                'form'] == 'ATX':
            psu_dict.append(psu)
    # filter psu in ATX form-factor, minimum 80+ efficiency, and with a price

    for psu in psu_dict:
        if type(psu['price']) != float:
            psu['price'] = float(psu['price'].strip('$'))
        if type(psu['watts']) != float:
            psu['watts'] = float(psu['watts'].strip(' W'))
    # turn price and watts into float for further processing

    psu_brand = ['EVGA', 'Corsair', 'SeaSonic']
    psu_brand_list = []
    for psu in psu_dict:
        for brands in psu_brand:
            if brands in psu['name']:
                psu_brand_list.append(psu)
    # filter PSU limiting to the 3 most reputable brands

    psu_list = []
    if compList['gpu'] > 0:
        for psu in psu_brand_list:
            if 1000 >= psu['watts'] >= 550:
                psu_list.append(psu)
    else:
        for psu in psu_brand_list:
            if 600 >= psu['watts'] >= 300:
                psu_list.append(psu)
    #filter PSU wattage base on whether the build has a GPU or not, and limit maximum and minimum

    psu_budget_list = []
    for psu in psu_list:
        if psu['price'] < compList['psu']:
            psu_budget_list.append(psu)
    #filter out price that is out of budget

    efficiency_index_max = 3
    efficiency_rank = ['Bronze', 'Gold', 'Platinum', 'Titanium']
    psu_eff_list = []
    while len(psu_eff_list) == 0:
        for psu in psu_budget_list:
            if efficiency_rank[efficiency_index_max] in psu['efficiency']:
                psu_eff_list.append(psu)
        efficiency_index_max -= 1

    modular_index_max = 2
    modular_rank = ['No', 'Semi', 'Full']
    psu_mod_list = []
    while len(psu_mod_list) == 0:
        for psu in psu_eff_list:
            if modular_rank[modular_index_max] == psu['modular']:
                psu_mod_list.append(psu)
        modular_index_max -= 1
    #filter our a list of best efficiency

    psu_watt = []
    for psu in psu_mod_list:
        psu_watt.append(psu['watts'])

    psu_watt_list = []
    for index, watt in enumerate(psu_watt, 0):
        if watt == max(psu_watt):
            psu_watt_list.append(psu_mod_list[index])
    # filter to PSU with highest wattage

    psu_price = []
    for psu in psu_watt_list:
        psu_price.append(psu['price'])

    psu_price_list = []
    for index, price in enumerate(psu_price, 0):
        if price == min(psu_price):
            psu_price_list.append(psu_watt_list[index])
    # filter to PSU with minimum price

    chosen_psu = psu_price_list[0]
    chosen_psu['component'] = 'Power Supply'
    return chosen_psu


def getgpu(compList, gpu_info, extra_budget, choice):
    if compList['gpu'] == 0:
        chosen_gpu = 'No GPU'
    else:
        gpu_dict = []
        for gpu in gpu_info:
            if gpu['price'] != '':
                gpu_dict.append(gpu)
        # filter out the gpu without a price

        new_gpu_list = [
            'Radeon RX 560 - 896', 'Radeon RX 560 - 1024', 'Radeon RX 570',
            'GeForce GTX 1660', 'Radeon RX 580', 'GeForce GTX 1660 Ti',
            'GeForce RTX 2060', 'GeForce RTX 2070', 'GeForce RTX 2080',
            'GeForce RTX 2080 Ti'
        ]
        gpu_chipset_index = len(new_gpu_list) - 1
        # list the new chipset, with ascending performance ranking
        # index will be used later for filter

        gpu_new_list = []
        for gpu in gpu_dict:
            for chipset in new_gpu_list:
                if gpu['chipset'] == chipset:
                    gpu_new_list.append(gpu)
        # filter down to GPU with new chipset only

        for gpu in gpu_new_list:
            if type(gpu['price']) != float:
                gpu['price'] = float(gpu['price'].strip('$'))
            if type(gpu['memory']) != float:
                gpu['memory'] = float(gpu['memory'].strip(' GB'))
        # moving string value and turning price and memory into float for further processing

        gpu_choice_list = []
        if choice == 3:
            for gpu in gpu_new_list:
                gpu_choice_list.append(gpu)
        elif choice == 2:
            for gpu in gpu_new_list:
                if 'Radeon' in gpu['chipset']:
                    gpu_choice_list.append(gpu)
        elif choice == 1:
            for gpu in gpu_new_list:
                if 'GeForce' in gpu['chipset']:
                    gpu_choice_list.append(gpu)
        #filter out GPU by user input

        temp_gpu_budget_list = []
        temp_gpu_budget_index = gpu_chipset_index
        temp_gpu_extra_list = []
        temp_gpu_extra_index = gpu_chipset_index

        while len(temp_gpu_extra_list) == 0:
            for gpu in gpu_choice_list:
                if (compList['gpu'] + extra_budget*1.1) > gpu['price']:
                    if new_gpu_list[temp_gpu_extra_index] == gpu['chipset']:
                        temp_gpu_extra_list.append(gpu)
            temp_gpu_extra_index -= 1

        while len(temp_gpu_budget_list) == 0:
            for gpu in gpu_choice_list:
                if compList['gpu'] > gpu['price']:
                    if new_gpu_list[temp_gpu_budget_index] == gpu['chipset']:
                        temp_gpu_budget_list.append(gpu)
            temp_gpu_budget_index -= 1

        gpu_budget_list = []
        if temp_gpu_extra_index > temp_gpu_budget_index:
            for gpu in temp_gpu_extra_list:
                gpu_budget_list.append(gpu)
            extra_budget_usage = 1
        else:
            for gpu in temp_gpu_budget_list:
                gpu_budget_list.append(gpu)
            extra_budget_usage = 0

        # use the left-over budget from other components and try to get a better GPU
        # the ranking of chipset is used to compare if the extra budget allow a significant upgrade
        # extra budget is used only when there is a significant upgrade

        gpu_mem = []
        for gpu in gpu_budget_list:
            gpu_mem.append(gpu['memory'])

        gpu_mem_list = []
        for gpu in gpu_budget_list:
            if gpu['memory'] == max(gpu_mem):
                gpu_mem_list.append(gpu)
        # filter to GPU with most memory

        gpu_price = []
        for gpu in gpu_mem_list:
            gpu_price.append(gpu['price'])

        gpu_price_list = []
        for gpu in gpu_mem_list:
            if gpu['price'] == min(gpu_price):
                gpu_price_list.append(gpu)
        # filter to GPU with minimum price

        chosen_gpu = gpu_price_list[0]
        if isinstance(chosen_gpu, dict) == True:
            chosen_gpu['component'] = 'Video Card'

    return chosen_gpu


def getcooler(compList, cooler_info, extra_budget, cooler_option, chosen_gpu):
    if cooler_option == 0:
        chosen_cooler = 'No after market cooler'
    else:
        pre_selected_list = [
            'Hyper 212 EVO', 'CRYORIG M9 Plus', 'Scythe - Ninja 5',
            'CRYORIG R1', 'NH-D15', 'Dark Rock Pro 4'
        ]
        # a pre_select list of reputable CPU cooler, with ranking ascending

        cooler_list = []
        for cooler in cooler_info:
            for preset in pre_selected_list:
                if cooler['price'] != '' and preset in cooler['name']:
                    cooler_list.append(cooler)
        # filter cooler without a price and cooler in pre-selected list

        for cooler in cooler_list:
            if type(cooler['price']) != float:
                cooler['price'] = float(cooler['price'].strip('$'))
        # converting price to float for further processing

        if compList['gpu'] == 0:
            cooler_budget = extra_budget
        else:
            cooler_budget = extra_budget + compList['gpu'] - chosen_gpu['price']

        cooler_budget_list = []
        for cooler in cooler_list:
            if cooler['price'] < cooler_budget * 1.35:
                cooler_budget_list.append(cooler)
        # add after market cooler that is within budget

        if len(cooler_budget_list) == 0:
            cooler_price = []
            for cooler in cooler_list:
                cooler_price.append(cooler['price'])

            cooler_price_list = []
            for cooler in cooler_list:
                if cooler['price'] == min(cooler_price):
                    cooler_price_list.append(cooler)
            # filter to cooler with minimum price
            cooler_budget_list.append(cooler_price_list[0])

        # add an after market cooler with minimum price from the list if the budget is insufficient

        cooler_p = []
        cooler_p_list = []
        for cooler in cooler_budget_list:
            cooler_p.append(cooler['price'])

        for cooler in cooler_budget_list:
            if cooler['price'] > 0.75 * max(cooler_p):
                cooler_p_list.append(cooler)
        chosen_cooler = random.choice(cooler_p_list)

        if isinstance(chosen_cooler, dict) == True:
            chosen_cooler['component'] = 'CPU Cooler'
    return chosen_cooler


def getcase(compList, case_info, chosen_mobo):
    case_list = []
    for case in case_info:
        if chosen_mobo['form-factor'] != 'ATX':
            if 'MicroATX' in case['type'] and case['price'] != '':
                case_list.append(case)
        else:
            if 'Test' not in case['type'] and 'Micro' not in case[
                    'type'] and 'ATX' in case['type'] and case['price'] != '':
                case_list.append(case)
    # Filter case based on motherboard size and remove items with empty price

    for case in case_list:
        if type(case['price']) != float:
            case['price'] = float(case['price'].strip('$'))
        if type(case['ratings']) != float:
            case['ratings'] = float(case['ratings'])
    # Turn price and rating into float for further processing

    case_nocd_list = []
    for case in case_list:
        if case['ext525b'] == '0' and case['price'] < compList['case']:
            case_nocd_list.append(case)
    # Filter to case within budget and without DVD drive bay

    case_brands = [
        'Phanteks', 'NZXT', 'Lian-Li', 'Silverstone', 'Cooler Master',
        'Fractal Design', 'Corsair', 'Antec - TORQUE', 'Cougar Conquer'
    ]
    case_sub_brands = ['Thermaltake', 'Rosewill', 'GAMDIAS']
    case_brand_list = []
    for case in case_nocd_list:
        for brand in case_brands:
            if brand in case['name']:
                case_brand_list.append(case)
    # Filter case from reputable brands

    if len(case_brand_list) == 0:
        for case in case_nocd_list:
            for brand in case_sub_brands:
                if brand in case['name']:
                    case_brand_list.append(case)
    # If no case available from reputable brands, use sub-par brands

    case_p = []
    for case in case_brand_list:
        case_p.append(case['price'])

    case_p_list = []
    for case in case_brand_list:
        if case['price'] > 0.75 * (max(case_p)):
            case_p_list.append(case)
    # pick case within highest 25% price budget

    chosen_case = random.choice(case_p_list)
    chosen_case['component'] = 'Computer Case'
    return chosen_case


