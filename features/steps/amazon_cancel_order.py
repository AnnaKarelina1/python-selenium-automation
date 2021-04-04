
from behave import given, when, then

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

AMAZON_HELPSEARCH =(By.ID, 'helpsearch')
HELP_SEARCH_RESULT=(By.XPATH, "//div[@class='help-content']/h1")


@given('Open Amazon Help page')
def open_help(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html")


@when('Input {search_input} into "Search the help library" and click')
def input_cancel(context,search_input):
    context.driver.find_element(*AMAZON_HELPSEARCH).send_keys(f'{search_input}', Keys.ENTER)

@then ('Verify {search_input_result} is present')
def cancel_order(context,search_input_result):
    actual_text=context.driver.find_element(*HELP_SEARCH_RESULT).text
    expected_text=f'{search_input_result}'
    assert actual_text ==expected_text, f"Expected text is {expected_text} but got {actual_text}"
