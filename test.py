cpu_dict = [
    {'name': 'Intel Core i3-8300', 'speed': '3.7 GHz', 'cores': '4', 'tdp': '62 W', 'ratings': '1',
     'price': 199.99, 'id': 'r3m323'},
    {'name': 'Intel Core i5-8400', 'speed': '2.8 GHz', 'cores': '6', 'tdp': '65 W', 'ratings': '65',
     'price': 237.0, 'id': 'LHYWGX'},
    {'name': 'Intel Core i5-8600K', 'speed': '3.6 GHz', 'cores': '6', 'tdp': '95 W',
     'ratings': '119', 'price': 339.98, 'id': 'Mr2rxr'},
    {'name': 'Intel Core i5-8500', 'speed': '3 GHz', 'cores': '6', 'tdp': '65 W', 'ratings': '5',
     'price': 288.5, 'id': 'kFKcCJ'},
    {'name': 'Intel Core i5-8600', 'speed': '3.1 GHz', 'cores': '6', 'tdp': '65 W', 'ratings': '3',
     'price': 309.99, 'id': 'XMTPxr'},
    {'name': 'Intel Core i7-8700K', 'speed': '3.7 GHz', 'cores': '6', 'tdp': '95 W',
     'ratings': '215', 'price': 499.0, 'id': 'sxDzK8'},
    {'name': 'Intel Core i7-8700', 'speed': '3.2 GHz', 'cores': '6', 'tdp': '65 W', 'ratings': '36',
     'price': 432.5, 'id': 'C9hj4D'},
    {'name': 'Intel Core i7-8086K', 'speed': '4 GHz', 'cores': '6', 'tdp': '95 W', 'ratings': '12',
     'price': 639.65, 'id': 'CgqhP6'},
    {'name': 'Intel Core i5-9600K', 'speed': '3.7 GHz', 'cores': '6', 'tdp': '95 W',
     'ratings': '25', 'price': 329.0, 'id': '28qhP6'},
    {'name': 'Intel Core i7-9700K', 'speed': '3.6 GHz', 'cores': '8', 'tdp': '95 W',
     'ratings': '25', 'price': 529.99, 'id': 'WtyV3C'},
    {'name': 'Intel Core i9-9900K', 'speed': '3.6 GHz', 'cores': '8', 'tdp': '95 W',
     'ratings': '23', 'price': 689.99, 'id': 'jHZFf7'}]

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

for index, cpu in enumerate(chosen_set):
    if cpu['price'] > comp_bud_list['cpu']:
        chosen_set.pop(index)


for item in chosen_set:
    print(item)
