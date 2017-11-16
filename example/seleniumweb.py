from selenium import webdriver
driver =webdriver.Chrome("/Users/Anass.Ben/AppData/Local/Programs/Python/Python36/Training/chromedriver")
driver.get("https://www.youtube.com/user/noobtoprofessional")
driver.find_element_by_xpath('//a[contains(text(),"Why you should learn Python Programming")]').click()
