from PCPartPicker_API import pcpartpicker as pcpp


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
        if type(cpu['price']) == float:
            continue
        else:
            cpu['price'] = float(cpu['price'].strip('$'))

    desktop_type = compList["name"]
    chosen_set = []
    if 'gen' in desktop_type:
        for cpu in cpu_dict:
            if 'AMD' in cpu['name'] and 'G' in cpu['name']:
                chosen_set.append(cpu)
            if 'Intel' in cpu['name'] and 'F' not in cpu['name']:
                chosen_set.append(cpu)
    elif 'game' in desktop_type or 'ws' in desktop_type:
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


def getmobo(compList, mobo_info, chosen_cpu):
    '''
    '''
    # Special ASUS motherboard from 8th gen that support 9th gen intel CPU
    ASUS_INTEL9 = ['STRIX Z370-E', 'STRIX Z370-F', 'STRIX Z370-H',
                   'STRIX Z370-G', 'PRIME Z370-A', 'TUF Z370-PRO GAMING',
                   'TUF Z370-PLUS GAMING', 'PRIME Z370-P', 'STRIX Z370-I',
                   'ROG MAXIMUS X ', 'STRIX H370-F', 'STRIX H370-I',
                   'TUF H370-PRO GAMING', 'PRIME H370-A', 'PRIME H370-PLUS',
                   'PRIME H370M-PLUS', 'STRIX B360-H GAMING',
                   'STRIX B360-F GAMING', 'STRIX B360-G GAMING',
                   'STRIX B360-I GAMING', 'TUF B360-PRO GAMING',
                   'TUF B360-PLUS GAMING', 'TUF B360M-E GAMING',
                   'TUF B360M-PLUS GAMING', 'PRIME B360-PLUS', 'PRIME B360M-A',
                   'PRIME B360M-C', 'PRIME B360M-D', 'PRIME B360M-K',
                   'EX-B360M-V', 'TUF H310-PLUS GAMING', 'PRIME H310-PLUS',
                   'TUF H310M-PLUS GAMING', 'PRIME H310M-A', 'PRIME H310M-C',
                   'PRIME H310I-PLUS', 'PRIME H310M-E', 'PRIME H310M-K',
                   'PRIME H310M-D', 'PRIME H310T']

    GIGA_INTEL9 = ['Z370 AORUS', 'Z370 HD3', 'Z370M D3H', 'Z370M DS3H',
                   'Z370N WIFI', 'Z370P D3', 'Z370 UD3H', 'Z370XP SLI',
                   'H370 AORUS GAMING 3', 'H370M D3H', 'H370M DS3H',
                   'H370M D3H', 'H370 HD3', 'H370N WIFI', 'B360 AORUS',
                   'B360 HD3', 'B360M GAMING', 'B360 HD3P', 'B360M D2V',
                   'B360M D3H', 'B360M D3P', 'B360M D3V', 'B360M DS3H',
                   'B360M H', 'B360M HD3', 'B360N WIFI', 'H310M S2H',
                   'H310M DS2', 'H310 D3', 'H310M A', 'H310M H', 'H310M S2',
                   'H310N']
    # Special Gigabyte motherboard from 8th gen that support 9th gen intel CPU

    MSI_INTEL9 = ['MSI B360 GAMING', 'MSI B360-A PRO', 'MSI B360M BAZOOKA',
                  'MSI B360I GAMING PRO AC', 'MSI B360M GAMING',
                  'MSI B360M MORTAR', 'MSI B360M PRO-V', 'MSI H310-A PRO',
                  'MSI H310I PRO', 'MSI H310M GAMING', 'MSI H310M PRO-',
                  'MSI H370 GAMING', 'MSI H370M BAZOOKA', 'MSI Z370 GAMING',
                  'MSI Z370 GODLIKE', 'MSI Z370 KRAIT', 'MSI Z370 PC PRO',
                  'MSI Z370 SLI PLUS', 'MSI Z370 TOMAHAWK', 'MSI Z370-A PRO',
                  'MSI Z370I GAMING PRO', 'MSI Z370M GAMING PRO',
                  'MSI Z370M MORTAR']
    # Special MSI motherboard from 8th gen that support 9th gen intel CPU

    ASROCK_INTEL9 = ['ASRock Z370M-ITX/ac', 'ASRock Z370M Pro4',
                     'ASRock Z370 Taichi', 'ASRock Z370 Pro4',
                     'ASRock Z370 Killer SLI', 'ASRock Z370 Extreme4',
                     'ASRock H370M-ITX/ac', 'ASRock H370M Pro4',
                     'ASRock H370 Pro4', 'ASRock H310M-ITX/ac',
                     'ASRock H310M-HDV', 'ASRock H310M-G/M.2',
                     'ASRock H310M-DGS', 'ASRock Fatal1ty Z370',
                     'ASRock Fatal1ty H370 Performance',
                     'ASRock Fatal1ty B360 Gaming K4', 'ASRock B360M-ITX/ac',
                     'ASRock B360M-HDV', 'ASRock B360M Pro4',
                     'ASRock B360M Performance', 'ASRock B360 Pro4']
    # Special ASROCK motherboard from 8th gen that support 9th gen intel CPU

    INTEL_9_BASE = ['Z390', 'Asus ROG MAXIMUS XI ']
    # Basic motherboard chipset that support Intel 9th gen CPU

    intel_9_para = INTEL_9_BASE + ASUS_INTEL9 + \
        GIGA_INTEL9 + MSI_INTEL9 + ASROCK_INTEL9
    # Parameter for all motherboard that support intel 9th gen CPU

    intel_8_para = ['Z370', 'H310', 'H370', 'Z390', 'B360',
                    'Asus ROG MAXIMUS X ', 'Asus ROG MAXIMUS XI ']
    # Parameter for all motherboard that support intel 8th gen CPU

    amd_para = ['A320', 'B350', 'B450', 'X370', 'X470', 'Asus CROSSHAIR VI ']
    # Parameter for all motherboard that support AMD Ryzen CPU

    intel_8_cpu = ['Intel Core i3-8', 'Intel Core i5-8', 'Intel Core i7-8']
    intel_9_cpu = ['Intel Core i3-9', 'Intel Core i5-9',
                   'Intel Core i7-9700', 'Intel Core i9-9900K']
    amd_cpu = ['AMD Ryzen']
    # list of names to identify CPU brand and series

    cpu_model = [intel_8_cpu, intel_9_cpu, amd_cpu]
    motherboard_for_cpu = [intel_8_para, intel_9_para, amd_para]

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
            mobo_dict_budget.append(motherboard)  # alternative list of motherboard, filtered by price

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
            mobo_set.append(motherboard)  # use alternative list if the optimal list is empty

    mobo_p = []
    for motherboard in mobo_set:
        mobo_p.append(motherboard['price'])

    # pick highest value within budget
    chosen_motherboard = mobo_set[mobo_p.index(max(mobo_p))]
    return chosen_motherboard
