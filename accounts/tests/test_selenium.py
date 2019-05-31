from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from django.contrib.auth.models import User

class MySeleniumTests(StaticLiveServerTestCase):

    
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(chrome_options=options)
        self.myGoodTestPassword = 'aTestPassword'
        self.user = User.objects.create_user(username='testuser', email='testUser@test.com', password=self.myGoodTestPassword)

    
    def tearDown(self):
        self.driver.quit()
    
    def login(self, username, password):
        self.driver.get('%s%s' % (self.live_server_url, '/account/login/'))
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys(username)
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit" and text()="Se connecter"]').click()

    def test_login_wrong_user(self):
        self.login('wrongUser', self.myGoodTestPassword)
        #Test we stay on the same page
        page_url = self.driver.current_url
        self.assertEqual(page_url, '%s%s' % (self.live_server_url, '/account/login/'), "Wrong login should stay on the same login page")
        #Test that error messages are displayed
        error_message = self.driver.find_elements_by_xpath('//ul[@class="errorlist nonfield"]')
        self.assertGreater(len(error_message), 0, "Wrong login should return at least 1 error message")

    def test_login_wrong_password(self):
        self.login(self.user.username, 'wrongPassword')
        #Test we stay on the same page
        page_url = self.driver.current_url
        self.assertEqual(page_url, '%s%s' % (self.live_server_url, '/account/login/'), "Wrong login should stay on the same login page")
        #Test that error messages are displayed
        error_message = self.driver.find_elements_by_xpath('//ul[@class="errorlist nonfield"]')
        self.assertGreater(len(error_message), 0, "Wrong login should return at least 1 error message")

    def test_login_wrong_user_password(self):
        self.login('wrongUser', 'wrongPassword')
        #Test we stay on the same page
        page_url = self.driver.current_url
        self.assertEqual(page_url, '%s%s' % (self.live_server_url, '/account/login/'), "Wrong login should stay on the same login page")
        #Test that error messages are displayed
        error_message = self.driver.find_elements_by_xpath('//ul[@class="errorlist nonfield"]')
        self.assertGreater(len(error_message), 0, "Wrong login should return at least 1 error message")

    def test_login_success(self):
        self.login(self.user.username, self.myGoodTestPassword)
        #Test we stay on the same page
        page_url = self.driver.current_url
        self.assertEqual(page_url, '%s%s' % (self.live_server_url, '/'), "Good login should redirect on index page")
        #Test that no error messages are displayed
        error_message = self.driver.find_elements_by_class_name("errorlist")
        self.assertEqual(len(error_message), 0, "Good login, no error message shloud be displayed")