from selenium import webdriver
from time import sleep

browser=webdriver.Chrome('C:\Driver\chromedriver.exe')
browser.get('https://loblaws.dev.precima.io/login')
browser.maximize_window()
browser.find_element_by_css_selector('#md-input-1').send_keys('smahajan2')
browser.find_element_by_css_selector('#passwordInput').send_keys('$aTW4d5R')
browser.find_element_by_css_selector('.mat-button-ripple.mat-ripple').click()

sleep(5)
browser.find_element_by_xpath("//div[@class='header-bar-options-choice'][contains(text(),'ADVANCED ANALYTICS')]").click()
sleep(5)
browser.switch_to.window(browser.window_handles[1])
browser.find_element_by_xpath("//div[contains(text(),'Queued Reports')]").click()
browser.find_element_by_css_selector('#qa-reportlist').click()
browser.find_element_by_css_selector('#md-option-2').click()







