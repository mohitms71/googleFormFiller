from selenium import webdriver
import time
count=0

browser = webdriver.Chrome("C:\\Users\\asus\\Downloads\\chromedriver")
browser.get('https://docs.google.com/forms/d/e/1FAIpQLSfxsg59ggPdonbOLakPTwn_qQk-P0euw531kGt2pdDxSlnB9Q/viewform')
while(count<100):
    d=browser.find_element_by_name('entry.1156409')
    d.send_keys("Mohit Sharma")
    time.sleep(1)
    e=browser.find_element_by_name('entry.210055283')
    e.send_keys("190508")
    time.sleep(1)
    f=browser.find_element_by_class_name("appsMaterialWizToggleRadiogroupRadioButtonContainer")
    f.click()
    time.sleep(1)
    g=browser.find_element_by_name('entry.446099277')
    g.send_keys("https://github.com/slayer747/8-languages-in-8-weeks.github.io")
    time.sleep(1)
    submit=browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonLabel")
    submit.click()
    time.sleep(1)
    h=browser.find_element_by_link_text("Submit another response")
    h.click()
    count=count+1
    

