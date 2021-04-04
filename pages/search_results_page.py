from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResultsPage(Page):
    SEARCH_QUERY_TEXT_RESULT = (By.CSS_SELECTOR, 'span.a-color-state.a-text-bold')

    def verify_search_result(self,search_result):
       self.verify_text(search_result,*self.SEARCH_QUERY_TEXT_RESULT )


    def verify_search_in_url(self,search_word):
        self.verify_url_contains_text(search_word)

# @then ('Verify {search_result} in URL')
# def verify_url(context, search_result):
#     assert f'{search_result}' in context.driver.current_url
#