from PCPartPicker_API import pcpartpicker as pcpp

# sets region to Canada.. all prices now will be CDN dollar
pcpp.setRegion('ca')

# collects all the list of gpu available in PCpartpicker website
gpu_chipset_para = ['Fire', 'Quadro', 'Radeon HD', 'Radeon 9550', 'Radeon Pro', 'Radeon R7', 'Radeon R9', 'Vega Frontier']
gpu_info_ca = pcpp.productLists.getProductList('video-card')
filtered_gpu_list = list()

for chipset in gpu_chipset_para:
    for gpu in gpu_info_ca:
        if chipset not in gpu['chipset']:
            # makes sure that all gpu stored in the new list has its own prices
            if gpu['price'] != '':
                filtered_gpu_list.append(gpu)

for gpu in filtered_gpu_list:
        gpu['price'] = format(float(gpu['price'].strip('$')))

for gpu in filtered_gpu_list:
    for keys, values in gpu.items():
        print(keys, ':', values)
    print('**********************************')

print(len(gpu_info_ca))
print(len(filtered_gpu_list))
print('Total products removed:', len(gpu_info_ca)-len(filtered_gpu_list))
