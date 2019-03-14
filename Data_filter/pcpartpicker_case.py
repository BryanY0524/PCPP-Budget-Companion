from PCPartPicker_API import pcpartpicker as pcpp

# sets region to Canada.. all prices now will be CDN dollar
pcpp.setRegion('ca')

# collects all the list of case available in PCpartpicker website
case_info_ca = pcpp.productLists.getProductList('case')
filtered_case_list = list()

for case in case_info_ca:
    # makes sure that all case stored in the new list has its own prices
    if case['price'] != '':
        filtered_case_list.append(case)

for case in filtered_case_list:
        case['price'] = format(float(case['price'].strip('$')))
        
for case in filtered_case_list:
    for keys, values in case.items():
        print(keys, ':', values)
    print('****************************************************************')

print(len(case_info_ca))
print(len(filtered_case_list))
print('Total products removed:', len(case_info_ca)-len(filtered_case_list))
