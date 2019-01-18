from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

if __name__ == '__main__':
    priority_order = {"W. Hubbard": 2, "Vernon": 1}

    driver = Chrome()

    url = "http://tinyurl.com/votehubbard"

    driver.get(url)

    delay = 10

    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'select-placeholder')))
    selections = driver.find_elements_by_class_name("select-placeholder")

    for element in selections:
        element.click()

        WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'select-option-menu-container')))
        option_list = driver.find_element_by_class_name("select-option-menu-container")

        options = option_list.find_elements_by_xpath("./li/div/span")


        def ordering(x):
            x = x.text
            if x in priority_order:
                return priority_order[x]
            return 0


        option = max(options, key=ordering)
        option.click()


def submit(driver):
    submit_button = driver.find_element_by_class_name("button-content")
    submit_button.click()

    driver.close()
