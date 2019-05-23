from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from django.contrib.auth.models import User

class MySeleniumTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.selenium = WebDriver()
        # self.selenium.implicitly_wait(10)
        self.myGoodTestPassword = 'aTestPassword'
        self.user = User.objects.create_user(username='testuser', email='testUser@test.com', password=self.myGoodTestPassword)

    @classmethod
    def tearDownClass(self):
        self.selenium.quit()
        super().tearDownClass()

    def test_login_failed(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/account/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('myuser')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('secret')
        self.selenium.find_element_by_xpath('//button[@type="submit" and text()="Se connecter"]').click()

        #Test we stay on the same page
        page_url = self.selenium.current_url
        self.assertEqual(page_url, '%s%s' % (self.live_server_url, '/account/login/'), "Wrong login should stay on the same login page")
        #Test that error messages are displayed
        error_message = self.selenium.find_elements_by_xpath('//ul[@class="errorlist nonfield"]')
        self.assertGreater(len(error_message), 0, "Wrong login should return at least 1 error message")

    def test_login_success(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/account/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys(self.user.username)
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys(self.myGoodTestPassword)
        self.selenium.find_element_by_xpath('//button[@type="submit" and text()="Se connecter"]').click()
        
        #Test we stay on the same page
        page_url = self.selenium.current_url
        self.assertEqual(page_url, '%s%s' % (self.live_server_url, '/'), "Good login should redirect on index page")
        #Test that no error messages are displayed
        error_message = self.selenium.find_elements_by_class_name("errorlist")
        self.assertEqual(len(error_message), 0, "Good login, no error message shloud be displayed")