from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.steps.test_base import BaseTest
# from pytest_bdd import scenarios, given, when, then

# scenarios('../features/login.feature')

class Test_Login(BaseTest):

    # @given('the user access the Order Management Page')
    def test_signup_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_signup_link_exists()
        assert flag

    # @then('the user access the To be prepared sub-tab')
    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        # title = self.loginPage.get_title()
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        # print("222222222222222222222222222")
        # print(title)
        assert title == TestData.LOGIN_PAGE_TITLE

    # @when('the user clicks on the first order')
    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
