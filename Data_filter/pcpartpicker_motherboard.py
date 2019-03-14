from PCPartPicker_API import pcpartpicker as pcpp

pcpp.setRegion('ca') #sets region to Canada.. all prices now will be CDN dollar

motherboard_info_ca = pcpp.productLists.getProductList('motherboard') # collects all the list of motherboards available in PCpartpicker website
socket_para = ['LGA1150','LGA2066','LGA1151','AM4','TR4',]
filtered_motherboard_list = list() #empty list where all filtered motherboards will be stored
for socket in socket_para:
    for motherboard in motherboard_info_ca:
        if socket in motherboard['socket']:
            if motherboard['price'] != '': #makes sure that all motherboard stored in the new list has its own prices
                #print(cpu['name'], ':', cpu['price'])
                #print('***************************************')
                filtered_motherboard_list.append(motherboard)

for motherboard in filtered_motherboard_list:
        motherboard['price'] = format(float(motherboard['price'].strip('$')))

for motherboard in filtered_motherboard_list:
    for keys, values in motherboard.items():
        print(keys, ':', values)
    print('**********************************')
print(len(motherboard_info_ca))
print(len(filtered_motherboard_list))
print('Total products removed:', len(motherboard_info_ca)-len(filtered_motherboard_list))

