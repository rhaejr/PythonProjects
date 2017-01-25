"""air squat, front squat, overhead squat, shoulder press, push press, push jerk, deadlift, medicine-ball clean,
Sumo Deadlift High Pull, Thruster, Wall Ball, Pull-up"""

import requests
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait

browser = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
browser.get("https://www.crossfit.com/exercisedemos/")

for i in browser.find_elements_by_tag_name("strong"):
    print(i.text)