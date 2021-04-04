
from selenium.webdriver.common.by import By
from behave import given, when,then


SEARCH_FIELD=(By.ID, 'twotabsearchtextbox')
SEARCH_ICON=(By.ID, 'nav-search-submit-button')
SEARCH_QUERY_TEXT_RESULT=(By.CSS_SELECTOR,'span.a-color-state.a-text-bold')


@given ('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main_page()
#
#
@when ('Input {search_query} into Amazon search field')
def input_search(context, search_query):
    context.app.main_page.input_amazon_search(search_query)

@when ('Click on Amazon search icon')
def click_search_icon(context):
    context.app.main_page.click_search_amazon()

@then('Product results for {search_result} are shown on Amazon')
def search_result(context, search_result):
    context.app.search_results_page.verify_search_result(search_result)

@then ('Verify {search_word} in URL')
def verify_url(context, search_word):
    context.app.search_results_page.verify_search_in_url(search_word)

# @then('Product results for {search_result} are shown on Amazon')
# def search_result(context, search_result):
#     actual_text=context.driver.find_element(*SEARCH_QUERY_TEXT_RESULT).text
#     expected_text = f'{search_result}'
#     assert expected_text==actual_text,f'Expected result {expected_text},but got {actual_text}'
# #

# @then('Product results for {search_result} are shown on Amazon')
# def search_result(context, search_result):
#     actual_text=context.driver.find_element(*SEARCH_QUERY_TEXT_RESULT).text
#     expected_text = f'{search_result}'
#     assert expected_text==actual_text,f'Expected result {expected_text},but got {actual_text}'
#
# @then ('Verify {search_result} in URL')
# def verify_url(context, search_result):
#     assert f'{search_result}' in context.driver.current_url
#
# # @then ('First result for dress shown on Amazon')
