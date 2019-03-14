from PCPartPicker_API import pcpartpicker as pcpp

pcpp.setRegion("ca")

cpu_para = ['AMD Ryzen', 'Intel Core i3-8', 'Intel Core i5-8', 'Intel Core i7-8', 'Intel Core i3-9',
            'Intel Core i5-9', 'Intel Core i7-9700', 'Intel Core i9-9900K']

cpu_ex = 'OEM'
cpu_info = pcpp.productLists.getProductList("cpu")
cpu_dict = []

for model in cpu_para:
    for cpu in cpu_info:
        if model in cpu['name']:
            if cpu_ex not in cpu['name']:
                if cpu['price'] != '':
                    cpu_dict.append(cpu)

for cpu in cpu_dict:
    cpu['price'] = float(cpu['price'].strip('$'))

comp_bud_list = {'name': 'ws1', 'cpu': 450.0, 'motherboard': 165.0, 'memory': 180.0,
                 'gpu': 300.0, 'storage': 150.0, 'psu': 105.0, 'case': 150.0}

type = 'game'
chosen_set = []
if type == 'gen':
    for cpu in cpu_dict:
        if 'AMD' in cpu['name'] and 'G' in cpu['name']:
            chosen_set.append(cpu)
        if 'Intel' in cpu['name'] and 'F' not in cpu['name']:
            chosen_set.append(cpu)
elif type == 'game' or type == 'ws':
    for cpu in cpu_dict:
        if 'AMD' in cpu['name'] and 'G' not in cpu['name']:
            chosen_set.append(cpu)
        if 'Intel' in cpu['name']:
            chosen_set.append(cpu)

for i in range(2):
    for index, cpu in enumerate(chosen_set):
        if cpu['price'] > comp_bud_list['cpu']:
            chosen_set.pop(index)

cpu_p = []
for i in chosen_set:
    cpu_p.append(i['price'])

chosen_cpu = chosen_set[cpu_p.index(max(cpu_p))]

print(chosen_cpu)