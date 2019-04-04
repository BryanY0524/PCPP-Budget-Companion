from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://ca.pcpartpicker.com/list/#partlist_remove_all")

# Find the object to interact with.
#driver.find_element_by_class_name("foo").click()

# New tabs will be the last object in window_handles
#driver.switch_to.window(driver.window_handles[-1])

# close the tab
driver.close()

# switch to the main window
#driver.switch_to.window(driver.window_handles[0])
