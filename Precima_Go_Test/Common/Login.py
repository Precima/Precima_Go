from selenium import webdriver
from time import sleep

browser=webdriver.Chrome('C:\Driver\chromedriver.exe')
browser.get('https://loblaws.pilot.precima.io/main/home')

browser.find_element_by_css_selector('#md-input-1').send_keys('smahajan2')
browser.find_element_by_css_selector('#passwordInput').send_keys('$aTW4d5R')
browser.find_element_by_css_selector('.mat-button-ripple.mat-ripple').click()
sleep(5)
browser.find_element_by_css_selector('.header-bar-options-choices > div:nth-child(2').click()
sleep(5)
browser.switch_to.window(browser.window_handles[1])
browser.find_element_by_css_selector('tr.rowLink[data-qa="CSD - Pepsi Vs Coke"]').click()
sleep(5)
browser.quit()




