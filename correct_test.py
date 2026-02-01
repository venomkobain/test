from selenium import webdriver
from main import test_correct_login as test

browser = [webdriver.Chrome(), 
           webdriver.Firefox()]

correct_username_pass_dict = {"standard_user":"secret_sauce",
                              "performance_glitch_user":"secret_sauce",
                              }

for driver in browser:

    print('----- First test - with correct login data -----')
    test(driver, "https://www.saucedemo.com/", correct_username_pass_dict)
    driver.quit()

