from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def wait_for_element_located(driver, xpath):
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath)))


def wait_title(driver, new_title):
    WebDriverWait(driver, 10).until(
        EC.title_is(new_title)
    )
