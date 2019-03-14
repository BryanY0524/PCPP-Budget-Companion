from PCPartPicker_API import pcpartpicker as pcpp

# sets region to Canada.. all prices now will be CDN dollar
pcpp.setRegion('ca')

# collects all the list of psu available in PCpartpicker website
psu_info_ca = pcpp.productLists.getProductList('power-supply')
psu_efficiency_para = ['80+']
filtered_psu_list = list()
for efficiency in psu_efficiency_para:
    for psu in psu_info_ca:
        if efficiency in psu['efficiency']:
            # makes sure that all psu stored in the new list has its own prices
            if psu['price'] != '':
                filtered_psu_list.append(psu)

for psu in filtered_psu_list:
        psu['price'] = format(float(psu['price'].strip('$')))

for psu in filtered_psu_list:
    for keys, values in psu.items():
        print(keys, ':', values)
    print('**********************************************************************************')
print(len(psu_info_ca))
print(len(filtered_psu_list))
print('Total products removed:', len(psu_info_ca)-len(filtered_psu_list))
