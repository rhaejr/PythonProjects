import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
import time
import sqlite3
import smtplib
from datetime import datetime

def loop():
    conn = sqlite3.connect("wages.db")
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS state(
    state TEXT PRIMARY KEY NOT NULL
    );''')


    cur.execute('''CREATE TABLE IF NOT EXISTS counties(
    state TEXT NOT NULL,
    county TEXT NOT NULL,
    date      TEXT     NOT NULL,
    link      TEXT  ,
    FOREIGN KEY(state) REFERENCES state(state)
    );''')

    # file = open('links.txt','w')
    state = "SelectedState"
    type = "SelectedType"
    Stype = "R"
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

    state_select = browser.find_element_by_xpath("//select[@id='SelectedState']")  # get the select element
    state_options = state_select.find_elements_by_tag_name("option")  # get all the options into a list

    state_optionsList = []

    for state_option in state_options:  # iterate over the options, place attribute value in list
        state_optionsList.append(state_option.get_attribute("value"))

    for state_optionValue in state_optionsList:
        # conn.commit()
        # cur.execute("select state from state")
        # skip = False
        # for i in cur.fetchall():
        #     if state_optionValue in i:
        #         skip = True

        if state_optionValue != '':# and skip == False:
            cur.execute("INSERT OR IGNORE INTO state VALUES('{}')".format(state_optionValue))
            print("starting loop on option %s" % state_optionValue)
            # file.write('{}\n'.format(state_optionValue))
            state_select = Select(browser.find_element_by_xpath("//select[@id='SelectedState']"))
            state_select.select_by_value(state_optionValue)

            time.sleep(1)
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
            time.sleep(3)
            county_select = browser.find_element_by_xpath("//select[@id='SelectedCounty']")  # get the select element
            county_options = county_select.find_elements_by_tag_name("option")  # get all the options into a list

            county_optionsList = []

            for county_option in county_options:  # iterate over the options, place attribute value in list
                county_optionsList.append(county_option.get_attribute("value"))

            for county_optionValue in county_optionsList:
                conn.commit()
                counties = cur.execute("select county from counties where state='{}'".format(state_optionValue)).fetchall()


                skip_county = False
                for i in counties:
                    if county_optionValue in i:
                        skip_county = True
                if county_optionValue != '' and skip_county == False:

                    print("starting loop on option %s" % county_optionValue)
                    # file.write('{}\n'.format(county_optionValue))
                    county_select = Select(browser.find_element_by_xpath("//select[@id='SelectedCounty']"))
                    county_select.select_by_value(county_optionValue)

                    time.sleep(1)

                    try:
                        doc_select = Select(browser.find_element_by_xpath("//select[@id='SelectedDocumentType']"))
                    except selenium.common.exceptions.NoSuchElementException:
                        time.sleep(3)
                        doc_select = Select(browser.find_element_by_xpath("//select[@id='SelectedDocumentType']"))
                    doc_select.select_by_value("html")

                    time.sleep(1)

                    date_select = browser.find_element_by_xpath(
                        "//select[@id='SelectedScheduleYear']")  # get the select element
                    date_options = date_select.find_elements_by_tag_name("option")  # get all the options into a list

                    date_optionsList = []

                    for date_option in date_options:  # iterate over the options, place attribute value in list
                        date_optionsList.append(date_option.get_attribute("value"))

                    for date_optionValue in date_optionsList:
                        if date_optionValue != '':
                            print("starting loop on option %s" % date_optionValue)
                            # file.write('{}\n'.format(date_optionValue))

                            date_select = Select(browser.find_element_by_xpath("//select[@id='SelectedScheduleYear']"))
                            date_select.select_by_value(date_optionValue)
                            county_optionValue_sep = county_optionValue.split(',')
                            # print(county_optionValue_sep)
                            link_builer = (county_optionValue_sep[0],county_optionValue_sep[1])
                            link = 'https://www.cpms.osd.mil/Content/AF%20Schedules/survey-sch/{}/{}R-{}.html'.format(link_builer[0],link_builer[1],date_optionValue)
                            print(link)
                            cur.execute(
                                                'INSERT INTO counties VALUES ("{}","{}", "{}", "{}")'.format(state_optionValue,
                                                                                                             county_optionValue,
                                                                                                             date_optionValue,
                                                                                                             link))

                            # time.sleep(.3)
                            # links = browser.find_elements_by_tag_name('a')
                            # try:
                            #     for link in links:
                            #         link = link.get_attribute('href')
                            #         if date_optionValue in link:
                            #             print(link)
                            #             # file.write('{}\n'.format(link.get_attribute('href')))
                            #             cur.execute(
                            #                 "INSERT INTO counties VALUES ('{}','{}', '{}', '{}')".format(state_optionValue,
                            #                                                                              county_optionValue,
                            #                                                                              date_optionValue,
                            #                                                                              link))
                            #             break
                            # except selenium.common.exceptions.StaleElementReferenceException:
                            #     links = browser.find_elements_by_tag_name('a')
                            #     outer_link = ''
                            #     for link in links:
                            #         link = link.get_attribute('href')
                            #         if date_optionValue in link:
                            #             outer_link = link
                            #             print(outer_link)
                            #             # file.write('{}\n'.format(link.get_attribute('href')))
                            #             cur.execute(
                            #                 "INSERT INTO counties VALUES ('{}','{}', '{}', '{}')".format(state_optionValue,
                            #                                                                              county_optionValue,
                            #                                                                              date_optionValue,
                            #                                                                              outer_link))
                            #             break

                                        # file.close()
    conn.close()

if __name__ == "__main__":
    not_done = True
    while not_done:
            try:
                loop()
                not_done = False
            except:
                conn = sqlite3.connect("wages.db")
                cur = conn.cursor()
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login('av8r.08@gmail.com', '1111aasfULLS$$')
                server.sendmail('av8r.08@gmail.com', '6623466983@vtext.com', 'Code Stopped!\n{}\n{}'.format(
                    cur.execute("SELECT count(*) FROM counties").fetchall()[0][0],
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                conn.close()
