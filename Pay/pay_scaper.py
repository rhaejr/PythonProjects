import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
import time
file = open('links.txt','w')
state = "SelectedState"
type = "SelectedType"
Stype= "R"
wage_area = "SelectedGSLocality"
doc_type = "SelectedDocumentType"
year = "SelectedScheduleYear"

def find(value):
    element = browser.find_elements_by_partial_link_text(value)
    if element:
        return element
    else:
        return False
# element = WebDriverWait(driver, secs).until(find)

browser = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
browser.get("https://www.cpms.osd.mil/Subpage/AFWageSchedules/")

state_select = browser.find_element_by_xpath("//select[@id='SelectedState']")  #get the select element
state_options = state_select.find_elements_by_tag_name("option") #get all the options into a list

state_optionsList = []

for state_option in state_options: #iterate over the options, place attribute value in list
    state_optionsList.append(state_option.get_attribute("value"))

for state_optionValue in state_optionsList:
    if state_optionValue != '':
        print("starting loop on option %s" % state_optionValue)
        file.write('{}\n'.format(state_optionValue))
        state_select = Select(browser.find_element_by_xpath("//select[@id='SelectedState']"))
        state_select.select_by_value(state_optionValue)

        time.sleep(.5)
        type_select = browser.find_element_by_xpath("//select[@id='SelectedType']")
        type_options = type_select.find_elements_by_tag_name("option")

        # type_optionsList = []
        # for type_option in type_options:
        #     type_optionsList.append(type_option.get_attribute("value"))

        # for type_optionValue in type_optionsList:
        #     print(state_optionValue)

        type_select = Select(browser.find_element_by_xpath("//select[@id='SelectedType']"))
        type_select.select_by_value("R")

        radio_select = browser.find_element_by_id('countyRadioButton')
        radio_select.click()
        time.sleep(.5)
        county_select = browser.find_element_by_xpath("//select[@id='SelectedCounty']")  # get the select element
        county_options = county_select.find_elements_by_tag_name("option")  # get all the options into a list

        county_optionsList = []

        for county_option in county_options:  # iterate over the options, place attribute value in list
            county_optionsList.append(county_option.get_attribute("value"))

        for county_optionValue in county_optionsList:
            if county_optionValue != '':
                print("starting loop on option %s" % county_optionValue)
                file.write('{}\n'.format(county_optionValue))
                county_select = Select(browser.find_element_by_xpath("//select[@id='SelectedCounty']"))
                county_select.select_by_value(county_optionValue)

                time.sleep(.5)

                try:
                    doc_select = Select(browser.find_element_by_xpath("//select[@id='SelectedDocumentType']"))
                except selenium.common.exceptions.NoSuchElementException:
                    time.sleep(1)
                    doc_select = Select(browser.find_element_by_xpath("//select[@id='SelectedDocumentType']"))
                doc_select.select_by_value("html")

                time.sleep(.5)

                date_select = browser.find_element_by_xpath("//select[@id='SelectedScheduleYear']")  # get the select element
                date_options = date_select.find_elements_by_tag_name("option")  # get all the options into a list

                date_optionsList = []

                for date_option in date_options:  # iterate over the options, place attribute value in list
                    date_optionsList.append(date_option.get_attribute("value"))

                for date_optionValue in date_optionsList:
                    if date_optionValue != '':
                        print("starting loop on option %s" % date_optionValue)
                        file.write('{}\n'.format(date_optionValue))

                        date_select = Select(browser.find_element_by_xpath("//select[@id='SelectedScheduleYear']"))
                        date_select.select_by_value(date_optionValue)
                        time.sleep(.3)
                        links = browser.find_elements_by_tag_name('a')
                        try:
                            for link in links:
                                if date_optionValue in link.get_attribute('href'):
                                    print(link.get_attribute('href'))
                                    file.write('{}\n'.format(link.get_attribute('href')))
                                    break
                        except selenium.common.exceptions.StaleElementReferenceException:
                            links = browser.find_elements_by_tag_name('a')
                            for link in links:
                                if date_optionValue in link.get_attribute('href'):
                                    print(link.get_attribute('href'))
                                    file.write('{}\n'.format(link.get_attribute('href')))
                                    break

file.close()