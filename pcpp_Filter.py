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
