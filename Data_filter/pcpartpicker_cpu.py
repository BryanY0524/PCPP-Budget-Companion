from PCPartPicker_API import pcpartpicker as pcpp

#set region as Canada
pcpp.setRegion('ca')
#set parameter for all latest desktop cpu`s for both AMD and INTEL
cpu_para = ['AMD Ryzen', 'Intel Core i3-6', 'Intel Core i5-6',
            'Intel Core i7-6','Intel Core i3-7', 'Intel Core i5-7', 'Intel Core i7-7',
            'Intel Core i3-8', 'Intel Core i5-8', 'Intel Core i7-8',
            'Intel Core i3-9', 'Intel Core i5-9', 'Intel Core i7-9',
             'Intel Core i9-9900K', 'Intel Core i9-7', 'Intel Core i9-99']
cpu_info_ca = pcpp.productLists.getProductList('cpu')
filtered_cpu_list = list() #empty list to store all filtered cpu product
for model in cpu_para:
    for cpu in cpu_info_ca:
        if model in cpu['name']:
            if cpu['price'] != '': # Since we need all a product that has prices, product that doesnt have prices needs to be filtered
                #print(cpu['name'], ':', cpu['price'])
                #print('***************************************')
                filtered_cpu_list.append(cpu)
for cpu in filtered_cpu_list:
        cpu['price'] = format(float(cpu['price'].strip('$')))
for cpu in filtered_cpu_list:
    for keys, values in cpu.items():
        print(keys , ':' , values)
    print('*********************************************')

print(len(cpu_info_ca))
print(len(filtered_cpu_list))
print('Total products removed:', len(cpu_info_ca)-len(filtered_cpu_list))
