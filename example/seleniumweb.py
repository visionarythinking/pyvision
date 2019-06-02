from selenium import webdriver
driver =webdriver.Chrome("D:/gitrepository/pyvision/webdriver/chromedriver")
driver.get("https://www.youtube.com/user/noobtoprofessional")
driver.find_element_by_xpath('//a[contains(text(),"Why you should learn Python Programming")]').click()
