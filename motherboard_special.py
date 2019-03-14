from PCPartPicker_API import pcpartpicker as pcpp

pcpp.setRegion("ca")

print("Total motherboard pages:", pcpp.productLists.totalPages("motherboard"))
mobo_info = pcpp.productLists.getProductList("motherboard")

asus_intel9 = ['STRIX Z370-E', 'STRIX Z370-F', 'STRIX Z370-H', 'STRIX Z370-G', 'PRIME Z370-A',
               'TUF Z370-PRO GAMING', 'TUF Z370-PLUS GAMING', 'PRIME Z370-P', 'STRIX Z370-I',
               'ROG MAXIMUS X ', 'STRIX H370-F', 'STRIX H370-I', 'TUF H370-PRO GAMING',
               'PRIME H370-A', 'PRIME H370-PLUS', 'PRIME H370M-PLUS', 'STRIX B360-H GAMING',
               'STRIX B360-F GAMING', 'STRIX B360-G GAMING', 'STRIX B360-I GAMING',
               'TUF B360-PRO GAMING', 'TUF B360-PLUS GAMING', 'TUF B360M-E GAMING',
               'TUF B360M-PLUS GAMING', 'PRIME B360-PLUS', 'PRIME B360M-A', 'PRIME B360M-C',
               'PRIME B360M-D', 'PRIME B360M-K', 'EX-B360M-V', 'TUF H310-PLUS GAMING',
               'PRIME H310-PLUS', 'TUF H310M-PLUS GAMING', 'PRIME H310M-A', 'PRIME H310M-C',
               'PRIME H310I-PLUS', 'PRIME H310M-E', 'PRIME H310M-K', 'PRIME H310M-D', 'PRIME H310T']

giga_intel9 = ['Z370 AORUS', 'Z370 HD3', 'Z370M D3H', 'Z370M DS3H', 'Z370N WIFI', 'Z370P D3',
               'Z370 UD3H', 'Z370XP SLI', 'H370 AORUS GAMING 3', 'H370M D3H', 'H370M DS3H',
               'H370M D3H', 'H370 HD3', 'H370N WIFI', 'B360 AORUS', 'B360 HD3', 'B360M GAMING',
               'B360 HD3P', 'B360M D2V', 'B360M D3H', 'B360M D3P', 'B360M D3V', 'B360M DS3H',
               'B360M H', 'B360M HD3', 'B360N WIFI', 'H310M S2H', 'H310M DS2', 'H310 D3', 'H310M A',
               'H310M H', 'H310M S2', 'H310N']

msi_intel9 = ['MSI B360 GAMING', 'MSI B360-A PRO', 'MSI B360I GAMING PRO AC', 'MSI B360M BAZOOKA',
              'MSI B360M GAMING', '	MSI B360M MORTAR', 'MSI B360M PRO-V', 'MSI H310-A PRO',
              'MSI H310I PRO', 'MSI H310M GAMING', 'MSI H310M PRO-', 'MSI H370 GAMING',
              'MSI H370M BAZOOKA', 'MSI Z370 GAMING', 'MSI Z370 GODLIKE', 'MSI Z370 KRAIT',
              'MSI Z370 PC PRO', 'MSI Z370 SLI PLUS', 'MSI Z370 TOMAHAWK', 'MSI Z370-A PRO',
              'MSI Z370I GAMING PRO', 'MSI Z370M GAMING PRO', 'MSI Z370M MORTAR']

asrock_intel9 = ['ASRock Z370M-ITX/ac', 'ASRock Z370M Pro4', '	ASRock Z370 Taichi',
                 'ASRock Z370 Pro4', 'ASRock Z370 Killer SLI', 'ASRock Z370 Extreme4',
                 'ASRock H370M-ITX/ac', 'ASRock H370M Pro4', 'ASRock H370 Pro4',
                 'ASRock H310M-ITX/ac', 'ASRock H310M-HDV', 'ASRock H310M-G/M.2',
                 'ASRock H310M-DGS', 'ASRock Fatal1ty Z370', 'ASRock Fatal1ty H370 Performance',
                 'ASRock Fatal1ty B360 Gaming K4', 'ASRock B360M-ITX/ac', 'ASRock B360M-HDV',
                 'ASRock B360M Pro4', 'ASRock B360M Performance', 'ASRock B360 Pro4']

intel_9_base = ['Z390', 'B365']

intel_9_mobo_para = intel_9_base + asus_intel9 + \
    giga_intel9 + msi_intel9 + asrock_intel9

mobo_dict = []
for chipset in intel_9_mobo_para:
    for motherboard in mobo_info:
        if chipset in motherboard['name']:
            if motherboard['price'] != '':
                mobo_dict.append(motherboard)

print(len(mobo_info))
print(len(mobo_dict))
print(mobo_dict)
