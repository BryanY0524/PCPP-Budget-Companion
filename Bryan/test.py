from PCPartPicker_API import pcpartpicker as pcpp

print("Total Storage pages:", pcpp.productLists.totalPages("internal-hard-drive"))
storage_info = pcpp.productLists.getProductList("internal-hard-drive")

print(storage_info)
