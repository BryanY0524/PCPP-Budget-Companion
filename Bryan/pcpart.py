from PCPartPicker_API import pcpartpicker as pcpp

pcpp.setRegion("ca")

print("Total CPU pages:", pcpp.productLists.totalPages("cpu"))
cpu_para = ['AMD Ryzen', 'Intel Core i3-8', 'Intel Core i5-8', 'Intel Core i7-8', 'Intel Core i3-9',
            'Intel Core i5-9', 'Intel Core i7-9', 'Intel Core i9-9900K']

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

print(len(cpu_info))
for item in cpu_dict:
    print(item)