# test_login.py
import requests
from login_page import LoginPage
import allure

@allure.step('Test of correct login page')
def test_correct_login(browser, link, username_pass_dict):
    
    for username, password in username_pass_dict.items():
        login_page = LoginPage(browser, link)
        login_page.elems_correct_check()
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()
        status = requests.get(link).status_code
        print(f'{status} Done\n')


@allure.step('Test of incorrect login page')
def test_incorrect_login(browser, link, username_pass_dict, error_list):
    
    for username, password in username_pass_dict.items():
        login_page = LoginPage(browser, link)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()
        status = requests.get(link).status_code
        actual_error = login_page.get_error_message_text()
        print(f'{status} {actual_error}')
        for error in error_list:
            assert actual_error, error
        print('Done\n')
        


   
    


