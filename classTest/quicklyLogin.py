# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select


user_file = open('file/login.txt', 'r')
values = user_file.readlines()
i=[]
for search in values:
    i.append(search)

user_file.close()
driver=webdriver.Chrome()
driver.get('http://123.206.57.62:17000/index')
driver.maximize_window()
# driver.find_element_by_class_name('selectpicker').click()
# driver.find_element_by_class_name("selectpicker").click()
# d=driver.find_elements_by_tag_name('option')
# d[0].click()
# driver.find_element_by_name('password').send_keys(u"123456")
# driver.find_element_by_name('telphone').send_keys(u"18888888888")
s=Select(driver.find_element_by_class_name("selectpicker"))
s.select_by_value('1')
# for select in s.options:
#     print select.text
# driver.find_element_by_class_name("selectpicker").find_elements_by_tag_name("option")[2].click()
username=i[0].split(',')[0]
password=i[0].split(',')[1]
driver.find_element_by_name('telphone').send_keys(username)
driver.find_element_by_name('password').send_keys(password)
# driver.find_element_by_name('loginBtn').click()
driver.implicitly_wait(10)
lis=driver.find_elements_by_tag_name('li')
print lis
lis[2].click()
driver.find_element_by_link_text('商品列表').click()


