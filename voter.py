import random

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def find_option_selectors(driver, timeout):
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, 'select-placeholder')))
    return driver.find_elements_by_class_name("select-placeholder")


def get_important_person(option_list, order):
    options = option_list.find_elements_by_xpath("./li/div/span")

    def ordering(x):
        x = x.text
        if x in order:
            return priority_order[x]
        return 0

    results = list(map(ordering, options))

    if any(results):
        return max(options, key=ordering)

    return options[random.randint(0, len(options) - 1)]


def go_though_options(driver, question_option_list, timeout, order):
    for element in question_option_list:
        element.click()

        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'select-option-menu-container')))
        option_list = driver.find_element_by_class_name("select-option-menu-container")

        option = get_important_person(option_list, order)
        option.click()


def fill_in_other(driver):
    inputs = driver.find_elements_by_xpath(
        '//input[../../..//div//div//span[.="Other"]]')

    preferd_input = max(priority_order.keys(), key=lambda x: priority_order[x])

    for textfield in inputs:
        textfield.send_keys(preferd_input)


def submit(driver):
    submit_button = driver.find_element_by_class_name("button-content")
    submit_button.click()


def resubmit(driver, timeout):
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, '//a[.="Submit another response"]')))
    driver.find_element_by_xpath('//a[.="Submit another response"]').click()

