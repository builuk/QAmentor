import time

from behave import given, when, then
from helper.data import base
from features.pages import base as pages
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@when('I open Homepage')
def open_homepage(context):
    option = Options()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    option.add_experimental_option("prefs", prefs)
    context.browser = webdriver.Chrome(options=option)
    context.base_page = pages.BasePage(context.browser)
    context.base_page.open()


@when('I open Homepage custom size screen "{size}"')
def open_homepage(context, size):
    option = Options()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    option.add_experimental_option("prefs", prefs)
    option.add_argument(f"--window-size={getattr(base, size)}")
    context.browser = webdriver.Chrome(options=option)
    context.base_page = pages.BasePage(context.browser)
    context.base_page.open()


@then('I switch to ua language')
def switch_to_ua(context):
    context.base_page.switch_to_ua()


@then('I click on About button')
def click_about(context):
    context.base_page.open_about()


@then('I click on "{button}" button')
def click_about(context, button):
    context.base_page.open_header_button(button)


@given('I see title "{title}"')
def check_title(context, title):
    expected_title = getattr(base, title)
    actual_title = context.base_page.return_title(expected_title)
    assert actual_title == expected_title, f"Expected title: {expected_title}, but got: {actual_title}"
