from selenium import webdriver
#driver = webdriver.Chrome(executable_path="chromedriver")
driver = webdriver.PhantomJS()
driver.get("https://duckduckgo.com/")
driver.find_element_by_id('search_form_input_homepage').send_keys("realpython")
driver.find_element_by_id("search_button_homepage").click()
driver.quit()
print("success")