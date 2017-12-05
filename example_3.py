from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://duckduckgo.com/")
element = driver.find_element_by_id('search_form_input_homepage')
print(element)
element.send_keys(str('a'))
#driver.find_element_by_id("search_button_homepage").click()
driver.quit()