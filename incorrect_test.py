from selenium import webdriver
from main import test_incorrect_login as test

browser = [webdriver.Chrome(), 
           webdriver.Firefox()]


incorrect_username_pass_dict = {
        
        "standard_user":"password",
        "locked_out_user":"secret_sauce",
        "":"",
}

correctusername_clearpass={"standard_user":"",}

error_list = ['Epic sadface: Username and password do not match any user in this service',
          'Epic sadface: Sorry, this user has been locked out.',
          'Epic sadface: Username is required',
          'Epic sadface: Password is required']

for driver in browser:
    print('----- Second test - with incorrect login data -----')
    test(driver, "https://www.saucedemo.com/", incorrect_username_pass_dict, error_list)
    driver.quit()

    print('----- Third test - with correct username and clear password -----')
    test(driver, "https://www.saucedemo.com/", correctusername_clearpass, error_list)
    driver.quit()
