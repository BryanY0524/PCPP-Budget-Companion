from PCPartPicker_API import pcpartpicker as pcpp

# sets region to Canada.. all prices now will be CDN dollar
pcpp.setRegion('ca')

# collects all the list of ram available in PCpartpicker website
ram_info_ca = pcpp.productLists.getProductList('memory')
filtered_ram_list = list()
for ram in ram_info_ca:
        # makes sure that all ram stored in the new list has its own prices
        if ram['price'] != '':
            filtered_ram_list.append(ram)

for ram in filtered_ram_list:
        ram['price'] = format(float(ram['price'].strip('$')))
    
for ram in filtered_ram_list:
    for keys, values in ram.items():
        print(keys, ':', values)
    print('*******************************************************************************')
print(len(ram_info_ca))
print(len(filtered_ram_list))
print('Total products removed:', len(ram_info_ca)-len(filtered_ram_list))

print("Total ram pages:", pcpp.productLists.totalPages("memory"))
for ram in ram_info_ca:
    print(ram,',')