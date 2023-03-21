import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def pick_browser(browser_name):
    if browser_name.lower() == 'chrome':
        browser = webdriver.Chrome(ChromeDriverManager().install())
        return browser
    elif browser_name.lower() == 'firefox':
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        return browser
    else:
        print(f"Unsupported browser: {browser_name}")


def Openurl(URL, expected_title):
    browser.get(URL)
    browser.maximize_window()
    print("\nBrowser opened successful: {}\n".format(URL))
    # Get the page title and verify it
    actual_title = browser.title
    if expected_title == actual_title:
        print("Page title verification passed!")
    else:
        print(f"Page title verification failed! Expected: '{expected_title}', but got: '{actual_title}'")

    # Take a screenshot of the page and save it to a file
    filename = f"{expected_title}.png"
    browser.save_screenshot(filename)
    print(f"Screenshot saved to '{filename}'\n")


def clickOnElement(elementID, elemenLctType):
    try:
        element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((elemenLctType, elementID)))
        element.click()
        print(f'clickOnElement: {elementID} by element locator type {elemenLctType} -- PASSED')

    except Exception as e:
        print(e)
        print(f'clickOnElement: {elementID} by element locator type {elemenLctType} -- FAILED')


def typeInElement(elementID, elemenLctType, value):
    try:
        element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((elemenLctType, elementID)))
        element.send_keys(value)
        print(f'typeInElement: {elementID} by element locator type {elemenLctType} -- PASSED')
    except Exception as e:
        print(e)
        print(f'typeInElement: {elementID} by element locator type {elemenLctType} -- FAILED')


def validateValue(elementID, elemenLctType, assertValue):
    try:
        element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((elemenLctType, elementID)))
        value = element.text
        if value == assertValue:
            print(f"Expected value: {assertValue}; Value Found: {value}.")
            print(f"Assert value: {assertValue} found -- PASSED")
        else:
            print(f"Expected value: {assertValue}; Value Found: {value}.")
            print(f"Assert value: {assertValue} not found -- FAILED")

    except Exception as e:
        print(e)
        print(f'validateValue: {elementID} by element locator type {elemenLctType} -- FAILED')


# Pick browser
browser_list = ['chrome', 'firefox']

for browser_name in browser_list:
    # Pick browser
    browser = pick_browser(browser_name)  # firs chrome then firefox
    print(f"\nBrowser: {browser_name}")

    ################## open the url: https://ultimateqa.com/automation/  ##################
    Openurl("https://ultimateqa.com/automation/", 'Automation Practice - Ultimate QA')

    # Click on login
    clickOnElement('/html/body/div[1]/div/div/div/article/div/div[1]/div/div[2]/div/div[1]/div/div/div/div/ul/li[6]/a',
                   By.XPATH)

    # input username and password
    typeInElement('user[email]', By.ID, 'aman.nigussie@gmail.com')
    typeInElement('user[password]', By.ID, 'superamanuel')

    # click Sign in
    clickOnElement('/html/body/main/div/div/article/form/div[5]/button', By.XPATH)
    time.sleep(3)

    # Verify that you signed in
    validateValue('/html/body/main/div/h2', By.XPATH, 'Products')

    # Click on the sign out nav
    clickOnElement('/html/body/header/div[2]/div/nav/ul/li[2]/button/i', By.XPATH)
    time.sleep(1)

    # Logout
    clickOnElement("/html/body/header/div[2]/div/nav/ul/li[2]/ul/li[4]/a", By.XPATH)

    ################## open the url: https://ultimateqa.com/filling-out-forms/ ##################
    # Browse to "Fill out forms" page and complete all forms, followed by submit action
    Openurl("https://ultimateqa.com/filling-out-forms/", 'Filling Out Forms - Ultimate QA')

    # Type name
    typeInElement('et_pb_contact_name_0', By.ID, 'Amanuel')

    # Type Message
    typeInElement('et_pb_contact_message_0', By.ID, 'This is a message from amanuel')

    # Click submit
    clickOnElement("et_builder_submit_button", By.NAME)

    ################## open the url: https://ultimateqa.com/automation/fake-pricing-page/ ##################
    # Browse to the "Fake Pricing Page" and Purchase the Basic package
    Openurl("https://ultimateqa.com/automation/fake-pricing-page/", 'Fake pricing page - Ultimate QA')

    # Click on the basic package
    clickOnElement("/html/body/div[1]/div/div/div/article/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div[4]/a",
                   By.XPATH)
