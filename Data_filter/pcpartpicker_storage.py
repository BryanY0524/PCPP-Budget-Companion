from PCPartPicker_API import pcpartpicker as pcpp

# sets region to Canada.. all prices now will be CDN dollar
pcpp.setRegion('ca')

# collects all the list of storage available in PCpartpicker website
storage_info_ca = pcpp.productLists.getProductList('internal-hard-drive')
filtered_storage_list = list()
for storage in storage_info_ca:
        # makes sure that all storage stored in the new list has its own prices
        if storage['price'] != '':
            filtered_storage_list.append(storage)

for storage in filtered_storage_list:
        storage['price'] = format(float(storage['price'].strip('$')))

for storage in filtered_storage_list:
    for keys, values in storage.items():
        print(keys, ':', values)
    print('*********************************************************************************')
print(len(storage_info_ca))
print(len(filtered_storage_list))
print('Total products removed:', len(storage_info_ca)-len(filtered_storage_list))
