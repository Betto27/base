from selenium import webdriver
from nose.tools import assert_equal

driver = webdriver.Chrome()
driver.get('https://www.youtube.com')
driver.maximize_window()

res = driver.find_element_by_css_selector('#sections > ytd-guide-signin-promo-renderer > yt-formatted-string').text
print(res)
print(driver.title)
if assert_equal(driver.title, 'YouTube'):
    print('Testes passou')

else:
    print('Teste falhouuuuuuuuuuuuuuuuuuuu')



driver.close()