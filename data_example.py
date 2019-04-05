import pcpp_Scrape

MASTER_LIST = pcpp_Scrape.read_JSON()

#print("CPU LIST LENGTH:", len(MASTER_LIST[0]))
#print("MOTHERBOARD LIST LENGTH:", len(MASTER_LIST[1]))
#print("MEMORY LIST LENGTH:", len(MASTER_LIST[2]))




for CPU in MASTER_LIST[0]:
    print(CPU)