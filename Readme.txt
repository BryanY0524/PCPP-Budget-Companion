Before running the program, please run the following codes in python terminal:
pip install PCPartPicker_API
pip install selenium

The PCPartPicker_API enable thes scraper to collect Data from PCPacker website, 
and Selenium enables the webdriver to control Chrome.

If Web-pages does not open properly after a build is selected,
Please go onto this website:
http://chromedriver.chromium.org/downloads

download the corresponding chrome webdriver, and then put it under the same directory as the program.

To start the Program, Run "menu.py"

If you selected to create a Build with guided parameters, after All the parameters are selected, 
'ONE' Build would be generated, and the webdriver would open up 'ONE' Chrome browser.

if you selected to create a Build by choose computer type and giving budget only,
'TWO' Builds would be generated, and the webdriver would open up 'TWO' Chrome browsers.
One for Intel CPU, another with AMD CPU


