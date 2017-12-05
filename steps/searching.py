
from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@given('we have navigated to "amazon.com"')
def step_impl(context):
    #context.driver = webdriver.Chrome(executable_path="chromedriver")
    context.driver = webdriver.PhantomJS()
    context.driver.get("http://amazon.com")
    assert "Amazon" in context.driver.title

@when('we search for "{target}"')
def step_impl(context, target):
    search_box = context.driver.find_element_by_id("twotabsearchtextbox")
    search_box.clear()
    search_box.send_keys(target)
    search_box.send_keys(Keys.RETURN)

@then(u'we will find results')
def step_impl(context):
    sResultCount = context.driver.find_element_by_id("s-result-count")
    assert "results for" in sResultCount.text

@then('we will find 0 results')
def step_impl(context):
    noResultsTitle = context.driver.find_element_by_id("noResultsTitle")
    print(noResultsTitle.text)
    zero_results = "0 results" in noResultsTitle.text 
    no_match = "did not match any" in noResultsTitle.text 
    assert zero_results or no_match