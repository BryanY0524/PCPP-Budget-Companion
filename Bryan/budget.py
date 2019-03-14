budget_list = [{
    'name': 'gen1',
    'cpu': 0.35,
    'motherboard': 0.15,
    'memory': 0.15,
    'gpu': 0,
    'storage': 0.15,
    'psu': 0.10,
    'case': 0.10
},
               {
                   'name': 'gen2',
                   'cpu': 0.35,
                   'motherboard': 0.12,
                   'memory': 0.15,
                   'gpu': 0,
                   'storage': 0.20,
                   'psu': 0.08,
                   'case': 0.10
               },
               {
                   'name': 'game1',
                   'cpu': 0.25,
                   'motherboard': 0.12,
                   'memory': 0.12,
                   'gpu': 0.25,
                   'storage': 0.10,
                   'psu': 0.08,
                   'case': 0.08
               },
               {
                   'name': 'game2',
                   'cpu': 0.22,
                   'motherboard': 0.11,
                   'memory': 0.12,
                   'gpu': 0.28,
                   'storage': 0.10,
                   'psu': 0.07,
                   'case': 0.10
               },
               {
                   'name': 'game3',
                   'cpu': 0.25,
                   'motherboard': 0.11,
                   'memory': 0.10,
                   'gpu': 0.30,
                   'storage': 0.09,
                   'psu': 0.07,
                   'case': 0.08
               },
               {
                   'name': 'game4',
                   'cpu': 0.22,
                   'motherboard': 0.09,
                   'memory': 0.08,
                   'gpu': 0.39,
                   'storage': 0.09,
                   'psu': 0.05,
                   'case': 0.08
               },
               {
                   'name': 'ws1',
                   'cpu': 0.30,
                   'motherboard': 0.11,
                   'memory': 0.12,
                   'gpu': 0.20,
                   'storage': 0.10,
                   'psu': 0.07,
                   'case': 0.10
               },
               {
                   'name': 'ws2',
                   'cpu': 0.28,
                   'motherboard': 0.08,
                   'memory': 0.20,
                   'gpu': 0.20,
                   'storage': 0.09,
                   'psu': 0.07,
                   'case': 0.08
               },
               {
                   'name': 'ws3',
                   'cpu': 0.25,
                   'motherboard': 0.09,
                   'memory': 0.12,
                   'gpu': 0.28,
                   'storage': 0.14,
                   'psu': 0.05,
                   'case': 0.07
               }]
type = 'game'
budget = 1300
comp_bud_list = 0

for set in budget_list:
    for item in set:
        if set[item] != set['name']:
            set[item] = set[item] * budget

if type == 'game':
    if 1500 > budget > 1000:
        comp_bud_list = budget_list[5]
elif type == 'gen':
    if 1500 > budget > 1000:
        comp_bud_list = budget_list[5]

elif type == 'ws':
    if 1500 > budget > 1000:
        comp_bud_list = budget_list[5]

print(comp_bud_list)
