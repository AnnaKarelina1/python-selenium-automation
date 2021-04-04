class Page:

    def __init__(self,driver):
        self.driver=driver

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        e=self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def open_url(self,url):
        self.driver.get(url)

    def verify_text(self,expected_text,*locator ):
        actual_text=self.driver.find_element(*locator).text
        assert actual_text==expected_text, f'Expected result {expected_text},but got {actual_text}'

    def verify_url_contains_text(self,text):
        assert f'{text}' in self.driver.current_url, f'{text}is not in {self.driver.current_url}'